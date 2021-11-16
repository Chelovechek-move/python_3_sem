from PIL import Image
import numpy as np

# считаем картинку в numpy array
img = Image.open("lunar02_raw.jpg")
data = np.array(img)

# ... логика обработки
new_data = (data - data.min()) / (data.max() - data.min()) * 255

# запись картинки после обработки
res_img = Image.fromarray(new_data)
res_img = res_img.convert('L')              # to convert image in gray scale
res_img.save("lunar02_new.jpg")