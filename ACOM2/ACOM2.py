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

#задание 3
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Не удалось получить кадр")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_frame = cv2.inRange(hsv_frame, (0, 100, 100), (10, 255, 255))
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(red_frame, kernel, iterations=1)
    erode = cv2.erode(dilate, kernel, iterations=1)
    cv2.imshow('Close', erode)

    erode = cv2.erode(red_frame, kernel, iterations=1)
    dilate = cv2.dilate(erode, kernel, iterations=1)
    cv2.imshow('Open', erode)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Задание 4
    moment = cv2.moments(erode)
    if (moment["m00"] != 0):
        print(f"Площадь: {moment['m00']}")
        print(f"Моменты 1 порядка: {moment['m01']}, {moment['m10']}")
        xc = int(moment['m10'] / moment['m00'])
        yc = int(moment['m01'] / moment['m00'])


# Определяем диапазоны для красного цвета в HSV
lower_red1 = np.array([0, 100, 100])  # HSV границы для первого диапазона (0-10)
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])  # HSV границы для второго диапазона (160-180)
upper_red2 = np.array([180, 255, 255])

# Создание объекта VideoCapture для захвата видео с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    # Чтение кадра из видео
    ret, frame = cap.read()

    if not ret:
        print("Не удалось получить кадр.")
        break

    # Преобразование изображения в HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Создание масок для красного цвета
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.add(mask1, mask2)  # Объединение двух масок

    # Морфологическая операция: сначала эрозия, затем дилатация
    kernel = np.ones((5, 5), np.uint8)  # Создаем структурный элемент

    # Эрозия для удаления шумов
    eroded_mask = cv2.erode(mask, kernel, iterations=1)
    # Дилатация для восстановления размера объекта
    dilated_mask = cv2.dilate(eroded_mask, kernel, iterations=1)

    # Поиск местоположения красного объекта
    M = cv2.moments(dilated_mask)

    if M["m00"] > 0:
        # Находим координаты центра массы
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # Рисуем черный прямоугольник вокруг красного объекта
        cv2.rectangle(frame, (cX - 50, cY - 50), (cX + 50, cY + 50), (0, 0, 0), 2)

    # Отображение кадра с прямоугольником
    cv2.imshow('Video Frame', frame)

    # Выход при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурса VideoCapture
cap.release()

# Закрытие всех окон
cv2.destroyAllWindows()

