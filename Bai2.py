import tkinter as tk
from sympy import symbols, diff, integrate

def calculate():
    x = symbols('x')
    expr = entry_expr.get()
    operation = var.get()
    result = ""
    try:
        if operation == "Tính đạo hàm":
            result = diff(expr, x)
        elif operation == "Tính tích phân":
            result = integrate(expr, x)
        label_result.config(text=f"Kết quả: {result}")
    except Exception as e:
        label_result.config(text=f"Lỗi: {e}")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Tính Toán Đạo Hàm và Tích Phân")
window.geometry("400x200")

# Tạo giao diện người dùng
tk.Label(window, text="Nhập biểu thức (theo biến x):").pack(pady=5)
entry_expr = tk.Entry(window, width=40)
entry_expr.pack(pady=5)

# Tùy chọn giữa đạo hàm và tích phân
var = tk.StringVar(window)
var.set("Tính đạo hàm")  # giá trị mặc định
tk.OptionMenu(window, var, "Tính đạo hàm", "Tính tích phân").pack(pady=5)

# Nút tính toán
tk.Button(window, text="Tính toán", command=calculate).pack(pady=10)

# Hiển thị kết quả
label_result = tk.Label(window, text="Kết quả:")
label_result.pack(pady=5)

# Chạy giao diện
window.mainloop()