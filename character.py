# import pygame
# from config import SCREEN_WIDTH, SCREEN_HEIGHT

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill((255, 0, 0))  # Màu đỏ cho nhân vật
#         self.rect = self.image.get_rect()
#         self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

#     def update(self, head_y):
#         if head_y is not None:
#             # Cập nhật vị trí y của nhân vật dựa trên vị trí đầu được phát hiện
#             self.rect.centery = head_y

#         # Giới hạn nhân vật trong màn hình
#         if self.rect.top < 0:
#             self.rect.top = 0
#         if self.rect.bottom > SCREEN_HEIGHT:
#             self.rect.bottom = SCREEN_HEIGHT
#             # Chuẩn hóa vị trí Y về
#             normalized_y = int((center_y / self.frame_height) * SCREEN_HEIGHT)
#             return normalized_y
#             if self.rect.bottom > SCREEN_HEIGHT:
#                 self.rect.bottom = SCREEN_HEIGHT
        
#         return normalized_y

import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Nếu chưa có hình ảnh, dùng hình vuông đơn giản
        # BẠN CÓ THỂ THAY THẾ BẰNG HÌNH ẢNH CỦA CHIM
        self.image = pygame.Surface([40, 40]) 
        self.image.fill((255, 255, 0)) # Màu vàng
        # self.image = pygame.image.load('bird.png').convert_alpha() # Khi có hình ảnh
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 4  # Vị trí X cố định
        self.rect.y = SCREEN_HEIGHT // 2 # Vị trí Y ban đầu
        
    def move_to_y(self, normalized_y):
        """Di chuyển nhân vật đến tọa độ Y đã chuẩn hóa từ webcam."""
        if normalized_y is not None:
            # Ngăn nhân vật đi ra ngoài biên màn hình (trên và dưới)
            if normalized_y < 0:
                normalized_y = 0
            if normalized_y > SCREEN_HEIGHT - self.rect.height:
                normalized_y = SCREEN_HEIGHT - self.rect.height
                    
            # Cập nhật vị trí Y
            self.rect.y = normalized_y
        
    def update(self):
        # Trong phiên bản này, chim không tự rơi bằng trọng lực, 
        # mà hoàn toàn di chuyển theo đầu người chơi. 
        # Nếu muốn thêm tính năng rơi nhẹ, bạn có thể thêm logic trọng lực tại đây.
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)