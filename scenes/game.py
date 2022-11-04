from scene import Scene
from entities.player import Player
import pyxel

class GameScene(Scene):
  def __init__(self):
    super().__init__()

    self.add_entity(Player(80-8//2, 60-8//2))

    pyxel.image(1).load(0, 0, "background.png")

  def update(self):
    self.viewport[1] -= 0.5
    self.update_entities()
  
  def draw(self):
    pyxel.camera(self.viewport[0], self.viewport[1])
    pyxel.blt(0, (self.viewport[1]//120) * 120, 1, 0, 0, 160, 120)
    pyxel.blt(0, (self.viewport[1]//120) * 120 + 120, 1, 0, 0, 160, 120)
    self.draw_entities()