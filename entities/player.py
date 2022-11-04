from components.rect_renderer import RectRenderer
from components.transform import Transform
from entity import Entity
from components.keyboard_movement import KeyboardMovement

class Player(Entity):
  def __init__(self, x: int, y: int):
    super().__init__()

    self.add_component(RectRenderer(self, 7, 8, 8))
    self.add_component(Transform(self))
    self.add_component(KeyboardMovement(self, 0.1))
  