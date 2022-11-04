from components.sprite_animator import SpriteAnimator
from components.sprite_renderer import SpriteRenderer
from components.transform import Transform
from entity import Entity
from components.keyboard_movement import KeyboardMovement
import spritesheet

class Player(Entity):
  def __init__(self, x: int, y: int):
    super().__init__()

  
    self.add_component(SpriteRenderer())
    self.add_component(SpriteAnimator(spritesheet.animations['blobbe']))
    self.add_component(Transform(x, y))
    self.add_component(KeyboardMovement(0.1))
