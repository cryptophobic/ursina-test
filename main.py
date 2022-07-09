from math import radians, cos
from threading import Timer

from ursina import *

# create a window
from Player import Player
from screeninfo import get_monitors

# monitors = get_monitors()
# window.fullscreen_resolution = (monitors[0].width, monitors[0].height)
# window.fullscreen = True

#window.screen_resolution = (1600, 900)
app = Ursina()

player = Player(model='cube', origin_y=-.5, color=color.orange)

wall_left = Entity(model='cube', collider='box', scale_y=3, scale_z=2, origin_y=-.5, color=color.azure, x=-random.randrange(4, 10))
wall_right = duplicate(wall_left, x=random.randrange(4, 10), color=color.red)
wall_front = duplicate(wall_left, x=0, z=random.randrange(4, 10), color=color.green)
wall_back = duplicate(wall_front, z=-random.randrange(4, 10), color=color.yellow)
wall_big = Entity(model='cube', collider='box', scale_x=60, scale_z=2, origin_y=-.5, color=color.white, z=30)
wall_big_2 = Entity(model='cube', collider='box', scale_x=60, scale_z=2, origin_y=-.5, color=color.white, z=-30)
wall_big_3 = Entity(model='cube', collider='box', scale_x=2, scale_z=60, origin_y=-.5, color=color.white, x=30)
wall_big_4 = Entity(model='cube', collider='box', scale_x=2, scale_z=60, origin_y=-.5, color=color.white, x=-30)
camera.y = 3


def adjust_camera(player_rotation, player_position):
    rotation = radians(player_rotation.y+180)
    radius = 9
    z = radius*cos(rotation)
    x = radius*sin(rotation)

    camera.rotation_y = player_rotation.y
    camera.x = player_position.x + x
    camera.z = player_position.z + z

    camera.rotation_x = 10

    # originale = camera.world_position
    #new_hit_info = raycast(camera.world_position, LVector3f(x, 3, z), ignore=(camera, player), distance=9, debug=False)
    # if new_hit_info.hit:
    #     print('camera', LVector3f(x, 3, z), camera.world_position, camera.position)
    #     print(new_hit_info.hit)


def update():
    t = Timer(0.3, adjust_camera, (player.rotation, player.position))
    t.start()

    # print('camera=', camera.x, camera.z, camera.rotation.x, camera.rotation.y)
    # print('player=', player.x, player.z, player.rotation.x, player.rotation.y)


def input(key):
    if key == 'escape':
        quit()

# start running the game
app.run()


