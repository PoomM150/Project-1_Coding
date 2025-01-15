import math
def calculate_circle_area(redius):
    area = math.pi * radius ** 2
    return area
radius = float(input("กรุณากรอกค่ารัศมีวงกลม:"))
area = calculate_circle_area(radius)
print(f"พื้นที่ของวงกลมที่มีรัศมี {radius} {area:.2f}")