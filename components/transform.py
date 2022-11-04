from entity import Entity

class Transform:
  def __init__(self, entity: Entity, max_velocity: float = 2.5, drag: float = 0.9):
    self.entity = entity
    self.x = 0
    self.y = 0
    self.x_velocity = 0
    self.y_velocity = 0
    self.max_velocity = max_velocity
    self.drag = drag

  def start(self):
    pass

  def update(self):
    self.x_velocity = max(min(self.x_velocity, self.max_velocity), -self.max_velocity)
    self.y_velocity = max(min(self.y_velocity, self.max_velocity), -self.max_velocity)
    self.x += self.x_velocity
    self.y += self.y_velocity
    self.x_velocity *= self.drag
    self.y_velocity *= self.drag
