import pyxel
from entities.player import Player

class App:
  def __init__(self):
    pyxel.init(160, 120, title="microscopic")

    self.entities = [
      Player(80, 60)
    ]

    for entity in self.entities:
      entity.start_components()

    pyxel.run(self.update, self.draw)


  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pyxel.cls(0)
    for entity in self.entities:
      entity.update_components()
    for entity in self.entities:
      entity.draw_components()
    # pyxel.text(55, 41, "Hello, snåp!", pyxel.frame_count % 16)
    # pyxel.blt(61, 66, 0, 0, 0, 38, 16)

App()