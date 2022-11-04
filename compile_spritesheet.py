from PIL import Image
import os

import spritesheet

image = Image.new('RGBA', (256, 256), color = (0, 0, 0, 255))

for filename in spritesheet.sprites:
  sprite = Image.open(os.path.join('sprites', filename)).convert('RGBA')
  image.paste(sprite, (spritesheet.sprites[filename][0] * spritesheet.grid_size, spritesheet.sprites[filename][1] * spritesheet.grid_size), sprite)

image.save('spritesheet.png')