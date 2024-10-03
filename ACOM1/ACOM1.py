import cv2
#
# img1 = cv2.imread(r'629343.png')
# img2 = cv2.imread(r'629343.png', cv2.IMREAD_GRAYSCALE)
# img3 = cv2.imread(r'629343.png', cv2.IMREAD_REDUCED_GRAYSCALE_8)
#
# cv2.namedWindow('img 1',cv2.WINDOW_NORMAL)
# cv2.imshow('img 1',img1)
#
# cv2.namedWindow('img 2',cv2.WINDOW_FULLSCREEN)
# cv2.imshow('img 2',img2)
#
# cv2.namedWindow('img 3',cv2.WINDOW_AUTOSIZE)
# cv2.imshow('img 3',img3)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# #Задание 3
# cap = cv2.VideoCapture(r'document_5393446035680942834.mp4', cv2.CAP_ANY)
#
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#
#     frame = cv2.resize(frame, (320, 240))
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame = cv2.resize(frame, (520, 360))
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Gray frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame = cv2.resize(frame, (730, 480))
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     cv2.imshow('HSV frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cv2.destroyAllWindows()
#
# # Задание 4
#
# import cv2
#
# # Открыть исходный видеофайл
# input_file = r'C:/Users/hexvgon/PycharmProjects/ACOM1/VID-20210626-WA0025.mp4'
# cap = cv2.VideoCapture(input_file)
#
# # Получить характеристики исходного видео
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# # Создать объект для записи выходного видео
# output_file = 'output_video.mp4'
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
#
# # Читать кадры из исходного видео и записывать их в выходной файл
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     out.write(frame)
#
# cap.release()
# out.release()
#
#
# # Задание 5
#
# #Загрузка изображения
# img = cv2.imread(f'C:/Users/hexvgon/PycharmProjects/ACOM1/629343.png')
# # Преобразование в формат HSV
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # Создание окон для отображения
# cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
# cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)
# # Отображение изображений
# cv2.imshow('Original Image', img)
# cv2.imshow('HSV Image', hsv_img)
# # Ожидание нажатия клавиши для закрытия окон
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #
#Задание 6
cap = cv2.VideoCapture(0)

def draw_red_cross(frame):
    h, w, _ = frame.shape
    center_x = w // 2
    center_y = h // 2
    # Размеры креста
    cross_size = 100
    cross_thickness = 2
    # Рисование креста
    cv2.rectangle(frame, (center_x - cross_size // 2, center_y - cross_size // 8),
                  (center_x + cross_size // 2, center_y + cross_size // 8),
                  (0, 0, 255), cross_thickness)
    cv2.rectangle(frame, (center_x - cross_size // 8, center_y - cross_size // 2),
                  (center_x + cross_size // 8, center_y + cross_size // 2),
                  (0, 0, 255), cross_thickness)
    return frame

while True:
    ret, frame = cap.read()
    if ret:
        frame = draw_red_cross(frame)
        cv2.imshow('Red Cross', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# Задание 7
# import cv2
#
# # Open the default camera
# cap = cv2.VideoCapture(0)
#
# # Check if the camera is opened
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
#
# # Set the video resolution
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
# # Create a video writer to save the video
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))
#
# while True:
#     # Capture a frame from the camera
#     ret, frame = cap.read()
#
#     # Check if the frame was captured successfully
#     if not ret:
#         print("Cannot receive frame")
#         break
#
#     # Display the frame
#     cv2.imshow('frame', frame)
#
#     # Save the frame to the video file
#     out.write(frame)
#
#     # Press 'q' to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the camera and video writer
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#
# #Задание 8
# import cv2
# import numpy as np
#
#
# def draw_cross(frame, color):
#     h, w, _ = frame.shape
#     center_x = w // 2
#     center_y = h // 2
#     cross_size = 100
#     cross_thickness = 2
#
#     cv2.rectangle(frame, (center_x - cross_size // 2, center_y - cross_size // 8),
#                   (center_x + cross_size // 2, center_y + cross_size // 8),
#                   color, cross_thickness)
#     cv2.rectangle(frame, (center_x - cross_size // 8, center_y - cross_size // 2),
#                   (center_x + cross_size // 8, center_y + cross_size // 2),
#                   color, cross_thickness)
#     return frame
#
#
# def main():
#     frame = cv2.imread('C:/Users/hexvgon/PycharmProjects/ACOM1/2019-04-04_13-59-43-tn2.jpg')
#     center_pixel = frame[frame.shape[0] // 2, frame.shape[1] // 2]
#
#     if np.all(center_pixel >= np.array([90, 0, 0])):
#         color = (255, 0, 0)
#     elif np.all(center_pixel >= np.array([0, 90, 0])):  # Зеленый
#         color = (0, 255, 0)  # Зеленый
#     else:
#         color = (0, 0, 255)
#
#     frame = draw_cross(frame, color)
#     cv2.imshow('Cross', frame)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     main()
#
#
