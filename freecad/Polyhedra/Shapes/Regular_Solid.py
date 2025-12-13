# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Polyhedra addon.

from ..Utils.Other import createSolid
from ..Utils.Plato import PlatoType

from FreeCAD import DocumentObject , Vector , Units , Qt
from typing import Any
from Part import makePolygon , makeSolid , makeShell , Point , Face


QT_TRANSLATE_NOOP = Qt.QT_TRANSLATE_NOOP

Sources : list[ tuple[ PlatoType , str , str ] ] = [
    (  '4' , 'Tetrahedron'  , '' ) ,
    (  '6' , 'Hexahedron'   , '' ) ,
    (  '8' , 'Octahedron'   , '' ) ,
    ( '12' , 'Dodecahedron' , '' ) ,
    ( '20' , 'Icosahedron'  , '' )
]

Snubs = (
    (  'None' , 'No Snub'    , '' ) ,
    (  'Left' , 'Left Snub'  , '' ) ,
    ( 'Right' , 'Right Snub' , '' )
)

Presets = [
    (    '0' , 'Custom','' ),
    (   't4' , 'Truncated Tetrahedron','' ),
    (   'r4' , 'Cuboctahedron','' ),
    (   't6' , 'Truncated Cube','' ),
    (   't8' , 'Truncated Octahedron','' ),
    (   'b6' , 'Rhombicuboctahedron','' ),
    (   'c6' , 'Truncated Cuboctahedron',''),
    (   's6' , 'Snub Cube','' ),
    (  'r12' , 'Icosidodecahedron','' ),
    (  't12' , 'Truncated Dodecahedron','' ),
    (  't20' , 'Truncated Icosahedron','' ),
    (  'b12' , 'Rhombicosidodecahedron','' ),
    (  'c12' , 'Truncated Icosidodecahedron','' ),
    (  's12' , 'Snub Dodecahedron','' ),
    (  'dt4' , 'Triakis Tetrahedron','' ),
    (  'dr4' , 'Rhombic Dodecahedron','' ),
    (  'dt6' , 'Triakis Octahedron','' ),
    (  'dt8' , 'Tetrakis Hexahedron','' ),
    (  'db6' , 'Deltoidal Icositetrahedron','' ),
    (  'dc6' , 'Disdyakis Dodecahedron','' ),
    (  'ds6' , 'Pentagonal Icositetrahedron','' ),
    ( 'dr12' , 'Rhombic Triacontahedron','' ),
    ( 'dt12' , 'Triakis Icosahedron','' ),
    ( 'dt20' , 'Pentakis Dodecahedron','' ),
    ( 'db12' , 'Deltoidal Hexecontahedron','' ),
    ( 'dc12' , 'Disdyakis Triacontahedron','' ),
    ( 'ds12' , 'Pentagonal Hexecontahedron','' )
]


Size_Names = [
    'Midradius' ,
    'Inradius' ,
    'Circumradius' ,
    'LongEdge' ,
    'ShortEdge'
]

# actual preset values (Source, Vtrunc, Etrunc, Dual, Snub)

