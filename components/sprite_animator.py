import pyxel
from components.sprite_renderer import SpriteRenderer
from components.transform import Transform

class SpriteAnimator:
  def __init__(self, animation = { 'frames': [(0, 0), (0, 1)], 'frame_steps': 10 }, grid_size: int = 8):
    self.animation = animation
    self.grid_size = grid_size

  def start(self):
    print('SpriteAnimator.start()')
    self.transform = self.entity.get_component(Transform)
    self.sprite_renderer = self.entity.get_component(SpriteRenderer)

  def update(self):
    if self.entity.scene.frame % self.animation['frame_steps'] == 0:
      self.sprite_renderer.uv = self.animation['frames'][self.entity.scene.frame // self.animation['frame_steps'] % len(self.animation['frames'])] 

