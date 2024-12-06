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