Preset_Values : dict[ str , tuple[ PlatoType , float , float , bool , str ] ] = {
      't4' : (  '4' , 2 / 3, 0, False , 'None' ) ,
      'r4' : (  '4' , 1, 1, False , 'None' ) ,
      't6' : (  '6' , 2 / 3, 0, False , 'None' ) ,
      't8' : (  '8' , 2 / 3, 0, False , 'None' ) ,
      'b6' : (  '6' , 1.0938, 1, False , 'None' ) ,
      'c6' : (  '6' , 1.0572, 0.585786, False , 'None' ) ,
      's6' : (  '6' , 1.0875, 0.704, False , 'Left' ) ,
     'r12' : ( '12' , 1, 0, False , 'None' ) ,
     't12' : ( '12' , 2 / 3, 0, False , 'None' ) ,
     't20' : ( '20' , 2 / 3, 0, False , 'None' ) ,
     'b12' : ( '12' , 1.1338, 1, False , 'None' ) ,
     'c12' : ( '20' , 0.921, 0.553, False , 'None' ) ,
     's12' : ( '12' , 1.1235, 0.68, False , 'Left' ) ,
     'dt4' : (  '4' , 2 / 3, 0, True , 'None' ) ,
     'dr4' : (  '4' , 1, 1, True , 'None' ) ,
     'dt6' : (  '6' , 2 / 3, 0, True , 'None' ) ,
     'dt8' : (  '8' , 2 / 3, 0, True , 'None' ) ,
     'db6' : (  '6' , 1.0938, 1, True , 'None' ) ,
     'dc6' : (  '6' , 1.0572, 0.585786, True , 'None' ) ,
     'ds6' : (  '6' , 1.0875, 0.704, True , 'Left' ) ,
    'dr12' : ( '12' , 1, 0, True , 'None' ) ,
    'dt12' : ( '12' , 2 / 3, 0, True , 'None' ) ,
    'dt20' : ( '20' , 2 / 3, 0, True , 'None' ) ,
    'db12' : ( '12' , 1.1338, 1, True , 'None' ) ,
    'dc12' : ( '20' , 0.921, 0.553, True , 'None' ) ,
    'ds12' : ( '12' , 1.1235, 0.68, True , 'Left' )
}


class RegularSolidPart ( DocumentObject ):

    Circumradius : Units.Quantity
    Midradius : Units.Quantity
    Inradius : Units.Quantity
    LongEdge : Units.Quantity
    ShortEdge : Units.Quantity

    KeepSize : list[ str ] | str
    Presets : list[ str ] | str
    Source : list[ str ] | str
    Snub : list[ str ] | str

    Vtrunc : float
    Etrunc : float

    Shape : Any
    Dual : bool


# The following two classes 'RegularSolid' and 'RegularSolidCommand' make the abilities of the 'createSolid' function above
# available to FreeCAD. They also borrow somewhat on the add_mesh_solid.py referenced above:

