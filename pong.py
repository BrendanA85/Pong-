import pygame

pygame.init()
running = True
WINDOW_WIDTH = 800
WINDOW_HEGIHT = 590
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEGIHT))

clock = pygame.time.Clock()

score_right = 0
score_left = 0

font = pygame.font.Font(None, 68)

paddle = pygame.Surface((25,90))
paddle.fill((255,255,255))
paddle_rectangle  = paddle.get_rect()
paddle_rectangle.center = (20,WINDOW_HEGIHT//2)
paddle_speed = 30

right_paddle = pygame.Surface((25,90))
right_paddle.fill((255,255,255))
right_paddle_rectangle = right_paddle.get_rect()
right_paddle_rectangle.center = (780,WINDOW_HEGIHT//2) 

ball = pygame.Surface((30,30))
ball.fill((0,0,255))
ball_rectangle = pygame.draw.circle(ball, (255,255,255), (15,15),15)
ball_rectangle.center = (WINDOW_WIDTH//2,WINDOW_HEGIHT//2)
ball_direction = -1
ball_y_axis = -1

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and paddle_rectangle.top>0:
                paddle_rectangle.move_ip(0,(-paddle_speed))
            if event.key == pygame.K_s and paddle_rectangle.bottom<WINDOW_HEGIHT:
                paddle_rectangle.move_ip(0,paddle_speed)
            if event.key == pygame.K_p and right_paddle_rectangle.top>0:
                right_paddle_rectangle.move_ip(0,(-paddle_speed))
            if event.key == pygame.K_SEMICOLON and right_paddle_rectangle.bottom<WINDOW_HEGIHT:
                right_paddle_rectangle.move_ip(0,paddle_speed)
    ball_rectangle.move_ip(2*ball_direction,1*ball_y_axis)
    if ball_rectangle.top <= 0 or ball_rectangle.bottom >= WINDOW_HEGIHT:
        ball_y_axis*=-1
    if ball_rectangle.colliderect(paddle_rectangle):
        ball_direction*=-1
    if ball_rectangle.colliderect(right_paddle_rectangle):
        ball_direction*=-1
    if ball_rectangle.right>= 800:
        ball_rectangle.center = (WINDOW_WIDTH//2,WINDOW_HEGIHT//2)
        score_left += 1
    if ball_rectangle.left<=0:
        ball_rectangle.center = (WINDOW_WIDTH//2,WINDOW_HEGIHT//2)
        score_right+=1
    left_score_text = font.render(str(score_left),True,(255,255,255))
    right_score_text = font.render(str(score_right),True,(255,255,255))
    window.fill((0,0,255))
    window.blit(right_score_text, (WINDOW_WIDTH//2+80,15))
    window.blit(left_score_text, (WINDOW_WIDTH//2-100,15))
    window.blit(paddle, paddle_rectangle)
    window.blit(right_paddle,right_paddle_rectangle)
    window.blit (ball, ball_rectangle)
    pygame.display.update()
pygame.quit()