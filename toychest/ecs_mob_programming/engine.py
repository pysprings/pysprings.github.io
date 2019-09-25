import time
from typing import Any

import attr
import esper
import pygame


@attr.s
class BoundingBox:
    top_left_x = attr.ib()
    top_left_y = attr.ib()
    width = attr.ib()
    height = attr.ib()


@attr.s
class Velocity:
    speed_x = attr.ib()
    speed_y = attr.ib()


class Gravity(esper.Processor):
    GRAVITY_ACCEL = 1

    def process(self) -> Any:
        for _ent_id, (rect_vals, vel_values) in self.world.get_components(
            BoundingBox, Velocity
        ):
            rect_vals.top_left_y += (
                vel_values.speed_y * 1 + self.GRAVITY_ACCEL * 1 * 0.5
            )
            vel_values.speed_y += self.GRAVITY_ACCEL * 1

class Renderer(esper.Processor):
    def __init__(self, window, clear_color=(0xFF, 0xFF, 0xFF)):
        self.window = window
        self.clear_color = clear_color

    def process(self) -> Any:
        self.window.fill(self.clear_color)
        for ent, box in self.world.get_component(BoundingBox):
            pygame.draw.rect(self.window, (128, 0xFF, 128), (box.top_left_x, box.top_left_y, box.width, box.height))

def main() -> None:
    pygame.init()
    window = pygame.display.set_mode((256, 256))
    pygame.display.set_caption('BLOCKS')
    clock = pygame.time.Clock()
    window.fill((0xFF, 0xFF, 0xFF))
    pygame.display.flip()

    world = esper.World()
    entity = world.create_entity()
    world.add_component(entity, BoundingBox(50, 50, 20, 20))
    world.add_component(entity, Velocity(10, -10))
    world.add_processor(Gravity())
    world.add_processor(Renderer(window))
    world.process()
    while True:
        for _ in range(30):
            world.process()
            time.sleep(.1)
            #print(world.components_for_entity(entity))
            pygame.display.flip()
        comp = world.component_for_entity(entity, BoundingBox)
        comp.top_left_y = 50
        comp = world.component_for_entity(entity, Velocity)
        comp.speed_y = -10
        
    input()


if __name__ == "__main__":
    main()
