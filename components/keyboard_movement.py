from components.transform import Transform
import pyxel
import time

class KeyboardMovement:
  def __init__(self, speed: float):
    self.speed = speed

  def start(self):
    self.transform = self.entity.get_component(Transform)

  def update(self):
    if pyxel.btn(pyxel.KEY_LEFT):
      self.transform.x -= self.speed
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.transform.x += self.speed
    if pyxel.btn(pyxel.KEY_UP):
      self.transform.y -= self.speed
    if pyxel.btn(pyxel.KEY_DOWN):
      self.transform.y += self.speed
