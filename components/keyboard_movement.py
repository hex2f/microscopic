from components.transform import Transform
import pyxel
import time

class KeyboardMovement:
  def __init__(self, speed: float):
    self.speed = speed
    self.last_frame_time = 0 

  def start(self):
    self.last_frame_time = time.time_ns() / 1_000_000_000
    self.transform = self.entity.get_component(Transform)

  def update(self):
    frame_time = time.time_ns() / 1_000_000_000 - self.last_frame_time
    if pyxel.btn(pyxel.KEY_LEFT):
      self.transform.x_velocity -= self.speed * frame_time
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.transform.x_velocity += self.speed * frame_time
    if pyxel.btn(pyxel.KEY_UP):
      self.transform.y_velocity -= self.speed * frame_time
    if pyxel.btn(pyxel.KEY_DOWN):
      self.transform.y_velocity += self.speed * frame_time
