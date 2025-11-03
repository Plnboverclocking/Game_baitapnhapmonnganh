import pygame
import sys
import time
from config import *
from character import Player
from obstacle import Pipe
from vision import HeadDetector # Thêm import HeadDetector
import cv2 # Cần cho cv2.waitKey

def draw_score(screen, score):
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 20))

def run_game():
    pygame.init()
    pygame.font.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    
    # Khởi tạo các đối tượng
    player = Player()
    detector = HeadDetector()
    
    # Danh sách chướng ngại vật
    pipes = []
    
    # Biến trạng thái game
    score = 0
    game_over = False
    
    # Tạo ống đầu tiên
    time_since_last_pipe = 0
    pipe_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(pipe_timer, PIPE_FREQUENCY)

    # Vòng lặp chính của Game
    running = True
    while running:
        # --- Xử lý sự kiện (Input) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Tạo ống mới theo timer
            if event.type == pipe_timer and not game_over:
                pipes.append(Pipe(SCREEN_WIDTH))

        # --- Cập nhật Logic Game ---
        if not game_over:
            # 1. Cập nhật vị trí nhân vật từ Webcam
            normalized_y, frame = detector.get_head_y()
            player.move_to_y(normalized_y)

            # 2. Cập nhật chướng ngại vật
            player.update()
            
            pipes_to_remove = []
            for pipe in pipes:
                pipe.update()
                
                # Kiểm tra điểm
                if pipe.top_rect.right < player.rect.left and not pipe.passed:
                    score += 1
                    pipe.passed = True
                    
                # Kiểm tra nếu ống đã ra khỏi màn hình
                if pipe.is_off_screen():
                    pipes_to_remove.append(pipe)
                    
                # 3. Kiểm tra Va chạm (Collision)
                top_rect, bottom_rect = pipe.get_rects()
                if player.rect.colliderect(top_rect) or player.rect.colliderect(bottom_rect):
                    game_over = True
            
            # Xóa các ống đã ra khỏi màn hình
            for pipe in pipes_to_remove:
                pipes.remove(pipe)

            # Kiểm tra va chạm với biên trên/dưới
            if player.rect.bottom > SCREEN_HEIGHT or player.rect.top < 0:
                game_over = True
        
        # --- Vẽ (Draw) ---
        screen.fill(BACKGROUND_COLOR) # Vẽ nền
        
        # Vẽ các ống
        for pipe in pipes:
            pipe.draw(screen)
            
        # Vẽ người chơi
        player.draw(screen)
        
        # Vẽ điểm số
        draw_score(screen, score)

        # --- Game Over Screen ---
        if game_over:
            font = pygame.font.Font(None, 100)
            text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
            
            # Dừng timer tạo ống
            pygame.time.set_timer(pipe_timer, 0)
            
            # Đóng camera feed sau khi game over
            cv2.destroyWindow('Camera Feed (Head Detection)')

        # Cập nhật màn hình và kiểm soát FPS
        pygame.display.flip()
        clock.tick(FPS)
        
        # Cần thiết để OpenCV hiển thị frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False

    # Dọn dẹp
    detector.release()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()