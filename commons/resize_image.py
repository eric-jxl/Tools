# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-08-07 09:24
'''
import base64
__all__ =['image_resize_image','encode_base64','decode_base64']
__author__ = 'Eric'
__doc__ = "压缩图片 默认像素1024*1024"

try:
    import cStringIO as StringIO
except ImportError:
    try:
        import StringIO
    except ImportError:
        from io import StringIO


from PIL import Image
from PIL import ImageEnhance

def encode_base64(file_path):
    with open(file_path,'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)
        return base64_data
def decode_base64(fname,base64_data):
    with open(fname,'wb') as file:
        decode_data = base64.b64decode(base64_data)  # 解码
        file.write(decode_data)


# source_data = encode_base64('/Users/eric/Documents/photo/2a4100008d310b5fd8a8.jpeg')

def image_resize_image(base64_source, size=(1024, 1024), encoding='base64', filetype=None, avoid_if_small=False):

    if not base64_source:
        return False
    if size == (None, None):
        return base64_source
    image_stream = StringIO.StringIO(base64_source.decode(encoding))
    image = Image.open(image_stream)
    # store filetype here, as Image.new below will lose image.format
    filetype = (filetype or image.format).upper()

    filetype = {
        'BMP': 'PNG',
    }.get(filetype, filetype)

    asked_width, asked_height = size
    if asked_width is None:
        asked_width = int(image.size[0] * (float(asked_height) / image.size[1]))
    if asked_height is None:
        asked_height = int(image.size[1] * (float(asked_width) / image.size[0]))
    size = asked_width, asked_height

    # check image size: do not create a thumbnail if avoiding smaller images
    if avoid_if_small and image.size[0] <= size[0] and image.size[1] <= size[1]:
        return base64_source

    if image.size != size:
        image = image_resize_and_sharpen(image, size)
    if image.mode not in ["1", "L", "P", "RGB", "RGBA"]:
        image = image.convert("RGB")

    background_stream = StringIO.StringIO()
    image.save(background_stream, filetype)
    return background_stream.getvalue().encode(encoding)

def image_resize_and_sharpen(image, size, preserve_aspect_ratio=False, factor=2.0):

    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    image.thumbnail(size, Image.ANTIALIAS)
    if preserve_aspect_ratio:
        size = image.size
    sharpener = ImageEnhance.Sharpness(image)
    resized_image = sharpener.enhance(factor)
    # create a transparent image for background and paste the image on it
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    image.paste(resized_image, ((size[0] - resized_image.size[0]) / 2, (size[1] - resized_image.size[1]) / 2))
    return image

# coding  = image_resize_image(source_data)
# decode_base64('风景.jpg',coding)