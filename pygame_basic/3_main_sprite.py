import pygame

pygame.init()#초기화 하기

#화면 크기
screen_width = 480#가로 
screen_height = 640#세로
screen = pygame.display.set_mode((screen_width,screen_height)) #크기 설정 

#화면 타이틀 설정
pygame.display.set_caption("LIKO Game")#게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users\김리호/Desktop/새 폴더/selfmade/python/pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("C:/Users\김리호/Desktop/새 폴더/selfmade/python/pygame_basic/character.png")
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0] #캐릭터 가로
character_height = character_size[1] #캐릭터 세로
character_x_pos = screen_width / 2 #화면 가로 절반 크기에 위치
character_y_pos = screen_height - character_height #화면 세로크기 가장 아래에


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가? 
            running = False
    screen.blit(background, (0,0)) #왼쪽 위가 0,0
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()
