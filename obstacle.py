import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_WIDTH, PIPE_GAP, GAME_SPEED

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x_pos):
        super().__init__()
        self.gap_start_y = random.randint(50, SCREEN_HEIGHT - 50 - PIPE_GAP)
        self.x = x_pos
        self.passed = False # Cờ để tính điểm

        # Tạo ống trên (Top Pipe)
        self.top_height = self.gap_start_y
        self.top_pipe = pygame.Surface([PIPE_WIDTH, self.top_height])
        self.top_pipe.fill((0, 255, 0)) # Màu xanh lá cây
        self.top_rect = self.top_pipe.get_rect(topleft=(self.x, 0))

        # Tạo ống dưới (Bottom Pipe)
        self.bottom_height = SCREEN_HEIGHT - (self.gap_start_y + PIPE_GAP)
        self.bottom_pipe = pygame.Surface([PIPE_WIDTH, self.bottom_height])
        self.bottom_pipe.fill((0, 255, 0)) # Màu xanh lá cây
        self.bottom_rect = self.bottom_pipe.get_rect(topleft=(self.x, self.gap_start_y + PIPE_GAP))

    def update(self):
        # Di chuyển ống sang trái
        self.x -= GAME_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        # Vẽ ống trên và ống dưới
        screen.blit(self.top_pipe, self.top_rect)
        screen.blit(self.bottom_pipe, self.bottom_rect)

    def is_off_screen(self):
        # Kiểm tra nếu ống đã ra khỏi màn hình
        return self.x + PIPE_WIDTH < 0

    def get_rects(self):
        # Trả về cả hai rect để kiểm tra va chạm
        return self.top_rect, self.bottom_rect