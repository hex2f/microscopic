from components.sprite_animator import SpriteAnimator
from components.sprite_renderer import SpriteRenderer
from components.transform import Transform
from entities.bullet import Bullet
from entities.enemy import Enemy
from entity import Entity
import pyxel
import spritesheet

# wave example: { "enemies": 5, "pattern": { "type": "circle", "radius": 64, "x": 0, "y": 0 } }

class Wave(Entity):
  def __init__(self, wave):
    super().__init__()
    self.enemies = []
    self.wave = wave
    self.add_component(Transform(160 // 2, -120 // 2))

  def start(self):
    self.transform = self.get_component(Transform)
    if self.wave['pattern']['type'] == "circle":
      r = self.wave['pattern']['radius']
      for i in range(self.wave['enemies']):
        angle = 360.0 / self.wave['enemies'] * i
        enemy = Enemy(i, self.transform.x + (pyxel.cos(angle) * r), self.transform.y + (pyxel.sin(angle) * r))
        self.scene.add_entity(enemy)
        self.enemies.append(enemy)
    elif self.wave['pattern']['type'] == "line":
      from_x = self.wave['pattern']['x1']
      from_y = self.wave['pattern']['y1']
      to_x = self.wave['pattern']['x2']
      to_y = self.wave['pattern']['y2']
      for i in range(self.wave['enemies']):
        enemy = Enemy(i, from_x + ((to_x - from_x) / self.wave['enemies'] * i), from_y + ((to_y - from_y) / self.wave['enemies'] * i))
        self.scene.add_entity(enemy)
        self.enemies.append(enemy)

  def update(self):
    if self.wave['pattern']['type'] == 'circle':
      for enemy in self.enemies:
        angle = (360.0 / self.wave['enemies'] * enemy.i) + ((self.scene.frame * 2) % 360)
        enemy.transform.x = self.transform.x + (pyxel.cos(angle) * self.wave['pattern']['radius'])
        enemy.transform.y = self.transform.y + (pyxel.sin(angle) * self.wave['pattern']['radius'])
        if enemy.transform.y > 120:
          self.enemies.remove(enemy)
          self.scene.remove_entity(enemy)
    elif self.wave['pattern']['type'] == 'line':
      # move back and forth on the line
      from_x = self.wave['pattern']['x1']
      from_y = self.wave['pattern']['y1']
      to_x = self.wave['pattern']['x2']
      to_y = self.wave['pattern']['y2']
      for enemy in self.enemies:
        enemy.transform.x = self.transform.x + (from_x + ((to_x - from_x) / self.wave['enemies'] * enemy.i) + (pyxel.sin(self.scene.frame * 2) * 16) + 8)
        enemy.transform.y = self.transform.y + (from_y + ((to_y - from_y) / self.wave['enemies'] * enemy.i))
        if enemy.transform.y > 120:
          self.enemies.remove(enemy)
          self.scene.remove_entity(enemy)

    self.transform.y += 0.25

    if len(self.enemies) == 0:
      self.scene.remove_entity(self)
  
