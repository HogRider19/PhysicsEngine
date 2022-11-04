import math
from typing import Union
from MathОperators.line import Line
from MathОperators.point import Point
from MathОperators.ray import Ray
from MathОperators.vector import Vector
from Objects.circle import Circle
from Objects.rect import Rect
from utils.base import MathUtils, RayCast
from utils.base import CoordinateSystemRotation


class DistanceBetweenObjects:

    def __init__(self, object1: Union[Rect, Circle], object2: Union[Rect, Circle]) -> None:
        self.object1 = object1
        self.object2 = object2

    def get_distance(self) -> float:
        dist = None

        if isinstance(self.object1, Circle) and  isinstance(self.object2, Circle):
            dist = self._dist_circle_circle()

        elif isinstance(self.object1, Rect) and  isinstance(self.object2, Rect):
            dist = self._dist_rect_rect()

        elif (isinstance(self.object1, Circle) and
                    isinstance(self.object2, Rect)) or (isinstance(self.object2, Circle) and
                        isinstance(self.object1, Rect)):

            if not isinstance(self.object1, Circle):
                # Меняем объксты местами если первый не Circle
                self.object1, self.object2 = self.object2, self.object1

            dist = self._dist_circle_rect()
        
        else:
            raise "Invalid object"

        return dist

    def _dist_circle_circle(self) -> float: 
        radius1 = self.object1.radius
        radius2 = self.object2.radius
        dist = MathUtils.distance_point_to_point(
                self.object1.position, self.object2.position) - (radius1 + radius2)
        dist = 0 if dist < 0 else dist
        return dist

    def _dist_circle_rect(self) -> float: 
        circle = self.object1
        rect = self.object2
        
        dists = []
        for line in rect.get_component_lines():
            dist = MathUtils.distance_point_to_line(circle.position,
                                                     line) - circle.radius
            dist = 0 if dist < 0 else dist
            dists.append(dist)

        return min(dists)

    def _dist_rect_rect(self) -> float: 
        dists = []
        for line1 in self.object1.get_component_lines():
            for line2 in self.object2.get_component_lines():
                dist = MathUtils.distance_line_to_line(line1, line2)
                dist = 0 if dist < 0 else dist
                dists.append(dist)
        
        return min(dists)



