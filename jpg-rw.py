import cv2
from os.path import join

def show_image(path):
    image = cv2.imread(path)
    cv2.imshow('Image', image)
    
    cv2.waitKey(0)
    
def convert_png_to_jpg(path):
    image = cv2.imread(path)
    cv2.imwrite(path.replace('png', 'jpg'), image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    
show_image(join('images','zebras.jpg'))
convert_png_to_jpg(join('images','hulk.png'))