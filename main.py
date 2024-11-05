import tkinter as tk
from tkinter import messagebox
import numpy as np

class UngDungGiaiPhuongTrinh:
    def __init__(self, master):
        self.master = master
        master.title("Giải hệ phương trình")

        self.so_phuong_trinh = 0
        self.he_so = []
        self.ket_qua = []

        self.tao_giao_dien()

    def tao_giao_dien(self):
        # Nhập số lượng phương trình
        tk.Label(self.master, text="Nhập số lượng phương trình:").pack()
        self.nhap_so_phuong_trinh = tk.Entry(self.master)
        self.nhap_so_phuong_trinh.pack()

        # Nút tạo ma trận ô nhập
        self.nut_tao_ma_tran = tk.Button(self.master, text="Tạo phương trình", command=self.tao_o_nhap_phuong_trinh)
        self.nut_tao_ma_tran.pack()

        # Nút giải hệ phương trình
        self.nut_giai = tk.Button(self.master, text="Giải hệ phương trình", command=self.giai_he_phuong_trinh, state=tk.DISABLED)  # Vô hiệu hóa ban đầu
        self.nut_giai.pack()

        # Nút xóa toàn bộ dữ liệu
        self.nut_xoa = tk.Button(self.master, text="Xóa Dữ Liệu", command=self.xoa_toan_bo, state=tk.DISABLED)  # Vô hiệu hóa ban đầu
        self.nut_xoa.pack()

        # Khung chứa các ô nhập phương trình (được tạo động)
        self.khung_phuong_trinh = tk.Frame(self.master)
        self.khung_phuong_trinh.pack()

        # Nhãn hiển thị kết quả
        self.nhan_ket_qua = tk.Label(self.master, text="")
        self.nhan_ket_qua.pack()

    def tao_o_nhap_phuong_trinh(self):
        try:
            self.so_phuong_trinh = int(self.nhap_so_phuong_trinh.get())
            if self.so_phuong_trinh <= 0:
                raise ValueError("Số lượng phương trình phải lớn hơn 0.")

            self.xoa_toan_bo()  # Xóa các mục nhập trước đó
            self.nut_giai.config(state=tk.NORMAL)  # Kích hoạt nút giải
            self.nut_xoa.config(state=tk.NORMAL)  # Kích hoạt nút xóa

            for i in range(self.so_phuong_trinh):
                khung_dong = tk.Frame(self.khung_phuong_trinh)
                khung_dong.pack()
                he_so_dong = []
                for j in range(self.so_phuong_trinh):
                    o_nhap = tk.Entry(khung_dong, width=5)
                    o_nhap.pack(side=tk.LEFT)
                    he_so_dong.append(o_nhap)
                    if j < self.so_phuong_trinh - 1:
                        tk.Label(khung_dong, text=f"x{j+1} +").pack(side=tk.LEFT)
                    else:
                        tk.Label(khung_dong, text=f"x{j+1}").pack(side=tk.LEFT)

                tk.Label(khung_dong, text=" = ").pack(side=tk.LEFT)
                o_nhap_ket_qua = tk.Entry(khung_dong, width=5)
                o_nhap_ket_qua.pack(side=tk.LEFT)
                self.he_so.append(he_so_dong)
                self.ket_qua.append(o_nhap_ket_qua)

        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    def xoa_toan_bo(self):
        for widget in self.khung_phuong_trinh.winfo_children():
            widget.destroy()
        self.he_so.clear()
        self.ket_qua.clear()
        self.nhan_ket_qua.config(text="")
        self.nut_giai.config(state=tk.DISABLED)  # Vô hiệu hóa nút giải
        self.nut_xoa.config(state=tk.DISABLED)  # Vô hiệu hóa nút xóa


    def giai_he_phuong_trinh(self):
        try:
            A = []
            B = []
            for he_so_dong, o_nhap_ket_qua in zip(self.he_so, self.ket_qua):
                A.append([float(o_nhap.get()) for o_nhap in he_so_dong])
                B.append(float(o_nhap_ket_qua.get()))

            A = np.array(A)
            B = np.array(B).reshape(-1, 1)  # Đảm bảo B là vector cột

            # Tạo ma trận mở rộng
            mo_rong = np.concatenate((A, B), axis=1)

            hang_A = np.linalg.matrix_rank(A)
            hang_mo_rong = np.linalg.matrix_rank(mo_rong)

            if hang_A < hang_mo_rong:
                self.nhan_ket_qua.config(text="Hệ phương trình vô nghiệm.")
            elif hang_A < A.shape[1]:
                self.nhan_ket_qua.config(text="Hệ phương trình có vô số nghiệm.")
            else:  # hang_A == hang_mo_rong == so_an
                nghiem = np.linalg.solve(A, B)
                ket_qua_text = ", ".join([f"x{i+1} = {x:.2f}" for i, x in enumerate(nghiem.flatten())]) # flatten để xử lý vector cột
                self.nhan_ket_qua.config(text=ket_qua_text)

        except ValueError as e:
            messagebox.showerror("Lỗi", f"Dữ liệu không hợp lệ: {e}")
        except np.linalg.LinAlgError as e:
            messagebox.showerror("Lỗi", f"Không thể giải hệ phương trình: {e}")



root = tk.Tk()
ung_dung = UngDungGiaiPhuongTrinh(root)
root.mainloop()