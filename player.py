import numpy as np
import pygame as pg
from rays import *


class Player:
    def __init__(self, x, y, map_grid):
        self.x = x
        self.y = y
        self.degree_in_radian = (2*np.pi)/360
        self.rotation = 3/2 * np.pi
        self.velocity = 1
        self.font = pg.font.SysFont('comicsans', 40, True)
        self.two_pi = 2 * np.pi
        self.map_grid = map_grid

    def rotate_left(self):
        self.rotation = (self.rotation + self.degree_in_radian) % self.two_pi

    def rotate_right(self):
        self.rotation = (self.rotation - self.degree_in_radian) % self.two_pi

    def move_forward(self):
        horizontal_ray = Ray(self.rotation, self.x, self.y, 'horizontal', self.map_grid)

        vertical_ray = Ray(self.rotation, self.x, self.y, 'vertical', self.map_grid)

        horizon_distance = np.hypot((horizontal_ray.x - self.x), (horizontal_ray.y - self.y))
        vertical_distance = np.hypot((vertical_ray.x - self.x), (vertical_ray.y - self.y))

        if min(horizon_distance, vertical_distance) >= horizontal_ray.unit_in_map // 3:
            self.x = self.x + ((np.cos(self.rotation)) * self.velocity)
            self.y = self.y - ((np.sin(self.rotation)) * self.velocity)

    def move_back(self):
        horizontal_ray = Ray((self.rotation + np.pi) % self.two_pi, self.x, self.y, 'horizontal', self.map_grid)

        vertical_ray = Ray((self.rotation + np.pi) % self.two_pi, self.x, self.y, 'vertical', self.map_grid)

        horizon_distance = np.hypot((horizontal_ray.x - self.x), (horizontal_ray.y - self.y))
        vertical_distance = np.hypot((vertical_ray.x - self.x), (vertical_ray.y - self.y))

        if min(horizon_distance, vertical_distance) >= horizontal_ray.unit_in_map // 3:
            self.x = self.x + ((np.cos(self.rotation)) * self.velocity * -1)
            self.y = self.y - ((np.sin(self.rotation)) * self.velocity * -1)

    def rays(self, surface, map_grid):
        rotation = self.rotation + 30 * self.degree_in_radian
        pg.draw.rect(surface, (50, 50, 50), pg.Rect(1000, 0, 1000, 1000))
        for i in range(120):
            if i == 0:
                rotation = rotation % self.two_pi

            horizontal_ray = Ray(rotation, self.x, self.y, 'horizontal', map_grid)

            vertical_ray = Ray(rotation, self.x, self.y, 'vertical', map_grid)

            horizon_distance = np.hypot((horizontal_ray.x - self.x),  (horizontal_ray.y - self.y))
            vertical_distance = np.hypot((vertical_ray.x - self.x), (vertical_ray.y - self.y))

            if horizon_distance <= vertical_distance:
                ray_color = (255, 0, 0)
                pg.draw.line(surface, (255, 0, 0), (self.x, self.y), (horizontal_ray.x, horizontal_ray.y), 6)
                distance = horizon_distance
            else:
                ray_color = (150, 0, 0)
                distance = vertical_distance
                pg.draw.line(surface, (0, 0, 255), (self.x, self.y), (vertical_ray.x, vertical_ray.y), 6)
            cosine_angle = abs(rotation - self.rotation)
            rotation = (rotation - (self.degree_in_radian / 2)) % self.two_pi


            if cosine_angle < 0:
                cosine_angle = self.two_pi
            elif cosine_angle > self.two_pi:
                cosine_angle -= self.two_pi
            distance = distance * np.cos(cosine_angle)

            if distance == 0:
                distance = 1
            line_height = (2**(abs(np.log2(len(map_grid)) - 9))*1000) / distance
            if line_height > 1000:
                line_height = 1000
            line_offset = 1000 + line_height/2

            pg.draw.line(surface, ray_color, (8 * i + 1000, (line_height + 1500 - line_offset)), (8 * i + 1000, 1500 - line_offset), 8)