class CollisionPoint:
    
    def __init__(self, object1: Union[Rect, Circle], object2: Union[Rect, Circle]) -> None:
        self.object1 = object1
        self.object2 = object2
        self._info = {}

    def calculate(self) -> None:

        if isinstance(self.object1, Circle) and  isinstance(self.object2, Circle):
            local_info = self._cross_circle_circle()

        elif isinstance(self.object1, Rect) and  isinstance(self.object2, Rect):
            local_info = self._cross_rect_rect()

        elif (isinstance(self.object1, Circle) and
                    isinstance(self.object2, Rect)) or (isinstance(self.object2, Circle) and
                        isinstance(self.object1, Rect)):

            if not isinstance(self.object1, Circle):
                # Меняем объксты местами если первый не Circle
                self.object1, self.object2 = self.object2, self.object1

            local_info = self._cross_circle_rect()
        
        else:
            raise ValueError("Invalid object")

        self._info = local_info

    def get_info(self) -> dict:
        """
        Словарь _info заполняется после 
        расчета точки соударения
        """
        return self._info

    def get_cross_point(self, update: bool=True) -> Point:
        
        if update:
            self.calculate()

        return self._info.get('cross_point')

    def _cross_circle_circle(self) -> Point:
        vector12 = Vector(self.object2.position.x - self.object1.position.x,
                             self.object2.position.y  - self.object1.position.y)

        if vector12.get_len() <= self.object1.radius + self.object2.radius:

            inrerior_vector = vector12.clone()
            force_vector = vector12.clone()
            force_vector.normalize()
            vector12.normalize()
            vector12.mult(self.object1.radius)
            cross_point = self.object1.position.displace_new_point(vector12)

            r_len = self.object1.radius + self.object2.radius
            local_info = {
                'type': 'cc',
                'cross_point': cross_point,
                'force_vector': force_vector,
                'inrerior_dist': 1 - (inrerior_vector.get_len()/r_len),
            }
            return local_info

        return {}

    def _cross_circle_rect(self, def_circle=None, def_rect=None) -> Union[Point, None]: 
        """
        1) Получаем точки rect
        2) Поворот системы координат
        3) a = arctg(dy/dx)
        4) a1 = arctg(h/w)
        5) lineNum = 
                3: -a1 < a < a1
                4: a1 < a < pi - a1
                1: pi - a1 < a < pi + a1
                2: pi+a1 < a < 2pi - a1
        6) d = sqrt(dx**2 + dy**2)
        7) d' = dist(Ld and lineNum)
        8) if d <= d':
            return Ld U lineNum
            else:
                None
        """
        rect = self.object2
        circle = self.object1
        if def_circle and def_rect:
            circle = def_circle
            rect = def_rect

        lines = rect.get_component_lines()

        rotateManager = CoordinateSystemRotation(ang=rect.ang)

        lines_r = list(map(lambda x: rotateManager.get_transformed_line(x), lines))
        circle_pos_r = rotateManager.get_transformed_point(circle.position)
        rect_pos_r = rotateManager.get_transformed_point(rect.position)

        dx = circle_pos_r.x - rect_pos_r.x
        dy = circle_pos_r.y - rect_pos_r.y

        if dx == 0:
            dx = 0.001

        lineNum = 0

        for index, line in enumerate(lines_r):
            ray_rect_circle = Ray(rect_pos_r, Vector(dx,dy))
            p = RayCast(ray_rect_circle, line).get_cross_point()
            if p:
                lineNum = index
        
        d = math.sqrt(dx**2 + dy**2) - circle.radius
        ray_rect_circle = Ray(rect_pos_r, Vector(dx,dy))
        cross_point_r = RayCast(ray_rect_circle, lines_r[lineNum]).get_cross_point()
        d1 = MathUtils.distance_point_to_point(rect_pos_r, cross_point_r)

        if d <= d1:
            cross_point = rotateManager.get_starting_point(cross_point_r)

            collision_line = rotateManager.get_starting_line(lines_r[lineNum])
            collision_vector = Vector(collision_line.point1.x-collision_line.point2.x,
                                        collision_line.point1.y-collision_line.point2.y)
            collision_vector.rotate(math.pi/2)
            force_vector = collision_vector
            force_vector.normalize()

            local_info = {
                'type': 'cr',
                'cross_point': cross_point,
                'force_vector': force_vector,
                'inrerior_dist': 1 - (d/d1),
            }

            return local_info

        return {}


    def _cross_rect_rect(self) -> Point: 
        
        rect1 = self.object1
        rect2 = self.object2

        points1 = rect1.get_component_points()
        points2 = rect2.get_component_points()

        local_info = {
            'type': 'rr',
            'cross_point': True,
            'multiple_interaction': True,
            'multiple_interaction_list': []
        }

        circle_rad = min([rect1.width, rect1.height])/10
        for index, point in enumerate(points1):
            
            circle = Circle(circle_rad, position=point)
            
            info_once = self._cross_circle_rect(circle, rect2)

            if info_once:
                info_once['force_vector'].mult(-1)
                local_info['multiple_interaction_list'].append(info_once)
        
        if local_info['multiple_interaction_list']:
            return local_info

        return {}


    def _set_info(self, **kwargs) -> None:
        self._info.update(kwargs)



class Interaction:
    
    def __init__(self, objects = []) -> None:
        self.objects = []
        self._info = []
        for object in objects:
            self.add_object(object)

    def add_object(self, object: Union[Rect, Circle]) -> None:
        if isinstance(object, (Circle, Rect)):
            self.objects.append(object)
        else:
            raise TypeError("The object must be a Circle or Rect!")

    def get_info(self) -> dict:
        """
        Словарь _info заполняется после 
        расчета точки соударения
        """
        return self._info

    def distribute_interactions(self) -> None:
        self._info = []
        mamory_dict = {i:[] for i in range(len(self.objects))}
        for index1, object1 in enumerate(self.objects):
            for index2, object2 in enumerate(self.objects):
                if index1 != index2:
                    collisionPointManager = CollisionPoint(object1, object2)
                    colision_point = collisionPointManager.get_cross_point()

                    if colision_point and not index1 in mamory_dict.get(index2, []):

                        mamory_dict.get(index1).append(index2)
                        info = collisionPointManager.get_info()
                        self._simple_interaction(object1, object2, info)

    def _simple_interaction(self, obj1, obj2, info: dict):

        multiple_interaction = info.get('multiple_interaction', False)

        if multiple_interaction:
            multiple_interaction_list = info.get('multiple_interaction_list', [])
        else:
            multiple_interaction_list = [info]

        for interaction in multiple_interaction_list:
            force_vector = interaction.get('force_vector')
            dist = interaction.get('inrerior_dist')
            elastic = (obj1.material.elastic + obj2.material.elastic)/2 + 1
            elastic = elastic**elastic**elastic
            force_vector.mult(elastic*100*math.tan(math.pi/2*dist**elastic))

            obj2.add_relative_force(force_vector, interaction.get('cross_point'))
            force_vector.mult(-1)
            obj1.add_relative_force(force_vector, interaction.get('cross_point'))

            self._info.append(interaction)



