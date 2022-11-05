from components.transform import Transform
import pyxel

from entities.bullet import Bullet

class Weapon:
  def __init__(self, fire_rate: int = 5, damage: int = 1):
    self.fire_rate = fire_rate
    self.damage = damage

  def fire(self, holder):
    holder.entity.scene.add_entity(Bullet(holder.transform.x + 3, holder.transform.y + 2, (0, -5)))

class WeaponHolder:
  def __init__(self, weapon: Weapon):
    self.weapon = weapon
    self.charge = 0

  def start(self):
    self.transform = self.entity.get_component(Transform)
    print(self.transform)

  def update(self):
    if pyxel.btn(pyxel.KEY_Z):
      if self.charge >= self.weapon.fire_rate:
        self.charge = 0
        self.weapon.fire(self)
    
    self.charge += 1

  def draw(self):
    if self.weapon.fire_rate >= 5 and self.charge < self.weapon.fire_rate + 2:
      fire_charge_progress = min(float(self.charge) / float(self.weapon.fire_rate), 1.0)
      pyxel.rect(self.transform.x, self.transform.y + 10, 8, 1, 6)
      pyxel.rect(self.transform.x, self.transform.y + 10, fire_charge_progress * 8, 1, 1)
