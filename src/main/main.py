from main.functions import FunctionsClass

img_arr = ["src/image/1.jpg", "src/image/2.jpg", "src/image/3.jpg"]

img_processor = FunctionsClass(img_arr)

processed_img = img_processor.img_process()

print(processed_img)
