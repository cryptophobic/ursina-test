from math import radians, cos

from ursina import *


class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'cube'
        self.color = color.orange
        self.collider = 'box'
        self.on_click = self.action
        self.direction = Vec3(0, 0, 1)

    def action(self):
        self.color = color.orange if self.color == color.red else color.red

    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            ).normalized()
        booster = 1 + 5 * held_keys['right shift']

        self.rotation_y += held_keys['d'] * 50 * time.dt * booster
        self.rotation_y -= held_keys['a'] * 50 * time.dt * booster
        if self.rotation_y > 360:
            self.rotation_y -= 360
        elif self.rotation_y < 0:
            self.rotation_y += 360
        # rotation = radians(self.rotation_y)
        # radius = 1
        # z = radius * cos(rotation)
        # x = radius * sin(rotation)
        # self.direction = LVector3f(x, 0, z)

        origin = self.world_position + (self.up*.5)
        hit_info = raycast(origin, self.direction, ignore=(self,), distance=0.5, debug=True)
        if not hit_info.hit:
            booster = 1 + 5 * held_keys['right shift']
            self.position += self.direction * 5 * time.dt * booster
            # if self.position.x > 30:
            #     self.position.x = 30
            #
            # if self.position.x < -30:
            #     self.position.x = -30
            #
            # if self.position.z > 30:
            #     self.position.z = 30
            #
            # if self.position.z < -30:
            #     self.position.z = -30

            print(self.position.x)
        else:
            # print('person', self.direction, origin, self.position)
            self.color = hit_info.entity.color

        #
        # self.x += held_keys['right arrow'] * time.dt * 5
        # self.x -= held_keys['left arrow'] * time.dt * 5
        # self.y += held_keys['up arrow'] * time.dt * 5
        # self.y -= held_keys['down arrow'] * time.dt * 5

    # def input(self, key):
    #     if key == 'w':
    #         self.position += self.forward
    #
    #     if key == 'd':
    #         self.animate('rotation_y', self.rotation_y + 90, duration=.1)
    #
    #     if key == 'a':
    #         self.animate('rotation_y', self.rotation_y - 90, duration=.1)
