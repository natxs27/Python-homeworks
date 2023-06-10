from PIL import Image
image_path = r"/Users/natalia/Downloads/piesek.jpeg"
image = Image.open(image_path)
print("Image Mode:", image.mode)
print("Image Size:", image.size)
print("Image Format:", image.format)
thumbnail_size = (128, 128)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)
thumbnail_path = "thumbnail.jpg"
thumbnail.save(thumbnail_path)
print("Thumbnail created successfully.")