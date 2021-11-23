import numpy as np
import pygame as pg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.degree_in_radian = (2*np.pi)/360
        self.rotation = 3/2*(np.pi)
        self.velocity = 0.5
        self.font = pg.font.SysFont('comicsans', 40, True)

    def rotate_left(self):
        self.rotation = (self.rotation + self.degree_in_radian * 0.5) % (2 * np.pi)

    def rotate_right(self):
        self.rotation = (self.rotation - self.degree_in_radian * 0.5) % (2 * np.pi)

    def move_forward(self):
        self.x = self.x + ((np.cos(self.rotation)) * self.velocity)
        self.y = self.y - ((np.sin(self.rotation)) * self.velocity)

    def move_back(self):
        self.x = self.x + ((np.cos(self.rotation)) * self.velocity * -1)
        self.y = self.y - ((np.sin(self.rotation)) * self.velocity * -1)

    def rays(self, surface, map_grid):

        rotation = self.rotation + 30 * self.degree_in_radian
        for i in range(60):
            ray_x = None
            ray_y = None
            if rotation < np.pi:   # looking up
                ray_y = (np.ceil(self.y / 125) * 125) - 125   # round to nearest 1020/8 down
                ray_x = self.x - ((-1 / np.tan(rotation)) * (self.y - ray_y))
                ray_y_offset = -125
                ray_x_offset = ray_y_offset * (-1 / np.tan(rotation))
            elif rotation > np.pi:    # looking down
                ray_y = (np.ceil(self.y / 125) * 125)  # round to nearest 1020/8 up
                ray_x = self.x - ((-1 / np.tan(rotation)) * (self.y - ray_y))
                ray_y_offset = 125
                ray_x_offset = ray_y_offset * (-1 / np.tan(rotation))
            elif int(rotation * 100000) == int(np.pi * 100000):
                ray_y = self.y
                ray_x = self.x
            else:
                ray_y = self.y
                ray_x = -self.x

            for d in range(10):
                mx = int(ray_x / 125)
                if rotation < np.pi:
                    my = int(ray_y / 125) - 1
                else:
                    my = int(ray_y / 125)
                if 0 <= mx <= 7 and 0 <= my <= 7 and map_grid[my][mx] == 1:
                    break
                else:
                    ray_y += ray_y_offset
                    ray_x += ray_x_offset
            horizon_ray_x = ray_x
            horizon_ray_y = ray_y
            '''
            ray_x = None
            ray_y = None
            negative_tangent = -np.tan(rotation)
            if np.pi/2 < rotation < 3/2 * np.pi:  # looking left
                ray_x = (np.ceil(self.x / 125) * 125) - 125  # round to nearest 1020/8 down
                ray_y = self.y - negative_tangent * (self.x - ray_x)
                ray_x_offset = 125
                ray_y_offset = ray_x_offset * negative_tangent
            elif int(rotation * 100000) == int(np.pi/2 * 100000) or int(rotation * 100000) == int(3/2 * np.pi * 100000):
                ray_x = self.x
                ray_y = self.y
                ray_x_offset = 1020
                ray_y_offset = 1020
            elif rotation < np.pi/2 or rotation > 3/2 * np.pi:  # looking right
                ray_x = (np.ceil(self.x / 125) * 125)  # round to nearest 1020/8 down
                ray_y = self.y - negative_tangent * (self.x - ray_x)
                ray_x_offset = -125
                ray_y_offset = ray_x_offset * negative_tangent
            for d in range(10):
                if np.pi/2 < rotation < 3/2 * np.pi:
                    mx = int(ray_x / 125) - 1
                else:
                    mx = int(ray_x / 125)
                my = int(ray_y / 125)
                if 0 <= mx <= 7 and 0 <= my <= 7 and map_grid[my][mx] == 1:
                    break
                else:
                    ray_y -= ray_y_offset
                    ray_x -= ray_x_offset
            vertical_ray_x = ray_x
            vertical_ray_y = ray_y

            horizon_distance = np.hypot((horizon_ray_x - self.x),  (horizon_ray_y - self.y))
            vertical_distance = np.hypot((vertical_ray_x - self.x), (vertical_ray_y - self.y))
            '''
            #if horizon_distance <= vertical_distance:
                #ray_x = horizon_ray_x
                #ray_y = horizon_ray_y
            if rotation < np.pi:
                pg.draw.line(surface, (0, 0, 255), (self.x, self.y), (ray_x, ray_y), 6)
            else:
                pg.draw.line(surface, (255, 0, 0), (self.x, self.y), (ray_x, ray_y), 6)

            #else:
                #ray_x = vertical_ray_x
                #ray_y = vertical_ray_y
                #pg.draw.line(surface, (0, 255, 0), (self.x, self.y), (ray_x, ray_y), 6)
            rotation = (rotation - self.degree_in_radian) % (2 * np.pi)

