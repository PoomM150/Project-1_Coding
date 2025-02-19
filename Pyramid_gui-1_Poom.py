import math
import tkinter as tk
from tkinter import ttk, messagebox

def pyramid_volume(base, height, base_shape):
    if height <= 0:
        return None
    
    if base_shape == "triangle":
        if base[0] <= 0 or base[1] <= 0:
            return None
        base_area = 0.5 * base[0] * base[1]
    elif base_shape == "square":
        if base[0] <= 0:
            return None
        base_area = base[0] ** 2
    elif base_shape == "rectangle":
        if base[0] <= 0 or base[1] <= 0:
            return None
        base_area = base[0] * base[1]
    elif base_shape == "hexagon":
        if base[0] <= 0:
            return None
        base_area = (3 * math.sqrt(3) * (base[0] ** 2)) / 2
    else:
        return None
    
    volume = (1/3) * base_area * height
    return volume

def calculate_volume():
    base_shape = shape_var.get()
    try:
        height = float(height_entry.get())
        if height <= 0 or height > 150:
            messagebox.showerror("ข้อผิดพลาด", "ค่าความสูงต้องอยู่ระหว่าง 0 - 150")
            return
        
        if base_shape in ["triangle", "rectangle"]:
            base1 = float(base1_entry.get())
            base2 = float(base2_entry.get())
            if base1 <= 0 or base2 <= 0 or base1 > 100 or base2 > 100:
                messagebox.showerror("ข้อผิดพลาด", "ค่ากว้างและยาวต้องอยู่ระหว่าง 0 - 100")
                return
            base = (base1, base2)
        elif base_shape in ["square", "hexagon"]:
            base1 = float(base1_entry.get())
            if base1 <= 0 or base1 > 100:
                messagebox.showerror("ข้อผิดพลาด", "ค่าด้านฐานต้องอยู่ระหว่าง 0 - 100")
                return
            base = (base1,)
        else:
            messagebox.showerror("ข้อผิดพลาด", "ประเภทฐานไม่ถูกต้อง")
            return
        
        volume = pyramid_volume(base, height, base_shape)
        if volume is not None:
            result_label.config(text=f"ปริมาตรของพีระมิดฐาน {base_shape}: {volume:.2f}")
        else:
            messagebox.showerror("ข้อผิดพลาด", "ค่าที่ป้อนไม่ถูกต้อง โปรดลองอีกครั้ง")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "โปรดป้อนค่าที่ถูกต้อง")

def reset_fields():
    base1_entry.delete(0, tk.END)
    base2_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# สร้าง GUI
root = tk.Tk()
root.title("คำนวณปริมาตรพีระมิด")

# ตัวเลือกฐานพีระมิด
shape_var = tk.StringVar(value="triangle")
ttk.Label(root, text="เลือกประเภทฐาน:").grid(row=0, column=0)
shape_menu = ttk.Combobox(root, textvariable=shape_var, values=["triangle", "square", "rectangle", "hexagon"])
shape_menu.grid(row=0, column=1)
shape_menu.current(0)

# ป้อนค่าพื้นฐาน
ttk.Label(root, text="กว้าง / ด้านฐาน:").grid(row=1, column=0)
base1_entry = ttk.Entry(root)
base1_entry.grid(row=1, column=1)

ttk.Label(root, text="ยาวฐาน (เฉพาะ rectangle, triangle):").grid(row=2, column=0)
base2_entry = ttk.Entry(root)
base2_entry.grid(row=2, column=1)

# ป้อนค่าความสูง
ttk.Label(root, text="ความสูง:").grid(row=3, column=0)
height_entry = ttk.Entry(root)
height_entry.grid(row=3, column=1)

# ปุ่มคำนวณและรีเซ็ต
button_frame = ttk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=2)
calculate_button = ttk.Button(button_frame, text="คำนวณ", command=calculate_volume)
calculate_button.pack(side=tk.LEFT, padx=5)
reset_button = ttk.Button(button_frame, text="รีเซ็ต", command=reset_fields)
reset_button.pack(side=tk.RIGHT, padx=5)

# แสดงผลลัพธ์
result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
