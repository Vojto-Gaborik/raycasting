import numpy as np
import map


class Ray:
    def __init__(self, rotation, x, y, orientation, map_grid):
        self.rotation = rotation
        self.x = x
        self.y = y
        self.orientation = orientation
        self.x_offset = None
        self.y_offset = None
        self.player_x = x
        self.player_y = y
        self.map_grid = map_grid
        self.unit_in_map = 1000 / len(map_grid)

        if orientation == 'horizontal':
            self.horizontal_orientation()
        elif orientation == 'vertical':
            self.vertical_orientation()

    def horizontal_orientation(self):
        inverse_of_tangent = (-1 / np.tan(self.rotation))
        if self.rotation < np.pi:  # looking up
            self.y = (np.ceil(self.player_y / self.unit_in_map) * self.unit_in_map) - self.unit_in_map  # round to nearest 1020/8 down
            self.x = self.player_x - (inverse_of_tangent * (self.player_y - self.y))
            self.y_offset = -self.unit_in_map
            self.x_offset = self.y_offset * inverse_of_tangent
        elif self.rotation > np.pi:  # looking down
            self.y = (np.ceil(self.player_y / self.unit_in_map) * self.unit_in_map)  # round to nearest 1020/8 up
            self.x = self.player_x - (inverse_of_tangent * (self.player_y - self.y))
            self.y_offset = self.unit_in_map
            self.x_offset = self.y_offset * inverse_of_tangent
        elif int(self.rotation * 100000) == int(np.pi * 100000):
            self.y = self.player_y
            self.x = self.player_x
            self.x_offset = 1000
            self.y_offset = 1000
        else:
            self.y = self.player_y
            self.x = -self.player_x
            self.x_offset = 1000
            self.y_offset = 1000

        for d in range(len(self.map_grid)):
            mx = int(self.x / self.unit_in_map)
            if self.rotation < np.pi:
                my = int(self.y / self.unit_in_map) - 1
            else:
                my = int(self.y / self.unit_in_map)
            if 0 <= mx <= len(self.map_grid) - 1 and 0 <= my <= len(self.map_grid) - 1 and self.map_grid[my][mx] == 1:
                break
            else:
                self.y += self.y_offset
                self.x += self.x_offset

    def vertical_orientation(self):
        negative_tangent = -np.tan(self.rotation)
        if np.pi / 2 < self.rotation < 3 / 2 * np.pi:  # looking left
            self.x = (np.ceil(self.player_x / self.unit_in_map) * self.unit_in_map) - self.unit_in_map  # round to nearest 1020/8 down
            self.y = self.player_y - negative_tangent * (self.player_x - self.x)
            self.x_offset = self.unit_in_map
            self.y_offset = self.x_offset * negative_tangent
        elif int(self.rotation * 100000) == int(np.pi / 2 * 100000) or int(self.rotation * 100000) == int(3 / 2 * np.pi * 100000):
            self.x = self.player_x
            self.y = self.player_y
            self.x_offset = 1000
            self.y_offset = 1000
        elif self.rotation < np.pi / 2 or self.rotation > 3 / 2 * np.pi:  # looking right
            self.x = (np.ceil(self.player_x / self.unit_in_map) * self.unit_in_map)  # round to nearest 1020/8 down
            self.y = self.player_y - negative_tangent * (self.player_x - self.x)
            self.x_offset = -self.unit_in_map
            self.y_offset = self.x_offset * negative_tangent

        for d in range(len(self.map_grid)):
            if np.pi / 2 < self.rotation < 3 / 2 * np.pi:
                mx = int(self.x / self.unit_in_map) - 1
            else:
                mx = int(self.x / self.unit_in_map)
            my = int(self.y / self.unit_in_map)
            if 0 <= mx <= len(self.map_grid) - 1 and 0 <= my <= len(self.map_grid) - 1 and self.map_grid[my][mx] == 1:
                break
            else:
                self.y -= self.y_offset
                self.x -= self.x_offset
