from components.rect_renderer import RectRenderer
from components.transform import Transform
from entity import Entity

class Bullet(Entity):
  def __init__(self, x: int, y: int, direction: tuple):
    super().__init__()

    self.direction = direction

    self.add_component(RectRenderer(13, 2, 2))
    self.add_component(Transform(x, y))
  
  def start(self):
    self.transform = self.get_component(Transform)

  def update(self):
    if self.transform.x < 0 or self.transform.x > 180 or self.transform.y < 0 or self.transform.y > 120:
      self.scene.remove_entity(self)

    self.transform.x += self.direction[0]
    self.transform.y += self.direction[1]