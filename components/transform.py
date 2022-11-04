class Transform:
  def __init__(self, x: int = 0, y: int = 0, max_velocity: float = 2.5, drag: float = 0.8):
    self.x = x
    self.y = y
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
