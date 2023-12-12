import tkinter as tk
from PIL import Image, ImageTk
import cv2
import time
import os

class FaceRecognitionApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", self.video_source)

        self.canvas = tk.Label(window)
        self.canvas.pack()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.last_capture_time = time.time()
        self.capture_interval = 0.05  # 0.1초 간격
        self.img_dir = 'captured_faces'  # 촬영된 얼굴을 저장할 디렉토리
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)
        self.update()
        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.display_frame(frame)
        self.window.after(10, self.update)

    def display_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            expression = "Happy" if w * h > 50000 else "Neutral"
            cv2.putText(frame, expression, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # 촬영 간격 확인 및 얼굴 촬영
            if time.time() - self.last_capture_time > self.capture_interval:
                face_img = frame[y:y + h, x:x + w]
                self.capture_face(face_img)
                self.last_capture_time = time.time()

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.canvas.imgtk = imgtk
        self.canvas.configure(image=imgtk)

    def capture_face(self, face_img):
        timestamp = int(time.time())
        filename = f"{self.img_dir}/face_{timestamp}.png"
        cv2.imwrite(filename, face_img)


if __name__ == '__main__':
    root = tk.Tk()
    app = FaceRecognitionApp(root, "Face Recognition")