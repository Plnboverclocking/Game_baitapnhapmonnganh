# import cv2
# from config import SCREEN_HEIGHT, CAMERA_SOURCE

# class HeadDetector:
#     def __init__(self):
#         # Load pre-trained Haar Cascade classifier for face detection
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         # Initialize video capture from the specified camera source
#         self.cap = cv2.VideoCapture(CAMERA_SOURCE)

#     def get_head_position(self):
#         ret, frame = self.cap.read()
#         if not ret:
#             return None  # Return None if frame is not captured

#         # Convert the frame to grayscale for face detection
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # Detect faces in the frame
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#         if len(faces) == 0:
#             return None  # No faces detected

#         # Assume the first detected face is the player's head
#         (x, y, w, h) = faces[0]
#         head_center_y = y + h // 2

#         # Normalize the head position to a value between 0 and SCREEN_HEIGHT
#         normalized_position = int((head_center_y / frame.shape[0]) * SCREEN_HEIGHT)
#         return normalized_position

#     def release(self):
#         self.cap.release()

import cv2
from config import SCREEN_HEIGHT, CAMERA_SOURCE

class HeadDetector:
    def __init__(self):
        # Khởi tạo Video Capture (kết nối với iVCam)
        self.cap = cv2.VideoCapture(CAMERA_SOURCE)
        if not self.cap.isOpened():
            print(f"Lỗi: Không thể kết nối với camera nguồn: {CAMERA_SOURCE}")
            # Thử lại với nguồn mặc định 0 nếu CAMERA_SOURCE không phải là 0
            if CAMERA_SOURCE != 0:
                 self.cap = cv2.VideoCapture(0)
                 if not self.cap.isOpened():
                     exit()
            else:
                exit()
        
        # Tải Haar Cascade cho khuôn mặt (sử dụng khuôn mặt thay cho đầu)
        # File haarcascade_frontalface_default.xml phải có sẵn trong thư mục
        # hoặc đường dẫn hệ thống của OpenCV
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        # Kích thước khung hình camera
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        print(f"Đã kết nối camera với kích thước: {self.frame_width}x{self.frame_height}")

    def get_head_y(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Lỗi: Không thể đọc frame từ camera.")
            return None, None

        # Lật khung hình (frame) để hành động của người chơi tự nhiên hơn
        frame = cv2.flip(frame, 1)
        
        # Chuyển sang ảnh xám để nhận diện nhanh hơn
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Phát hiện khuôn mặt
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        # Vẽ và xử lý kết quả
        normalized_y = None
        
        for (x, y, w, h) in faces:
            # Vẽ hình chữ nhật quanh khuôn mặt để hiển thị (Debug)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Tính toán tâm Y của khuôn mặt
            center_y = y + h // 2
            
            # Chuẩn hóa tọa độ Y: Chuyển từ tọa độ webcam sang tọa độ màn hình game
            # Nếu khuôn mặt càng lên cao (y nhỏ) thì nhân vật trong game cũng lên cao (y nhỏ).
            # Công thức chuẩn hóa:
            normalized_y = int(center_y * SCREEN_HEIGHT / self.frame_height)
            
            # Chỉ xử lý khuôn mặt đầu tiên tìm thấy
            break 
            
        # Hiển thị frame
        cv2.imshow('Camera Feed (Head Detection)', frame)
        
        return normalized_y, frame # normalized_y là tọa độ y mới của chim

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

# LƯU Ý QUAN TRỌNG:
# Để sử dụng Haar Cascade, bạn cần đảm bảo file 'haarcascade_frontalface_default.xml' 
# có sẵn. Nó thường được cài đặt sẵn cùng với opencv-python.