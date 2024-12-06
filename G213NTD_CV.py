import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter

# Hàm làm mờ ảnh
def blur_image_G213NTD(image):
    return image.filter(ImageFilter.GaussianBlur(radius=5))

# Hàm làm sắc nét ảnh
def sharpen_image_G213NTD(image):
    return image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

# Hàm chuyển ảnh sang đen trắng
def convert_to_bw_G213NTD(image):
    return image.convert("L")

# Hàm cắt ảnh
def crop_image_G213NTD(image, left, top, right, bottom):
    return image.crop((left, top, right, bottom))

# Hàm resize ảnh
def resize_image_G213NTD(image, width, height):
    return image.resize((width, height))

# Hàm tải ảnh từ máy tính
def load_image_G213NTD():
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
def save_image_G213NTD(image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
    if file_path:
        try:
            image.save(file_path)
            messagebox.showinfo("Success", "Ảnh đã được lưu thành công!")
        except Exception as e:
            messagebox.showerror("Error", f"Không thể lưu ảnh: {str(e)}")

class VideoFrameExtractorApp_G213NTD:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Frame Extractor-G213NTD")
        self.root.geometry("1920x1080")

        # Video path và image path
        self.video_path = None
        self.current_image = None

        # Tạo các widget cho GUI
        self.create_widgets()

    def create_widgets(self):
        # Nút chọn video
        self.select_button = tk.Button(self.root, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=20)

        # Label hiển thị video path
        self.video_label = tk.Label(self.root, text="No video selected", wraplength=400)
        self.video_label.pack(pady=10)

        # Nút trích xuất frame
        self.extract_button = tk.Button(self.root, text="Extract Frames", state=tk.DISABLED, command=self.extract_frames)
        self.extract_button.pack(pady=20)

        # Nút tải ảnh
        self.load_button = tk.Button(self.root, text="Tải ảnh", command=self.load_image_G213NTD)
        self.load_button.pack(pady=10)

        # Nút lưu ảnh
        self.save_button = tk.Button(self.root, text="Lưu ảnh", state=tk.DISABLED, command=self.save_image_G213NTD)
        self.save_button.pack(pady=10)

        # Nút làm mờ ảnh
        self.blur_button = tk.Button(self.root, text="Làm mờ ảnh", state=tk.DISABLED, command=self.blur_image_G213NTD)
        self.blur_button.pack(pady=5)

        # Nút làm sắc nét ảnh
        self.sharpen_button = tk.Button(self.root, text="Làm sắc nét ảnh", state=tk.DISABLED, command=self.sharpen_image_G213NTD)
        self.sharpen_button.pack(pady=5)

        # Nút chuyển sang đen trắng
        self.bw_button = tk.Button(self.root, text="Chuyển sang đen trắng", state=tk.DISABLED, command=self.convert_to_bw_G213NTD)
        self.bw_button.pack(pady=5)

        # Nút cắt ảnh
        self.crop_button = tk.Button(self.root, text="Cắt ảnh", state=tk.DISABLED, command=self.crop_image_G213NTD)
        self.crop_button.pack(pady=5)

        # Nút resize ảnh
        self.resize_button = tk.Button(self.root, text="Resize ảnh", state=tk.DISABLED, command=self.resize_image_G213NTD)
        self.resize_button.pack(pady=5)

        # Status label
        self.status_label = tk.Label(self.root, text="Ready to extract frames.", wraplength=400)
        self.status_label.pack(pady=10)

        # Label để hiển thị ảnh
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)
        # Tạo khung để hiển thị ảnh
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=20)

        # Các label để hiển thị ảnh
        self.original_image_label = tk.Label(self.image_frame)
        self.original_image_label.grid(row=0, column=0, padx=10, pady=10)

        self.blur_image_label = tk.Label(self.image_frame)
        self.blur_image_label.grid(row=0, column=1, padx=10, pady=10)

        self.bw_image_label = tk.Label(self.image_frame)
        self.bw_image_label.grid(row=0, column=2, padx=10, pady=10)

        self.sharpen_image_label = tk.Label(self.image_frame)
        self.sharpen_image_label.grid(row=1, column=0, padx=10, pady=10)

        self.resized_image_label = tk.Label(self.image_frame)
        self.resized_image_label.grid(row=1, column=1, padx=10, pady=10)

    def load_image_G213NTD(self):
        self.current_image = load_image_G213NTD()
        if self.current_image:
            self.update_image_display()
            # Kích hoạt các nút chỉnh sửa ảnh
            self.save_button.config(state=tk.NORMAL)
            self.blur_button.config(state=tk.NORMAL)
            self.sharpen_button.config(state=tk.NORMAL)
            self.bw_button.config(state=tk.NORMAL)
            self.crop_button.config(state=tk.NORMAL)
            self.resize_button.config(state=tk.NORMAL)

    def select_video(self):
        # Mở cửa sổ chọn file video
        self.video_path = filedialog.askopenfilename(title="Select Video", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])

        # Hiển thị đường dẫn video
        if self.video_path:
            self.video_label.config(text=f"Selected Video: {self.video_path}")
            self.extract_button.config(state=tk.NORMAL)  # Kích hoạt nút trích xuất frame
        else:
            self.video_label.config(text="No video selected")

    def extract_frames(self):
        # Kiểm tra nếu không chọn video
        if not self.video_path:
            messagebox.showerror("Error", "Please select a video first!")
            return

        # Tạo thư mục lưu các frame
        output_folder = "frames"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Mở video
        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            messagebox.showerror("Error", "Failed to open video.")
            return

        # Trích xuất frame
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Lưu từng frame dưới dạng ảnh
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            frame_count += 1

        cap.release()

        # Hiển thị thông báo hoàn tất
        self.status_label.config(text=f"Extracted {frame_count} frames successfully.")
        messagebox.showinfo("Success", f"{frame_count} frames extracted and saved to '{output_folder}'.")

    def save_image_G213NTD(self):
        if self.current_image:
            save_image_G213NTD(self.current_image)
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để lưu!")

    def blur_image_G213NTD(self):
        if self.current_image:
            self.current_image = blur_image_G213NTD(self.current_image)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để làm mờ!")

    def sharpen_image_G213NTD(self):
        if self.current_image:
            self.current_image = sharpen_image_G213NTD(self.current_image)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để làm sắc nét!")

    def convert_to_bw_G213NTD(self):
        if self.current_image:
            self.current_image = convert_to_bw_G213NTD(self.current_image)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để chuyển sang đen trắng!")

    def crop_image_G213NTD(self):
        if self.current_image:
            # Cắt ảnh (mặc định: cắt từ 50, 50 tới 250, 250)
            left = 50
            top = 50
            right = self.current_image.width - 50
            bottom = self.current_image.height - 50
            self.current_image = crop_image_G213NTD(self.current_image, left, top, right, bottom)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để cắt!")

    def resize_image_G213NTD(self):
        if self.current_image:
            # Resize ảnh (mặc định: 300x300)
            width = 300
            height = 300
            self.current_image = resize_image_G213NTD(self.current_image, width, height)
            self.update_image_display()
        else:
            messagebox.showwarning("Warning", "Chưa có ảnh để resize!")

    def update_image_display(self):
        if self.current_image:
            # Chuyển đổi ảnh từ PIL Image sang định dạng mà tkinter có thể hiển thị
            img_tk = ImageTk.PhotoImage(self.current_image)
            self.original_image_label.config(image=img_tk)
            self.original_image_label.image = img_tk

            # Cập nhật các ảnh đã chỉnh sửa
            blurred_img = blur_image_G213NTD(self.current_image)
            blur_img_tk = ImageTk.PhotoImage(blurred_img)
            self.blur_image_label.config(image=blur_img_tk)
            self.blur_image_label.image = blur_img_tk

            bw_img = convert_to_bw_G213NTD(self.current_image)
            bw_img_tk = ImageTk.PhotoImage(bw_img)
            self.bw_image_label.config(image=bw_img_tk)
            self.bw_image_label.image = bw_img_tk

            sharpened_img = sharpen_image_G213NTD(self.current_image)
            sharpen_img_tk = ImageTk.PhotoImage(sharpened_img)
            self.sharpen_image_label.config(image=sharpen_img_tk)
            self.sharpen_image_label.image = sharpen_img_tk

            resized_img = resize_image_G213NTD(self.current_image, 300, 300)
            resized_img_tk = ImageTk.PhotoImage(resized_img)
            self.resized_image_label.config(image=resized_img_tk)
            self.resized_image_label.image = resized_img_tk
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoFrameExtractorApp_G213NTD(root)
    root.mainloop()
