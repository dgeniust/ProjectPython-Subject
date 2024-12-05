import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFilter, ImageTk
import os

# Hàm làm mờ ảnh
def blur_image(image):
    return image.filter(ImageFilter.GaussianBlur(radius=5))

# Hàm làm sắc nét ảnh
def sharpen_image(image):
    return image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

# Hàm chuyển ảnh sang đen trắng
def convert_to_bw(image):
    return image.convert("L")

# Hàm cắt ảnh
def crop_image(image, left, top, right, bottom):
    return image.crop((left, top, right, bottom))

# Hàm resize ảnh
def resize_image(image, width, height):
    return image.resize((width, height))

# Hàm tải ảnh từ máy tính
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        try:
            image = Image.open(file_path)
            return image
        except Exception as e:
            messagebox.showerror("Error", f"Không thể mở ảnh: {str(e)}")
            return None
    return None

# Hàm lưu ảnh sau khi xử lý
def save_image(image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
    if file_path:
        try:
            image.save(file_path)
            messagebox.showinfo("Success", "Ảnh đã được lưu thành công!")
        except Exception as e:
            messagebox.showerror("Error", f"Không thể lưu ảnh: {str(e)}")

# Giao diện người dùng GUI
class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("G213NTD_CV")
        self.image = None
        self.original_image = None
        # Set up the GUI components
        self.create_widgets()
    def create_widgets(self):
        # Load image button
        # Nút tải ảnh
        self.load_button = tk.Button(root, text="Tải ảnh", command=self.load_image)
        self.load_button.pack(pady=10)
        
        # Nút lưu ảnh
        self.save_button = tk.Button(root, text="Lưu ảnh", command=self.save_image)
        self.save_button.pack(pady=10)
        
        # Nút làm mờ ảnh
        self.blur_button = tk.Button(root, text="Làm mờ ảnh", command=self.blur_image)
        self.blur_button.pack(pady=5)
        
        # Nút làm sắc nét ảnh
        self.sharpen_button = tk.Button(root, text="Làm sắc nét ảnh", command=self.sharpen_image)
        self.sharpen_button.pack(pady=5)
        
        # Nút chuyển sang đen trắng
        self.bw_button = tk.Button(root, text="Chuyển sang đen trắng", command=self.convert_to_bw)
        self.bw_button.pack(pady=5)
        
        # Nút cắt ảnh
        self.crop_button = tk.Button(root, text="Cắt ảnh", command=self.crop_image)
        self.crop_button.pack(pady=5)
        
        # Nút resize ảnh
        self.resize_button = tk.Button(root, text="Resize ảnh", command=self.resize_image)
        self.resize_button.pack(pady=5)
        
        # Label để hiển thị ảnh
        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)
        

    def load_image(self):
        self.image = load_image()
        if self.image:
            self.original_image = self.image.copy()
            self.update_image_display()

    def save_image(self):
        if self.image:
            save_image(self.image)
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để lưu!")

    def blur_image(self):
        if self.image:
            self.image = blur_image(self.image)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để làm mờ!")

    def sharpen_image(self):
        if self.image:
            self.image = sharpen_image(self.image)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để làm sắc nét!")

    def convert_to_bw(self):
        if self.image:
            self.image = convert_to_bw(self.image)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để chuyển sang đen trắng!")

    def crop_image(self):
        if self.image:
            # Bạn có thể cho phép người dùng nhập kích thước cắt tại đây
            left = 50
            top = 50
            right = self.image.width - 50
            bottom = self.image.height - 50
            self.image = crop_image(self.image, left, top, right, bottom)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để cắt!")

    def resize_image(self):
        if self.image:
            # Cho phép người dùng nhập chiều rộng và chiều cao mới
            width = 300
            height = 300
            self.image = resize_image(self.image, width, height)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để resize!")

    def update_image_display(self):
        if self.image:
            # Chuyển đổi ảnh từ PIL Image sang định dạng mà tkinter có thể hiển thị
            img_tk = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Lưu tham chiếu đến ảnh để tránh bị garbage collection

# Tạo cửa sổ chính của ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
