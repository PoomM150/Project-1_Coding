import math

def pyramid_volume(base, height, base_shape):
    if base_shape == "triangle":
        base_area = 0.5 * base[0] * base[1]  # base[0] = ฐาน, base[1] = สูงของสามเหลี่ยม
    elif base_shape == "square":
        base_area = base[0] ** 2  # base[0] = ด้านของสี่เหลี่ยมจัตุรัส
    elif base_shape == "rectangle":
        base_area = base[0] * base[1]  # base[0] = กว้าง, base[1] = ยาว
    elif base_shape == "hexagon":
        base_area = (3 * math.sqrt(3) * (base[0] ** 2)) / 2  # base[0] = ด้านของหกเหลี่ยม
    else:
        return "รูปทรงฐานไม่รองรับ"
    
    volume = (1/3) * base_area * height
    return volume

# รับค่าจากผู้ใช้
print("เลือกประเภทฐานของพีระมิด (triangle, square, rectangle, hexagon):")
base_shape = input().strip().lower()

if base_shape in ["triangle", "rectangle"]:
    base1 = float(input("ป้อนความกว้างของฐาน (ไม่เกิน 100): "))
    base2 = float(input("ป้อนความยาวของฐาน (ไม่เกิน 100): "))
    if base1 > 100 or base2 > 100:
        print("ค่าความกว้างหรือความยาวเกินขีดจำกัด")
        exit()
    base = (base1, base2)
elif base_shape in ["square", "hexagon"]:
    base1 = float(input("ป้อนความยาวด้านของฐาน (ไม่เกิน 100): "))
    if base1 > 100:
        print("ค่าความยาวด้านเกินขีดจำกัด")
        exit()
    base = (base1,)
else:
    print("ประเภทฐานไม่ถูกต้อง")
    exit()

height = float(input("ป้อนความสูงของพีระมิด (ไม่เกิน 150): "))
if height > 150:
    print("ค่าความสูงเกินขีดจำกัด")
    exit()

# คำนวณและแสดงผลลัพธ์
volume = pyramid_volume(base, height, base_shape)
print(f"ปริมาตรของพีระมิดฐาน {base_shape}: {volume:.2f}")
