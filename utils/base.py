import math
from typing import Union
from typing import Tuple
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

        if a * v + b * w == 0:
            return None

        t = (-a * lineray.point1.x - b * lineray.point1.y - c) / (a * v + b * w)

        if t > 0:
            x = lineray.point1.x + v * t
            y = lineray.point1.y + w * t

            d1 = MathUtils.distance_point_to_point(Point(x,y), line.point1)
            d2 = MathUtils.distance_point_to_point(Point(x,y), line.point2)
            d3 = line.get_len()
            if abs(d1 + d2 - d3) > 0.01:
                return None

            return Point(x, y)

        return None 


    def _rc_to_circle(self) -> Union[Point, None]:
        radius = self.object.radius
        dist_line_to_center = MathUtils.distance_point_to_line(self.object.position,
                                                                MathUtils.ray_to_line(self.ray))

        if dist_line_to_center < radius:
            pass

        return None



class CoordinateSystemRotation:

    def __init__(self, ang: float) -> None:
        self.ang = ang

    def get_transformed_line(self, line: Line) -> Line:        
        return Line(
            self.get_transformed_point(line.point1),
            self.get_transformed_point(line.point2),
        )

    def get_starting_line(self, line: Line) -> Line:
        return Line(
            self.get_starting_point(line.point1),
            self.get_starting_point(line.point2),
        )

    def get_transformed_point(self, point: Point) -> Point:
        """
        x' = x * cos(a) + y * sin(a)
        y' = y * cos(a) - x * sin(a)
        """

        transformed_point = Point(
            x = point.x * math.cos(self.ang) + point.y * math.sin(self.ang),
            y = point.y * math.cos(self.ang) - point.x * math.sin(self.ang)
        )
        return transformed_point

    def get_starting_point(self, point: Point) -> Point:
        """
        x = x' * cos(a) - y' * sin(a)
        y = x' * sin(a) + y' * cos(a)
        """

        transformed_point = Point(
            x = point.x * math.cos(self.ang) - point.y * math.sin(self.ang),
            y = point.x * math.sin(self.ang) + point.y * math.cos(self.ang)
        )
        return transformed_point
        



class MathUtils:

    @staticmethod
    def line_coefficients(line: Line) -> Tuple[float, float, float]:
        a = line.point2.y - line.point1.y
        b = line.point1.x - line.point2.x
        c = -line.point1.x  * line.point2.y + line.point1.y * line.point2.x
        return (a, b, c)

    @staticmethod
    def distance_point_to_line(point: Point, line: Line, linesegment = True) -> float:
        a,b,c = MathUtils.line_coefficients(line)
        dist = abs(a*point.x + b*point.y + c) / math.sqrt(a**2 + b**2)

        if linesegment:
            line_ang = line.get_ang()
            rotateManager = CoordinateSystemRotation(line_ang)

            line_r = rotateManager.get_transformed_line(line)
            point_r = rotateManager.get_transformed_point(point)

            dist_point1 = MathUtils.distance_point_to_point(point, line.point1)
            dist_point2 = MathUtils.distance_point_to_point(point, line.point2)

            max_x = max(line_r.point1.x, line_r.point2.x)
            min_x = min(line_r.point1.x, line_r.point2.x)

            if point_r.x > max_x or point_r.x < min_x:
                return min(dist_point1, dist_point2)

        return dist

    @staticmethod
    def distance_point_to_point(point1: Point, point2: Point) -> float:
        return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)

    @staticmethod
    def distance_line_to_line(line1: Line, line2: Line) -> float:

            ## Вводим параметры отрезков
            xa, ya, xb, yb = line1.point1.x, line1.point1.y, line1.point2.x, line1.point2.y
            xc, yc, xd, yd = line2.point1.x, line2.point1.y, line2.point2.x, line2.point2.y

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
                dl1 = MathUtils.distance_point_to_line(Point(xc,yc), Line(Point(xa,ya), Point(xb,yb)))
                min = dl1
            dl2 = MathUtils.distance_point_to_line(Point(xd,yd), Line(Point(xa,ya), Point(xb,yb)))

            if ( dl2<min and dl2!=-1 ) or min==-1 :
                min=dl2
            dl3 = MathUtils.distance_point_to_line(Point(xa,ya), Line(Point(xc,yc), Point(xd,yd)))
            if ( dl3<min and dl3!=-1 ) or min==-1 :
                min=dl3
            dl4=MathUtils.distance_point_to_line(Point(xb,yb), Line(Point(xc,yc), Point(xd,yd)))
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

            return min

    @staticmethod
    def ray_to_line(ray: Ray) -> Line: 
        line = Line(Point(ray.point.x, ray.point.y),
                        Point(ray.vector.x+ray.point.x, ray.vector.y+ray.point.y))
        return line


