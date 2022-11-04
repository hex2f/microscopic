import pyxel
from components.transform import Transform

class RectRenderer:
  def __init__(self, color, height, width):
    self.color = color
    self.height = height
    self.width = width

  def start(self):
    self.transform = self.entity.get_component(Transform)

  def draw(self):
    pyxel.rect(self.transform.x, self.transform.y, self.height, self.width, self.color)