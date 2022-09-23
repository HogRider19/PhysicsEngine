import math
from typing import Union
from MathОperators.point import Point
from MathОperators.line import Line
from MathОperators.ray import Ray
from MathОperators.vector import Vector
from Objects.circle import Circle


class RayCast:

    def __init__(self, ray: Ray, object: Union[Line, Circle]) -> None:
        self.ray = ray
        self.object = object

    def get_cross_point(self) -> Union[Point, None]:
        #Вернуть точку пересечения или False
        cross_point = None

        if isinstance(self.object, Line):
            cross_point = self._rc_to_line()
        elif isinstance(self.object, Circle):
            cross_point = self._rc_to_circle()

        return cross_point

    def _rc_to_line(self) -> Union[Point, None]:
        line = self.object
        lineray = MathUtils.ray_to_line(self.ray)

        v = lineray.point2.x - lineray.point1.x
        w = lineray.point2.y - lineray.point1.y

        a,b,c = MathUtils.line_coefficients(line)

        t = (-a * lineray.point1.x - b * lineray.point1.y - c) / (a * v + b * w)

        if t > 0:
            x = lineray.point1.x + v * t
            y = lineray.point1.y + w * t

            return Point(x, y)

        return None 


    def _rc_to_circle(self) -> Union[Point, None]:
        radius = self.object.radius
        dist_line_to_center = MathUtils.distance_point_to_line(self.object.position,
                                                                MathUtils.ray_to_line(self.ray))

        if dist_line_to_center < radius:
            pass

        return None



class MathUtils:

    @staticmethod
    def line_coefficients(line: Line) -> float:
        a = line.point2.y - line.point1.y
        b = line.point1.x - line.point2.x
        c = -line.point1.x  * line.point2.y + line.point1.y * line.point2.x
        return a, b, c

    @staticmethod
    def distance_point_to_line(point: Point, line: Line, linesegment = True) -> float:
        a,b,c = MathUtils.line_coefficients(line)
        dist = abs(a*point.x + b*point.y + c) / math.sqrt(a**2 + b**2)

        if linesegment:
            dist_point1 = MathUtils.distance_point_to_point(point, line.point1)
            dist_point2 = MathUtils.distance_point_to_point(point, line.point2)

            return min([dist_point1, dist_point2, dist])

        return dist

    @staticmethod
    def distance_point_to_point(point1: Point, point2: Point) -> float:
        return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)

    @staticmethod
    def distance_line_to_line(line1: Line, line2: Line) -> float:
        """
            #!/usr/bin/env python3
            # -*- coding: utf-8 -*- 

            import math

            def ras (x1, y1, x2, y2, x3, y3):
            ## Если отрезок вертикальный - меняем местами координаты каждой точки.
            if x1==x2:
                x1, y1 = y1, x1
                x2, y2 = y2, x2
                x3, y3 = y3, x3
            k=(y1-y2)/(x1-x2) ## Ищем коэффициенты уравнения прямой, которому принадлежит данный отрезок.
            d=y1-k*x1
            xz=(x3*x2-x3*x1+y2*y3-y1*y3+y1*d-y2*d)/(k*y2-k*y1+x2-x1)
            dl=-1
            if ( xz<=x2 and xz>=x1 ) or ( xz<=x1 and xz>=x2 ):
                dl=math.sqrt((x3-xz)*(x3-xz)+(y3-xz*k-d)*(y3-xz*k-d)) ## Проверим лежит ли основание высоты на отрезке.
            return dl


            ## Вводим параметры отрезков
            # xa, ya, xb, yb = [1, 1, 2, 2]
            # xc, yc, xd, yd = [2, 1, 3, 0]

            xa, ya, xb, yb = [int(s) for s in input().split()]
            xc, yc, xd, yd = [int(s) for s in input().split()]

            min=-1
            t=-2
            s=-2

            o=(xb-xa)*(-yd+yc)-(yb-ya)*(-xd+xc)
            o1=(xb-xa)*(yc-ya)-(yb-ya)*(xc-xa)
            o2=(-yd+yc)*(xc-xa)-(-xd+xc)*(yc-ya)

            if o!=0:
            t=o1/o
            s=o2/o

            if (t>=0 and s>=0) and (t<=1 and s<=1):
            min=0 ## Проверим пересекаются ли отрезки.
            else: 
            ## Найдём наименьшую высоту опущенную из конца одного отрезка на другой.
            dl1=ras(xa,ya,xb,yb,xc,yc)
            min=dl1
            dl2=ras(xa,ya,xb,yb,xd,yd)
            if ( dl2<min and dl2!=-1 ) or min==-1 :
                min=dl2
            dl3=ras(xc,yc,xd,yd,xa,ya)
            if ( dl3<min and dl3!=-1 ) or min==-1 :
                min=dl3
            dl4=ras(xc,yc,xd,yd,xb,yb)
            if ( dl4<min and dl4!=-1) or min==-1 :
                min=dl4
            if min==-1 :
                ## В случае, если невозможно опустить высоту найдём минимальное расстояние между точками.
                dl1=math.sqrt((xa-xc)*(xa-xc)+(ya-yc)*(ya-yc))
                min=dl1
                dl2=math.sqrt((xb-xd)*(xb-xd)+(yb-yd)*(yb-yd))
                if dl2<min :
                min=dl2
                dl3=math.sqrt((xb-xc)*(xb-xc)+(yb-yc)*(yb-yc))
                if dl3<min :
                min=dl3
                dl4=math.sqrt((xa-xd)*(xa-xd)+(ya-yd)*(ya-yd))
                if dl4<min :
                min=dl4

            print (min)
        """

    @staticmethod
    def ray_to_line(ray: Ray) -> Line: 
        line = Line(Point(ray.point.x, ray.point.y),
                        Point(ray.vector.x+ray.point.x, ray.vector.y+ray.point.y))
        return line


