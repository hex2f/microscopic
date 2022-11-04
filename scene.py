class Scene:
  def __init__(self):
    self.entities = []
    self.viewport = [0, 0]
    self.frame = 0
  
  def add_entity(self, entity):
    setattr(entity, 'scene', self)
    self.entities.append(entity)
  
  def remove_entity(self, entity):
    self.entities.remove(entity)
  
  def start(self):
    for entity in self.entities:
      entity.start_components()
  
  def update_entities(self):
    self.frame += 1
    for entity in self.entities:
      entity.update_components()

  def draw_entities(self):
    for entity in self.entities:
      entity.draw_components()
  