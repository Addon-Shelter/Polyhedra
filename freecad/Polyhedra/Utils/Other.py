# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

#
#   The following code section provides an object that can be
#   parameterized to produce any of the platonic, archimedean
#   and catalan solids, and more, by starting with one of the
#   five platonic solids and then truncating vertices respectively edges.
#

from functools import reduce

from FreeCAD import Vector


def sum ( values : list[ Vector ] ):
    return reduce( lambda a , b : a.add(b) , values )


from .Plato import plato as source , PlatoType


# The python code of the following three functions "createSolid" is taken from Blenders add_mesh_solid.py
# from the "Add Mesh Extra Objects" addon, authored by Dreampainter, licensed as SPDX-License-Identifier GPL-2.0-or-later,
# refer https://github.com/blender/blender-addons/blob/master/add_mesh_extra_objects/add_mesh_solid.py.


# creates the 5 platonic solids as a base for the rest
#  plato: should be one of {"4","6","8","12","20"}. decides what solid the
#         outcome will be.
#  returns a list of vertices and faces


def scaled ( vertices : list[ Vector ] , factor : float ):
    return [ factor * vertex for vertex in vertices ]

def mirror ( vectors : list[ Vector ] ):
    return [ -vector for vector in vectors ]




def createSolid (
    plato : PlatoType ,
    vtrunc : float ,
    etrunc : float ,
    dual : bool ,
    snub : str
):

    # the duals from each platonic solid

    dualSource : dict[ PlatoType , PlatoType ] = {
        '20' : '12' ,
        '12' : '20' ,
         '8' :  '6' ,
         '6' :  '8' ,
         '4' :  '4'
    }

    vtrunc *= 0.5
    etrunc *= 0.5

    scale = 0

    noSnub = ( snub == 'None' ) or ( etrunc == 0.5 ) or ( etrunc == 0 )
    lSnub = ( snub == 'Left' ) and ( 0 < etrunc < 0.5 )
    rSnub = ( snub == 'Right' ) and ( 0 < etrunc < 0.5 )

    # no truncation

    if vtrunc == 0 :

        # dual is as simple as another, but mirrored platonic solid

        if dual :

            vectors , faces = source( dualSource[ plato ] )

            vector_indices = faces[ 0 ]

            vectors_per_face = len(vector_indices)

            factor = sum([ vectors[ index ] for index in vector_indices ]).Length / vectors_per_face

            vectors = mirror(vectors)
            vectors = scaled(vectors,factor)

            return vectors , faces

        return source(plato)

    # simple truncation of the source

    elif 0 < vtrunc <= 0.5 :

        vectors , faces = source(plato)

    # truncation is now equal to simple
    # truncation of the dual of the source

    else :

        vectors , faces = source(dualSource[plato])

        scale = sum(vectors[i] for i in faces[0]).Length / len(faces[0])

        # account for the source being a dual
        vtrunc = 1 - vtrunc

        # no truncation needed
        if vtrunc == 0:

            if dual:

                vectors , faces = source(plato)

                vectors = [ i * scale for i in vectors ]

                return vectors, faces

            vectors = [ -i * scale for i in vectors ]

            return vectors , faces

    # generate connection database

    vDict = [ {} for i in vectors ]

    # for every face, store what vertex comes
    # after and before the current vertex

    for face_index in range(len(faces)):

        vector_indices = faces[ face_index ]

        for vector_index in range(len(vector_indices)):

            vDict[ vector_indices[ vector_index - 1 ] ][ vector_indices[ vector_index ] ] = [ vector_indices[ vector_index - 2 ] , face_index ]

            if len(vDict[vector_indices[vector_index - 1]]) == 1:
                vDict[vector_indices[vector_index - 1]][-1] = vector_indices[vector_index]

    # the actual connection database: exists out of:
    # [vtrunc pos, etrunc pos, connected vert IDs, connected face IDs]

    vData = [[[], [], [], []] for i in vectors]

    fvOutput = []      # faces created from truncated vertices
    feOutput = []      # faces created from truncated edges
    vOutput = []       # newly created vertices

    for face_index in range(len(vectors)):

        vector_indices = vDict[face_index]   # lookup the current vertex
        current = vector_indices[-1]

        while True:    # follow the chain to get a ccw order of connected verts and faces

            vData[face_index][2].append(vector_indices[current][0])
            vData[face_index][3].append(vector_indices[current][1])

            # create truncated vertices

            vData[face_index][0].append((1 - vtrunc) * vectors[face_index] + vtrunc * vectors[vData[face_index][2][-1]])
            current = vector_indices[current][0]

            if current == vector_indices[-1]:
                break                   # if we're back at the first: stop the loop

        fvOutput.append([])             # new face from truncated vert
        fOffset = face_index * (len(vector_indices) - 1)      # where to start off counting faceVerts

        # only create one vert where one is needed (v1 todo: done)

        if etrunc == 0.5:

            for vector_index in range(len(vector_indices) - 1):
                vOutput.append((vData[face_index][0][vector_index] + vData[face_index][0][vector_index - 1]) * etrunc)  # create vert
                fvOutput[face_index].append(fOffset + vector_index)                                 # add to face

            fvOutput[face_index] = fvOutput[face_index][1:] + [fvOutput[face_index][0]]                    # rotate face for ease later on

            # create faces from truncated edges.

            for vector_index in range(len(vector_indices) - 1):
                if face_index > vData[face_index][2][vector_index]:     # only create when other vertex has been added
                    index = vData[vData[face_index][2][vector_index]][2].index(face_index)
                    feOutput.append([fvOutput[face_index][vector_index], fvOutput[face_index][vector_index - 1],
                                     fvOutput[vData[face_index][2][vector_index]][index],
                                     fvOutput[vData[face_index][2][vector_index]][index - 1]])
        # edge truncation between none and full

        elif etrunc > 0:

            for vector_index in range(len(vector_indices) - 1):

                # create snubs from selecting verts from rectified meshes

                if rSnub:
                    vOutput.append(etrunc * vData[face_index][0][vector_index] + (1 - etrunc) * vData[face_index][0][vector_index - 1])
                    fvOutput[face_index].append(fOffset + vector_index)
                elif lSnub:
                    vOutput.append((1 - etrunc) * vData[face_index][0][vector_index] + etrunc * vData[face_index][0][vector_index - 1])
                    fvOutput[face_index].append(fOffset + vector_index)
                else:   # noSnub,  select both verts from rectified mesh
                    vOutput.append(etrunc * vData[face_index][0][vector_index] + (1 - etrunc) * vData[face_index][0][vector_index - 1])
                    vOutput.append((1 - etrunc) * vData[face_index][0][vector_index] + etrunc * vData[face_index][0][vector_index - 1])
                    fvOutput[face_index].append(2 * fOffset + 2 * vector_index)
                    fvOutput[face_index].append(2 * fOffset + 2 * vector_index + 1)

            # rotate face for ease later on

            if noSnub:
                fvOutput[face_index] = fvOutput[face_index][2:] + fvOutput[face_index][:2]
            else:
                fvOutput[face_index] = fvOutput[face_index][1:] + [fvOutput[face_index][0]]

            # create single face for each edge

            if noSnub:
                for vector_index in range(len(vector_indices) - 1):
                    if face_index > vData[face_index][2][vector_index]:
                        index = vData[vData[face_index][2][vector_index]][2].index(face_index)
                        feOutput.append([fvOutput[face_index][vector_index * 2], fvOutput[face_index][2 * vector_index - 1],
                                         fvOutput[vData[face_index][2][vector_index]][2 * index],
                                         fvOutput[vData[face_index][2][vector_index]][2 * index - 1]])

            # create 2 tri's for each edge for the snubs

            elif rSnub:

                for vector_index in range(len(vector_indices) - 1):
                    if face_index > vData[face_index][2][vector_index]:
                        index = vData[vData[face_index][2][vector_index]][2].index(face_index)
                        feOutput.append([fvOutput[face_index][vector_index], fvOutput[face_index][vector_index - 1],
                                         fvOutput[vData[face_index][2][vector_index]][index]])
                        feOutput.append([fvOutput[face_index][vector_index], fvOutput[vData[face_index][2][vector_index]][index],
                                         fvOutput[vData[face_index][2][vector_index]][index - 1]])
            elif lSnub:

                for vector_index in range(len(vector_indices) - 1):
                    if face_index > vData[face_index][2][vector_index]:
                        index = vData[vData[face_index][2][vector_index]][2].index(face_index)
                        feOutput.append([fvOutput[face_index][vector_index], fvOutput[face_index][vector_index - 1],
                                         fvOutput[vData[face_index][2][vector_index]][index - 1]])
                        feOutput.append([fvOutput[face_index][vector_index - 1], fvOutput[vData[face_index][2][vector_index]][index],
                                         fvOutput[vData[face_index][2][vector_index]][index - 1]])

        # special rules for birectified mesh (v1 todo: done)

        elif vtrunc == 0.5:

            for vector_index in range(len(vector_indices) - 1):
                if face_index < vData[face_index][2][vector_index]:  # use current vert,  since other one has not passed yet
                    vOutput.append(vData[face_index][0][vector_index])
                    fvOutput[face_index].append(len(vOutput) - 1)
                else:
                    # search for other edge to avoid duplicity
                    connectee = vData[face_index][2][vector_index]
                    fvOutput[face_index].append(fvOutput[connectee][vData[connectee][2].index(face_index)])

        else:   # vert truncation only

            vOutput.extend(vData[face_index][0])   # use generated verts from way above

            for vector_index in range(len(vector_indices) - 1):   # create face from them
                fvOutput[face_index].append(fOffset + vector_index)

    # calculate supposed vertex length to ensure continuity

    if scale and not dual:                    # this to make the vtrunc > 1 work
        scale *= len(fvOutput[0]) / sum(vOutput[i] for i in fvOutput[0]).Length
        vOutput = [-i * scale for i in vOutput]

    # create new faces by replacing old vert IDs by newly generated verts

    ffOutput = [[] for i in faces]

    for face_index in range(len(faces)):

        # only one generated vert per vertex,  so choose accordingly

        if etrunc == 0.5 or (etrunc == 0 and vtrunc == 0.5) or lSnub or rSnub:
            ffOutput[face_index] = [fvOutput[i][vData[i][3].index(face_index) - 1] for i in faces[face_index]]

        # two generated verts per vertex

        elif etrunc > 0:
            for vector_indices in faces[face_index]:
                ffOutput[face_index].append(fvOutput[vector_indices][2 * vData[vector_indices][3].index(face_index) - 1])
                ffOutput[face_index].append(fvOutput[vector_indices][2 * vData[vector_indices][3].index(face_index) - 2])

        # cutting off corners also makes 2 verts

        else:
            for vector_indices in faces[face_index]:
                ffOutput[face_index].append(fvOutput[vector_indices][vData[vector_indices][3].index(face_index)])
                ffOutput[face_index].append(fvOutput[vector_indices][vData[vector_indices][3].index(face_index) - 1])

    if not dual:
        return vOutput, fvOutput + feOutput + ffOutput
    else:

        # do the same procedure as above,  only now on the generated mesh
        # generate connection database

        vDict = [{} for i in vOutput]
        dvOutput = [0 for i in fvOutput + feOutput + ffOutput]
        dfOutput = []

        # for every face
        for face_index in range(len(dvOutput)):

            vector_indices = (fvOutput + feOutput + ffOutput)[face_index]  # choose face to work with

            # find vertex from face

            normal = (vOutput[vector_indices[0]] - vOutput[vector_indices[1]]).cross(vOutput[vector_indices[2]] - vOutput[vector_indices[1]]).normalize()
            dvOutput[face_index] = normal / (normal.dot(vOutput[vector_indices[0]]))

            # create vert chain
            for vector_index in range(len(vector_indices)):

                vDict[vector_indices[vector_index - 1]][vector_indices[vector_index]] = [vector_indices[vector_index - 2], face_index]

                if len(vDict[vector_indices[vector_index - 1]]) == 1:
                    vDict[vector_indices[vector_index - 1]][-1] = vector_indices[vector_index]

        # calculate supposed size for continuity

        scale = sum([vectors[i] for i in faces[0]]).Length / len(faces[0])
        scale /= dvOutput[-1].Length
        dvOutput = [i * scale for i in dvOutput]

        # use chains to create faces

        for face_index in range(len(vOutput)):

            vector_indices = vDict[face_index]
            current = vector_indices[-1]
            face = []

            while True:

                face.append(vector_indices[current][1])
                current = vector_indices[current][0]

                if current == vector_indices[-1]:
                    break

            dfOutput.append(face)

        return dvOutput , dfOutput
