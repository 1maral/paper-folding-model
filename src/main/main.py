from functions import ImageClass

img_arr = ['src/image/1.jpg', 'src/image/2.jpg', 'src/image/3.jpg']

img_processor = ImageClass(img_arr)

processed_img = img_processor.img_process()

print("The processed image example: ")

processed_img[0].show()
