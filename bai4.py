import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Đọc dữ liệu từ file CSV
df = pd.read_csv('diemPython.csv')

# Chuyển dữ liệu thành mảng numpy
in_data = np.array(df.iloc[:, :])

# Tính toán thông tin
total_students = np.sum(in_data[:, 2])
diemA = in_data[:, 4]
diemB_plus = in_data[:, 5]
diemB = in_data[:, 6]
diemC_plus = in_data[:, 7]
diemC = in_data[:, 8]
diemD_plus = in_data[:, 9]
diemD = in_data[:, 10]
diemF = in_data[:, 11]
L1_scores = in_data[:, 12]
L2_scores = in_data[:, 13]
lops = in_data[:, 1]  # Class identifiers
max_diemA = diemA.max()
max_diemA_index = np.where(diemA == max_diemA)[0]

# Hàm vẽ biểu đồ
def show_plot(title, x, y_data, labels, xlabel, ylabel):
    top = Toplevel()
    top.title(title)

    fig, ax = plt.subplots(figsize=(12, 8))
    for y, label in zip(y_data, labels):
        ax.plot(x, y, label=label, marker='o')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.grid(True)

    # Xoay nhãn trục x dọc
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=30)  # Hiển thị nhãn dọc

    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Hàm hiển thị từng biểu đồ
def plot_diem():
    show_plot(
        "Biểu đồ phân bố điểm theo lớp",
        lops,
        [diemA, diemB_plus, diemB, diemC_plus, diemC, diemD_plus, diemD, diemF],
        ["Điểm A", "Điểm B+", "Điểm B", "Điểm C+", "Điểm C", "Điểm D+", "Điểm D", "Điểm F"],
        "Lớp",
        "Số sinh viên"
    )

def plot_tx():
    tx1_scores = in_data[:, 14]
    tx2_scores = in_data[:, 15]
    show_plot(
        "Biểu đồ phân bố điểm TX1 và TX2 theo lớp",
        lops,
        [tx1_scores, tx2_scores],
        ["TX1", "TX2"],
        "Lớp",
        "Điểm bài kiểm tra"
    )

def plot_L1_L2():
    show_plot(
        "Điểm chuẩn đầu ra L1 và L2 theo lớp",
        lops,
        [L1_scores, L2_scores],
        ["L1", "L2"],
        "Lớp",
        "Điểm chuẩn đầu ra"
    )

# Giao diện Tkinter
root = Tk()
root.title("Thống kê điểm thi")

# Hiển thị thông tin tóm tắt
Label(root, text=f"Tổng số sinh viên đi thi: {total_students}").pack()
Label(root, text=f"Số sinh viên đạt điểm A: {np.sum(diemA)}").pack()
Label(root, text=f"Số sinh viên đạt điểm B+: {np.sum(diemB_plus)}").pack()
Label(root, text=f"Số sinh viên đạt điểm B: {np.sum(diemB)}").pack()
Label(root, text=f"Số sinh viên đạt điểm C+: {np.sum(diemC_plus)}").pack()
Label(root, text=f"Số sinh viên đạt điểm C: {np.sum(diemC)}").pack()
Label(root, text=f"Số sinh viên đạt điểm D+: {np.sum(diemD_plus)}").pack()
Label(root, text=f"Số sinh viên đạt điểm D: {np.sum(diemD)}").pack()
Label(root, text=f"Số sinh viên rớt (F): {np.sum(diemF)}").pack()
Label(root, text=f"Trung bình điểm chuẩn đầu ra L1: {np.mean(L1_scores):.2f}").pack()
Label(root, text=f"Trung bình điểm chuẩn đầu ra L2: {np.mean(L2_scores):.2f}").pack()
Label(root, text=f"Lớp có nhiều sinh viên đạt điểm A nhất: {lops[max_diemA_index]} với {max_diemA} sinh viên.").pack()

# Thêm các nút để hiển thị biểu đồ
Button(root, text="Biểu đồ phân bố điểm theo lớp", command=plot_diem).pack(pady=5)
Button(root, text="Biểu đồ TX1 và TX2 theo lớp", command=plot_tx).pack(pady=5)
Button(root, text="Biểu đồ điểm chuẩn đầu ra L1 và L2", command=plot_L1_L2).pack(pady=5)

# Chạy giao diện
root.mainloop()
