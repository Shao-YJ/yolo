import os
import cv2
from numpy.core.defchararray import isnumeric

image_path = 'F:/python/cycle gan/strengthganphoto'
annotation_path = 'F:/python/cycle gan/strengthganxml'

image_save_path = './Images'
annotation_save_path = './Annotations'

image_list = os.listdir(image_path)
annotation_list = os.listdir(annotation_path)

num=0
# for i in annotation_list:
#     # print(i[-7])
#     if i[-7].isnumeric() is False:
#         os.remove(os.path.join(annotation_path,i))
#         num+=1
# print(num)

# for i in annotation_list:
#     path = os.path.join(annotation_path, i)
#     with open(path) as f:
#         file = open(os.path.join(annotation_save_path, i.replace('_', '-')), mode='w')
#         txt = f.read()
#         file.write(txt)
#         file.close()
#         f.close()

for i in image_list:
    path = os.path.join(image_path, i)
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    save_path = os.path.join(image_save_path, i.replace('_', '-'))
    cv2.imwrite(save_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    print(save_path)
