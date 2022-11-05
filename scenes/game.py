from entities.enemy import Enemy
from entities.wave import Wave
from scene import Scene
from entities.player import Player
import pyxel

class GameScene(Scene):
  def __init__(self):
    super().__init__()

    self.add_entity(Player(80-8//2, 60-8//2))
    self.add_entity(Wave({ "enemies": 5, "pattern": { "type": "circle", "radius": 24, "x": 0, "y": 0 } }))
    self.add_entity(Wave({ "enemies": 4, "pattern": { "type": "line", "x1": -64, "y1": -48, "x2": 64, "y2": -48 } }))

    pyxel.image(1).load(0, 0, "background.png")

  def update(self):
    if self.frame % 8 == 0:
      self.viewport[1] += 1
    self.update_entities()
  
  def draw(self):
    # pyxel.camera(self.viewport[0], self.viewport[1])
    pyxel.blt(0, self.viewport[1] % 120, 1, 0, 0, 160, 120)
    pyxel.blt(0, (self.viewport[1] % 120) - 120, 1, 0, 0, 160, 120)
    self.draw_entities()