

import Part

from ..Utils.Other import createSolid

from FreeCAD import Vector , Qt


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP


# The following two classes 'RegularSolid' and 'RegularSolidCommand' make the abilities of the 'createSolid' function above
# available to FreeCAD. They also borrow somewhat on the add_mesh_solid.py referenced above:

class Regular_Solid:

    enums = {

        'Source' : (
            (  '4' , 'Tetrahedron'  , ''        ) ,
            (  '6' , 'Hexahedron'   , '' , True ) ,
            (  '8' , 'Octahedron'   , ''        ) ,
            ( '12' , 'Dodecahedron' , ''        ) ,
            ( '20' , 'Icosahedron'  , ''        )
        ),

        'Snub' : (
            (  'None' , 'No Snub'    , '' , True ) ,
            (  'Left' , 'Left Snub'  , ''        ) ,
            ( 'Right' , 'Right Snub' , ''        )
        ),

        'Presets' : (
            (    '0' , 'Custom', ''),
            (   't4' , 'Truncated Tetrahedron', ''),
            (   'r4' , 'Cuboctahedron', ''),
            (   't6' , 'Truncated Cube', ''),
            (   't8' , 'Truncated Octahedron', ''),
            (   'b6' , 'Rhombicuboctahedron', ''),
            (   'c6' , 'Truncated Cuboctahedron', '', True),
            (   's6' , 'Snub Cube', ''),
            (  'r12' , 'Icosidodecahedron', ''),
            (  't12' , 'Truncated Dodecahedron', ''),
            (  't20' , 'Truncated Icosahedron', ''),
            (  'b12' , 'Rhombicosidodecahedron', ''),
            (  'c12' , 'Truncated Icosidodecahedron', ''),
            (  's12' , 'Snub Dodecahedron', ''),
            (  'dt4' , 'Triakis Tetrahedron', ''),
            (  'dr4' , 'Rhombic Dodecahedron', ''),
            (  'dt6' , 'Triakis Octahedron', ''),
            (  'dt8' , 'Tetrakis Hexahedron', ''),
            (  'db6' , 'Deltoidal Icositetrahedron', ''),
            (  'dc6' , 'Disdyakis Dodecahedron', ''),
            (  'ds6' , 'Pentagonal Icositetrahedron', ''),
            ( 'dr12' , 'Rhombic Triacontahedron', ''),
            ( 'dt12' , 'Triakis Icosahedron', ''),
            ( 'dt20' , 'Pentakis Dodecahedron', ''),
            ( 'db12' , 'Deltoidal Hexecontahedron', ''),
            ( 'dc12' , 'Disdyakis Triacontahedron', ''),
            ( 'ds12' , 'Pentagonal Hexecontahedron', '')
        )
    }

    # actual preset values (Source, Vtrunc, Etrunc, Dual, Snub)

    p = {
          't4' : [  '4' , 2 / 3, 0, 0, 'None' ] ,
          'r4' : [  '4' , 1, 1, 0, 'None' ] ,
          't6' : [  '6' , 2 / 3, 0, 0, 'None' ] ,
          't8' : [  '8' , 2 / 3, 0, 0, 'None' ] ,
          'b6' : [  '6' , 1.0938, 1, 0, 'None' ] ,
          'c6' : [  '6' , 1.0572, 0.585786, 0, 'None' ] ,
          's6' : [  '6' , 1.0875, 0.704, 0, 'Left' ] ,
         'r12' : [ '12' , 1, 0, 0, 'None' ] ,
         't12' : [ '12' , 2 / 3, 0, 0, 'None' ] ,
         't20' : [ '20' , 2 / 3, 0, 0, 'None' ] ,
         'b12' : [ '12' , 1.1338, 1, 0, 'None' ] ,
         'c12' : [ '20' , 0.921, 0.553, 0, 'None' ] ,
         's12' : [ '12' , 1.1235, 0.68, 0, 'Left' ] ,
         'dt4' : [  '4' , 2 / 3, 0, 1, 'None' ] ,
         'dr4' : [  '4' , 1, 1, 1, 'None' ] ,
         'dt6' : [  '6' , 2 / 3, 0, 1, 'None' ] ,
         'dt8' : [  '8' , 2 / 3, 0, 1, 'None' ] ,
         'db6' : [  '6' , 1.0938, 1, 1, 'None' ] ,
         'dc6' : [  '6' , 1.0572, 0.585786, 1, 'None' ] ,
         'ds6' : [  '6' , 1.0875, 0.704, 1, 'Left' ] ,
        'dr12' : [ '12' , 1, 0, 1, 'None' ] ,
        'dt12' : [ '12' , 2 / 3, 0, 1, 'None' ] ,
        'dt20' : [ '20' , 2 / 3, 0, 1, 'None' ] ,
        'db12' : [ '12' , 1.1338, 1, 1, 'None' ] ,
        'dc12' : [ '20' , 0.921, 0.553, 1, 'None' ] ,
        'ds12' : [ '12' , 1.1235, 0.68, 1, 'Left' ]
    }

    sizenames = [
        'Midradius' ,
        'Inradius' ,
        'Circumradius' ,
        'LongEdge' ,
        'ShortEdge'
    ]


    def __init__ (
        self ,
        object ,
        midradius = 5
    ):

        def property ( name , type , description ):
            return object.addProperty(
                f'App::Property{ type }',
                name , 'RegularSolid' ,
                description
            )


        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Radius of inscribed sphere touching closest edge') ,
            name = 'Midradius' ,
            type = 'Length'
        ).Midradius = midradius


        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Radius of inscribed sphere touching closest face') ,
            name = 'Inradius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Radius of inscribed sphere touching furthest vertex') ,
            name = 'Circumradius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Length of longest edge') ,
            name = 'LongEdge' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Length of shortest edge') ,
            name = 'ShortEdge' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'What drives solid size when changing construction') ,
            name = 'KeepSize' ,
            type = 'Enumeration'
        )

        object.KeepSize = self.sizenames
        object.KeepSize = self.sizenames[0]

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Initiating body') ,
            name = 'Source' ,
            type = 'Enumeration'
        )

        object.Source = [ e[1] for e in self.enums['Source'] ]
        object.Source = [ e[1] for e in self.enums['Source'] if len(e) >= 4 and e[3] ][0]

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Amount of vertex truncation/elongation') ,
            name = 'Vtrunc' ,
            type = 'Float'
        ).Vtrunc = 0.0

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Amount of edge truncation') ,
            name = 'Etrunc' ,
            type = 'Float'
        ).Etrunc = 0.0

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Create the snub version') ,
            name = 'Snub' ,
            type = 'Enumeration'
        )

        object.Snub = [e[1] for e in self.enums['Snub']]
        object.Snub = [e[1] for e in self.enums['Snub'] if len(e) >= 4 and e[3]][0]

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Create the dual of the current solid') ,
            name = 'Dual' ,
            type = 'Bool'
        ).Dual = False

        property(
            description = QT_TRANSLATE_NOOP('App::Property', 'Preset parameters for some hard names') ,
            name = 'Presets' ,
            type = 'Enumeration'
        )

        object.Presets = [ e[1] for e in self.enums['Presets'] ]
        object.Presets = [ e[1] for e in self.enums['Presets'] if len(e) >= 4 and e[3]][0]

        object.Proxy = self

        # We could implement onChanged(self,opj,prop) to handle property value changes, but its easier to keep property previous values around

        self.prevcode = None
        self.prevsizes = ( None , None , None , None , None )


    # We do not want to clutter our serialisation with previous property value state.
    # Also, self.prevsizes contains Quantity objects which don't JSON-serialise

    def __getstate__ ( self ):
        return None

    def __setstate__ ( self , state ):
        self.prevsizes = ( None , None , None , None , None )
        self.prevcode = None

    def execute ( self , object ):

        sizes = (
            object.Midradius ,
            object.Inradius ,
            object.Circumradius ,
            object.LongEdge ,
            object.ShortEdge
        )

        keepsize = object.KeepSize

        for i in range(len(sizes)):
            if sizes[ i ] != self.prevsizes[ i ] and self.prevsizes[ i ] != None:
                keepsize = self.sizenames[ i ]
                break

        presetcode = [ e[ 0 ] for e in self.enums[ 'Presets' ] if e[ 1 ] == object.Presets ][ 0 ]

        # The user has selected a new preset

        if presetcode != '0' and presetcode != self.prevcode:

                source , vtrunc , etrunc , dual , snub = self.p[ presetcode ]

                object.Source = [e[1] for e in self.enums['Source'] if e[0]==source][0]
                object.Vtrunc,object.Etrunc,object.Dual = vtrunc,etrunc,dual
                object.Snub = [e[1] for e in self.enums['Snub'] if e[0]==snub][0]

        else:

            # The preset is as it was, or it was set to 'Custom'. Check if the user has changed a parameter affecting the preset

            source = [ e[0] for e in self.enums['Source'] if e[1] == object.Source ][0]

            vtrunc , etrunc , dual = object.Vtrunc , object.Etrunc , object.Dual

            snub = [ e[0] for e in self.enums['Snub'] if e[1] == object.Snub ][0]

            if presetcode != '0' and self.p[presetcode] != ( source , vtrunc , etrunc , dual , snub ):
                presetcode = '0' if (presetcode[0]=='d')==dual else 'd'+presetcode if dual else presetcode[1:]
                object.Presets = [e[1] for e in self.enums['Presets'] if e[0]==presetcode][0]

        self.prevcode = presetcode

        bpy_verts , bpy_faces = createSolid(source,vtrunc,etrunc,dual,snub)

        faces = []

        for face in bpy_faces:
            verts = [ bpy_verts[ vi ] for vi in face ] + [ bpy_verts[ face[0] ] ]
            polygon = Part.makePolygon(verts)
            faces.append(Part.Face(polygon))

        v0 = Vector(0,0,0)
        s0 = Part.Point(v0).toShape()

        origsizes = (
            min(e.distToShape(s0)[0] for f in faces for e in f.Edges), # Midradius
            min(f.distToShape(s0)[0] for f in faces), # Inradius
            max(v.distToShape(s0)[0] for f in faces for v in f.Vertexes), # Circumradius
            max(e.Length for f in faces for e in f.Edges), # LongEdge
            min(e.Length for f in faces for e in f.Edges) # ShortEdge
        )

        for i in range(len(self.sizenames)):
            if keepsize == self.sizenames[i]:
                scale = sizes[i] / origsizes[i]
                break

        object.Midradius , \
        object.Inradius , \
        object.Circumradius , \
        object.LongEdge , \
        object.ShortEdge = \
        self.prevsizes = \
        tuple( os * scale for os in origsizes )

        shell = Part.makeShell(faces).scaled(scale,v0)
        solid = Part.makeSolid(shell)

        object.Shape = solid
