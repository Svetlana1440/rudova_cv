import cv2
import numpy as np
from collections import defaultdict
# Загрузите изображение
image = cv2.imread('balls_and_rects.png')

# Преобразуйте в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Примените пороговое значение для выделения фигур
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Найдите контуры
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Итерируйте по контурам и обработайте каждую фигуру
dict = defaultdict(lambda: 0)
rects = []
circles = []
for contour in contours:
    # Получите цвет фигуры
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)
    mean_color = cv2.mean(image, mask=mask)
    meanc = np.
    # Добавьте фигуру в словарь с цветом в качестве ключа
    dict[meanc] += 1

    # Определите тип фигуры
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == 4:
        rects.append(contour)
    elif len(approx) == 8:
        circles.append(contour)

# Выведите количество фигур каждого оттенка
print("Общее количество фигур: ", len(contours))
print("Количество прямоугольников: ", len(rects))
print("Количество кругов: ", len(circles))

# Выведите количество фигур каждого оттенка для прямоугольников и кругов
rect_colors = defaultdict(lambda: 0)
circle_colors = defaultdict(lambda: 0)
for rect in rects:
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [rect], -1, 255, -1)
    mean_color = cv2.mean(image, mask=mask)[:3]
    rect_colors[mean_color] += 1

for circle in circles:
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [circle], -1, 255, -1)
    mean_color = cv2.mean(image, mask=mask)[:3]
    circle_colors[mean_color] += 1

print("Количество прямоугольников каждого оттенка: ", rect_colors)
print("Количество кругов каждого оттенка: ", circle_colors)