class Regular_Solid:

    __module__ = 'Virtual.Polyhedra.Parts'
    __name__ = 'Regular_Solid'


    def __init__ (
        self ,
        object : RegularSolidPart ,
        midradius = 5
    ):

        self.defineProperties(object)

        #   Selectable Values

        object.Presets = [ preset[1] for preset in Presets ]
        object.Source = [ source[1] for source in Sources ]
        object.Snub = [ snub[1] for snub in Snubs ]

        #   Default Value

        object.Presets = Presets[ 6 ][ 1 ]
        object.Source = Sources[ 2 ][ 1 ]
        object.Snub = Snubs[ 0 ][ 1 ]

        object.KeepSize = Size_Names
        object.KeepSize = Size_Names[0]

        object.Midradius.Value = midradius
        object.Vtrunc = 0.0
        object.Etrunc = 0.0
        object.Dual = False

        object.Proxy = self

        # We could implement onChanged(self,opj,prop) to handle property value changes, but its easier to keep property previous values around

        self.prevcode = None
        self.prevsizes = ( None , None , None , None , None )


    # We do not want to clutter our serialization with previous property value state.
    # Also, self.prevsizes contains Quantity objects which don't JSON-serialize

    def __getstate__ ( self ):
        return None

    def __setstate__ ( self , state ):
        self.prevsizes = ( None , None , None , None , None )
        self.prevcode = None

    def execute ( self , object : RegularSolidPart ):

        sizes = (
            object.Midradius ,
            object.Inradius ,
            object.Circumradius ,
            object.LongEdge ,
            object.ShortEdge
        )

        retain_size = object.KeepSize

        for i in range( len(sizes) ):
            if sizes[ i ] != self.prevsizes[ i ] and self.prevsizes[ i ] != None:
                retain_size = Size_Names[ i ]
                break

        code = [ preset[ 0 ] for preset in Presets if preset[ 1 ] == object.Presets ][ 0 ]

        # The user has selected a new preset

        if code == '0' or code == self.prevcode :

            # The preset is as it was, or it was set to 'Custom'.
            # Check if the user has changed a parameter affecting the preset

            plato = [ source for source in Sources if source[1] == object.Source ][0][0]

            vtrunc = object.Vtrunc
            etrunc = object.Etrunc
            dual = object.Dual

            snub = [ snub[0] for snub in Snubs if snub[1] == object.Snub ][0]

            current = ( plato , vtrunc , etrunc , dual , snub )

            if code != '0' and Preset_Values[ code ] != current :

                code = '0' if( code[0] == 'd' ) == dual else 'd' + code if dual else code[1:]

                object.Presets = [ preset[1] for preset in Presets if preset[0] == code ][0]

        else :

            plato , vtrunc , etrunc , dual , snub = Preset_Values[ code ]

            object.Source = [ source[1] for source in Sources if source[0] == plato ][0]

            object.Vtrunc = vtrunc
            object.Etrunc = etrunc
            object.Dual = dual

            object.Snub = [ s[1] for s in Snubs if s[0] == snub ][0]


        self.prevcode = code

        faces = []

        solid_vertices , solid_faces = createSolid(plato,vtrunc,etrunc,dual,snub)

        for face in solid_faces:
            vertices = [ solid_vertices[ index ] for index in face ] + [ solid_vertices[ face[0] ] ]
            polygon = makePolygon(vertices)
            faces.append(Face(polygon))

        v0 = Vector( 0 , 0 , 0 )
        s0 = Point(v0).toShape()

        orig_sizes = (
            min( edge.distToShape(s0)[0] for face in faces for edge in face.Edges ) , # Midradius
            min( face.distToShape(s0)[0] for face in faces ) , # Inradius
            max( vertex.distToShape(s0)[0] for face in faces for vertex in face.Vertexes ) , # Circumradius
            max( edge.Length for face in faces for edge in face.Edges ) , # LongEdge
            min( edge.Length for face in faces for edge in face.Edges ) # ShortEdge
        )

        scale = 1.0

        for i in range( len(Size_Names) ) :
            if retain_size == Size_Names[ i ]:
                scale = sizes[ i ] / orig_sizes[ i ]
                break

        self.prevsizes = tuple( size * scale for size in orig_sizes )

        object.Midradius , \
        object.Inradius , \
        object.Circumradius , \
        object.LongEdge , \
        object.ShortEdge = self.prevsizes

        shell = makeShell(faces).scaled(scale,v0)
        solid = makeSolid(shell)

        object.Shape = solid


    def defineProperties (
        self ,
        object : RegularSolidPart
    ):

        def property ( name , type , description ):
            object.addProperty(
                f'App::Property{ type }',
                name , 'RegularSolid' ,
                description
            )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of inscribed sphere touching closest edge') ,
            name = 'Midradius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of inscribed sphere touching closest face') ,
            name = 'Inradius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Radius of inscribed sphere touching furthest vertex') ,
            name = 'Circumradius' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Length of longest edge') ,
            name = 'LongEdge' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Length of shortest edge') ,
            name = 'ShortEdge' ,
            type = 'Length'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','What drives solid size when changing construction') ,
            name = 'KeepSize' ,
            type = 'Enumeration'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Initiating body') ,
            name = 'Source' ,
            type = 'Enumeration'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Amount of vertex truncation/elongation') ,
            name = 'Vtrunc' ,
            type = 'Float'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Amount of edge truncation') ,
            name = 'Etrunc' ,
            type = 'Float'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Create the snub version') ,
            name = 'Snub' ,
            type = 'Enumeration'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Create the dual of the current solid') ,
            name = 'Dual' ,
            type = 'Bool'
        )

        property(
            description = QT_TRANSLATE_NOOP('App::Property','Preset parameters for some hard names') ,
            name = 'Presets' ,
            type = 'Enumeration'
        )