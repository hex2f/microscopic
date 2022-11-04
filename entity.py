class Entity:
  def __init__(self):
    self.components = {}

  def add_component(self, component):
    self.components[component.__class__.__name__] = component

  def remove_component(self, component):
    del self.components[component.__name__]

  def get_component(self, component):
    return self.components[component.__name__]

  def start_components(self):
    for component in self.components.values():
      if hasattr(component, "start"):
        component.start()

    if hasattr(self, "start"):
      self.start()

  def update_components(self):
    if hasattr(self, "update"):
      self.update()
  
    for component in self.components.values():
      if hasattr(component, "update"):
        component.update()

  def draw_components(self):
    if hasattr(self, "draw"):
      self.draw()

    for component in self.components.values():
      if hasattr(component, "draw"):
        component.draw()