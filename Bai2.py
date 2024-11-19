import sympy as sp
import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Tạo biến x cho biểu thức
x = sp.symbols('x')


# Hàm xử lý nhập liệu hàm số
def parse_expression():
    try:
        expr_str = entry_expression.get()
        expr = sp.sympify(expr_str)
        return expr
    except (sp.SympifyError, ValueError):
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ! Vui lòng nhập đúng định dạng.")
        return None


# Tính đạo hàm
def calculate_derivative():
    expr = parse_expression()
    if expr:
        derivative = sp.diff(expr, x)
        result_label.config(text=f"Đạo hàm: {sp.simplify(derivative)}")


# Tính nguyên hàm
def calculate_integral():
    expr = parse_expression()
    if expr:
        integral = sp.integrate(expr, x)
        result_label.config(text=f"Nguyên hàm: {integral} + C")


# Tính tích phân xác định
def calculate_definite_integral():
    expr = parse_expression()
    if expr:
        try:
            a = float(entry_limit_a.get())
            b = float(entry_limit_b.get())
            definite_integral = sp.integrate(expr, (x, a, b))
            result_label.config(text=f"Tích phân từ {a} đến {b}: {definite_integral}")
        except ValueError:
            messagebox.showerror("Lỗi", "Giới hạn tích phân không hợp lệ!")


# Tính giới hạn
def calculate_limit():
    expr = parse_expression()
    if expr:
        try:
            limit_value = float(entry_limit.get())
            limit_result = sp.limit(expr, x, limit_value)
            result_label.config(text=f"Giới hạn tại x → {limit_value}: {limit_result}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ cho giới hạn!")


# Giao diện vẽ đồ thị hàm số
def plot_function():
    expr = parse_expression()
    if expr:
        try:
            # Chuyển đổi biểu thức thành hàm số Python
            expr_lambdified = sp.lambdify(x, expr, modules="numpy")

            # Tạo dữ liệu x và y để vẽ
            x_values = np.linspace(-10, 10, 500)
            y_values = expr_lambdified(x_values)

            # Vẽ đồ thị
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(x_values, y_values, label=f"{expr}")
            ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
            ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
            ax.grid(True)
            ax.set_title("Đồ thị hàm số")
            ax.legend()

            # Nhúng đồ thị vào Tkinter
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()
            canvas.draw()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể vẽ đồ thị hàm số! Chi tiết: {e}")


# Thiết kế giao diện Tkinter
window = tk.Tk()
window.title("Phần mềm hỗ trợ học tập Giải tích")
window.geometry("500x600")
window.configure(bg="#f2f2f2")

# Tiêu đề chính
title_label = tk.Label(window, text="Phần mềm hỗ trợ Giải tích", font=("Arial", 16, "bold"), bg="#4caf50", fg="white")
title_label.pack(fill=tk.X, pady=10)

# Khu vực nhập hàm số tự do
frame = tk.Frame(window, bg="#f2f2f2")
frame.pack(pady=10)

tk.Label(frame, text="Nhập hàm số:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
entry_expression = tk.Entry(frame, width=30)
entry_expression.grid(row=0, column=1, padx=5)

# Các nút chức năng với phong cách
button_frame = tk.Frame(window, bg="#f2f2f2")
button_frame.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=("Arial", 10, "bold"), padding=5)
btn_derivative = ttk.Button(button_frame, text="Tính Đạo hàm", command=calculate_derivative)
btn_derivative.grid(row=0, column=0, padx=5, pady=5)

btn_integral = ttk.Button(button_frame, text="Tính Nguyên hàm", command=calculate_integral)
btn_integral.grid(row=0, column=1, padx=5, pady=5)

btn_definite_integral = ttk.Button(button_frame, text="Tính Tích phân xác định", command=calculate_definite_integral)
btn_definite_integral.grid(row=1, column=0, padx=5, pady=5)

btn_limit = ttk.Button(button_frame, text="Tính Giới hạn", command=calculate_limit)
btn_limit.grid(row=1, column=1, padx=5, pady=5)

btn_plot = ttk.Button(button_frame, text="Vẽ đồ thị", command=plot_function)
btn_plot.grid(row=2, column=0, columnspan=2, pady=10)

# Nhập giới hạn tích phân và giá trị giới hạn
limit_frame = tk.Frame(window, bg="#f2f2f2")
limit_frame.pack(pady=5)

tk.Label(limit_frame, text="Giới hạn a:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
entry_limit_a = tk.Entry(limit_frame, width=10)
entry_limit_a.grid(row=0, column=1, padx=5)

tk.Label(limit_frame, text="Giới hạn b:", bg="#f2f2f2").grid(row=0, column=2, sticky="w")
entry_limit_b = tk.Entry(limit_frame, width=10)
entry_limit_b.grid(row=0, column=3, padx=5)

tk.Label(limit_frame, text="x tiến tới:", bg="#f2f2f2").grid(row=1, column=0, sticky="w")
entry_limit = tk.Entry(limit_frame, width=10)
entry_limit.grid(row=1, column=1, padx=5)

# Kết quả
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#333333")
result_label.pack(pady=20)

window.mainloop()
