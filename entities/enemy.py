from components.sprite_animator import SpriteAnimator
from components.sprite_renderer import SpriteRenderer
from components.transform import Transform
from entities.bullet import Bullet
from entity import Entity
import spritesheet

class Enemy(Entity):
  def __init__(self, i: int, x: int, y: int):
    super().__init__()

    self.i = i

    self.add_component(SpriteRenderer())
    self.add_component(SpriteAnimator(spritesheet.animations['blobbe']))
    self.add_component(Transform(x, y))

  def start(self):
    self.transform = self.get_component(Transform)
  
  def update(self):
    if self.scene.frame % 35 == 0:
      self.scene.add_entity(Bullet(self.transform.x + 3, self.transform.y + 2, (0, 2)))
