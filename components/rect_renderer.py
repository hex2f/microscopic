import pyxel
from components.transform import Transform
from entity import Entity

class RectRenderer:
  def __init__(self, entity: Entity, color, height, width):
    self.entity = entity
    self.color = color
    self.height = height
    self.width = width

  def start(self):
    self.transform = self.entity.get_component(Transform)

  def draw(self):
    pyxel.rect(self.transform.x, self.transform.y, self.height, self.width, self.color)