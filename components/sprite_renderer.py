import pyxel
from components.transform import Transform

class SpriteRenderer:
  def __init__(self, sprite: tuple = (0, 0), grid_size: int = 8):
    self.uv = sprite
    self.grid_size = grid_size

  def start(self):
    self.transform = self.entity.get_component(Transform)

  def draw(self):
    pyxel.blt(self.transform.x, self.transform.y, 0, self.uv[0] * self.grid_size, self.uv[1] * self.grid_size, 8, 8, 0)
