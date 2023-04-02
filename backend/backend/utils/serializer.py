def serialize_image(image):
    if image:
        image = image.replace("&export=download", "")
    return image
