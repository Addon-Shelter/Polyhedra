

import FreeCADGui
import FreeCAD
import Part
import math
import os

from ..Utils.ViewProviderBox import ViewProviderBox
from ..Utils.Resources import icon
from ..Utils.Vertexes import horizontal_regular_polygon_vertexes
from ..Utils.Geodesic import geodesic_radius2side

from FreeCAD import Base


QT_TRANSLATE_NOOP = FreeCAD.Qt.QT_TRANSLATE_NOOP


class Geodesic_sphere:

    radiusvalue = 0
    divided_by = 2


    def __init__(self, obj, radius=5, div=2):
        obj.addProperty(
            "App::PropertyLength",
            "Radius",
            "Geodesic",
            QT_TRANSLATE_NOOP("App::Property", "Radius of the sphere"),
        ).Radius = radius
        obj.addProperty(
            "App::PropertyLength",
            "Side",
            "Geodesic",
            QT_TRANSLATE_NOOP("App::Property", "Sidelength of the triangles (approximative!)"),
        )
        obj.addProperty(
            "App::PropertyInteger",
            "DividedBy",
            "Geodesic",
            QT_TRANSLATE_NOOP(
                "Properties tooltips",
                "The sides of the basic polyhedron are divided in ... (value 1 to 10)",
            ),
        ).DividedBy = div

        obj.Proxy = self


    def geodesic_divide_triangles(self,vertex1, vertex2, vertex3, faces):

        vector1 = (Base.Vector(vertex2) - Base.Vector(vertex1)) / self.divided_by
        vector2 = (Base.Vector(vertex3) - Base.Vector(vertex2)) / self.divided_by

        icosaPt={}


        icosaPt[str(1)] = Base.Vector(vertex1)

        for level in range(self.divided_by):
            l1 = level + 1
            icosaPt[str(l1*10+1)] = icosaPt[str(1)]+ vector1 * (l1)

            for pt in range(level+1):
                icosaPt[str(l1*10+2+pt)] = icosaPt[str(l1*10+1)] + vector2 *(pt+1)


        for level in range(self.divided_by):

            for point in range(level+1):
                vertex1x = icosaPt[str(level*10+1+point)].normalize().multiply(self.radiusvalue)
                vertex2x = icosaPt[str(level*10+11+point)].normalize().multiply(self.radiusvalue)
                vertex3x = icosaPt[str(level*10+12+point)].normalize().multiply(self.radiusvalue)
                polygon = Part.makePolygon([vertex1x,vertex2x,vertex3x, vertex1x])
                faces.append(Part.Face(polygon))

            for point in range(level):
                vertex1x = icosaPt[str(level*10+1+point)].normalize().multiply(self.radiusvalue)
                vertex2x = icosaPt[str(level*10+2+point)].normalize().multiply(self.radiusvalue)
                vertex3x = icosaPt[str(level*10+12+point)].normalize().multiply(self.radiusvalue)
                polygon = Part.makePolygon([vertex1x,vertex2x,vertex3x, vertex1x])
                faces.append(Part.Face(polygon))

        return faces



    def execute (self,obj):

        obj.DividedBy = int(round(obj.DividedBy))
        if obj.DividedBy <= 0:
            obj.DividedBy = 1
        if obj.DividedBy > 10:
            obj.DividedBy = 10


        radius = float(obj.Radius)
        if radius != self.radiusvalue or obj.DividedBy != self.divided_by:
            self.divided_by = obj.DividedBy
            obj.Side = geodesic_radius2side(radius, self.divided_by)
            self.radiusvalue = radius
        else:
            self.radiusvalue = geodesic_side2radius(obj.Side,self.divided_by)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue

        self.divided_by = obj.DividedBy

        z = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
        anglefaces = 138.189685104
        r = z/12 * math.sqrt(3) * (3 + math.sqrt(5))


        #radius of a pentagram with the same side
        radius2 = z / math.sin(36 * math.pi/180)/2

        #height of radius2 in the sphere
        angle = math.acos(radius2/radius)
        height = radius * math.sin(angle)

        faces = []

        vertex_bottom = (0,0,-radius)
        vertexes_low = horizontal_regular_polygon_vertexes(5,radius2, -height)
        vertexes_high = horizontal_regular_polygon_vertexes(5,radius2, height, math.pi/5)
        vertex_top = (0,0,radius)

        for i in range(5):
            faces = self.geodesic_divide_triangles(vertex_bottom,vertexes_low[i+1],vertexes_low[i],faces)


        for i in range(5):
            faces = self.geodesic_divide_triangles(vertexes_high[i],vertexes_low[i+1],vertexes_low[i],faces)
            faces = self.geodesic_divide_triangles(vertexes_low[i+1],vertexes_high[i+1],vertexes_high[i],faces)

        for i in range(5):
            faces = self.geodesic_divide_triangles(vertex_top,vertexes_high[i],vertexes_high[i+1],faces)


        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid


class GeodesicSphereCommand:
    def GetResources(self):
        return {
            "Pixmap": icon('Shapes/Geodesic-Sphere') ,
            "Accel": "Shift+G",
            "MenuText": QT_TRANSLATE_NOOP("Geodesic_sphere", "Geodesic sphere"),
            "ToolTip": QT_TRANSLATE_NOOP("Geodesic_sphere", "Generate Geodesic Spheres"),
        }

    def Activated(self):
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "GeodesicSphere")
        Geodesic_sphere(obj)
        #obj.ViewObject.Proxy=0
        ViewProviderBox(obj.ViewObject, "Geodesic-sphere")
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        return


    def IsActive(self):
        if FreeCAD.ActiveDocument == None:
               return False
        else:
               return True

