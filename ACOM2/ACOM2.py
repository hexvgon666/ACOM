import cv2
import numpy as np
#задание 1
#Открываем камеру
cap = cv2.VideoCapture(0)

while True:
    # Считываем кадр с камеры
    ret, frame = cap.read()

    # Преобразуем кадр в формат HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Отображаем кадр в окне
    cv2.imshow('HSV Image', hsv)

    # Ждем нажатия клавиши 'q' для выхода из программы
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()

#задание 2

#Открываем камеру
cap = cv2.VideoCapture(0)

while True:
    # Считываем кадр с камеры
    ret, frame = cap.read()

    # Преобразуем кадр в формат HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Определяем диапазон красного цвета
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Создаем маску для выделения красного цвета
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Применяем маску к изображению
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Отображаем результат
    cv2.imshow('Filtered Image', result)

    # Ждем нажатия клавиши 'q' для выхода из программы
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()

#задание 3,4,5
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Не удалось получить кадр")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_frame = cv2.inRange(hsv_frame, (0, 100, 100), (10, 255, 255))
    kernel = np.ones((5, 5), np.uint8)
    erode = cv2.erode(red_frame, kernel, iterations=1)
    dilate = cv2.dilate(erode, kernel, iterations=1)

    moment = cv2.moments(erode)
    if (moment["m00"] != 0):
        print(f"Площадь: {moment['m00']}")
        print(f"Моменты 1 порядка: {moment['m01']}, {moment['m10']}")
        xc = int(moment['m10'] / moment['m00'])
        yc = int(moment['m01'] / moment['m00'])
    (contours, _) = cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for countour in contours:
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
