import pygame
import time
import random
import sys
pygame.init()
class Rect():
    def __init__(self, x, y, width , height, font_size, frame_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.frame_size = frame_size
        self.name = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(None, self.font_size)
    def painter(self, color, frame_color):
            pygame.draw.rect(window, color, self.name)
            pygame.draw.rect(window, frame_color, self.name, self.frame_size)
    def show_text(self, x_shift, y_shift, text = 'CLICK'):
        text = self.font.render(text, True, text_color)
        window.blit(text, (self.x + x_shift, self.y + y_shift))
#Цвета
card_color = (204, 51, 153)
background = (26, 26, 255)
frame_color = (102, 255, 51)
text_color = (230, 230, 0)
green = (51, 204, 51)
red = (255, 51, 0)
grey = (128, 128, 128)
#Переменные
amount_card = 0
complexity_choice = -10
play_again_choice = 0
points = 0
timer = 0
amount_cards = 0
x = 20
y = 150
time_wait = 0
wait_complexity = 0
wait = wait_complexity


choice_cards = list()
window = pygame.display.set_mode((500 , 500))
window.fill(background)

fps = pygame.time.Clock()
easy_choice = Rect(180, 100, 150 , 35, 30, 5)
normal_choice = Rect(180, 200, 150 , 35, 30, 5)

hard_choice = Rect(180, 300, 150 , 35, 30, 5)
impossible_choice = Rect(180, 400, 150 , 35, 30, 5)
choice_cards.append(easy_choice)
choice_cards.append(normal_choice)
choice_cards.append(hard_choice)
choice_cards.append(impossible_choice)
counter_text = Rect(0, 0, 70, 80, 28, 5)
counter = Rect(240, 0, 70, 80, 28, 5)
points_text = Rect(0, 40, 70, 80, 28, 5)
points_counter = Rect(150, 40, 70, 80, 28, 5)
play_again_rect = Rect(100, 240 , 100, 40, 40, 5)
exit_game = Rect(250, 240, 100, 40 , 40, 5)
play = True
choice = True
continue_playing = True

play_again = [play_again_rect, exit_game]

pygame.display.set_caption('Clicker By DLNATE')
lose_or_win =  pygame.font.Font(None, 60)
lose_txt = lose_or_win.render('Game over!', True, text_color)
win_txt = lose_or_win.render('Ты победил!', True, text_color)
def create_cards(amount_cards, x, y):
    x = 20
    y = 150
    for i in range(amount_cards):
        rect = Rect(x, y, 70, 80, 28, 5)
        cards.append(rect)  
        x += 100
        if  i % 5 == 0 and i != 0:
            x = 20
            y += 100
while continue_playing == True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()
    window.fill(background)
    points_text.painter(background, background)
    counter_text.painter(background, background)
    counter_text.show_text(10, 10, 'ВРЕМЕНИ ОСТАЛОСЬ:')
    points_text.show_text(10, 10, 'ВАШИ ОЧКИ:')
    easy_choice.painter(card_color, frame_color)
    easy_choice.show_text(10, 10, 'Легкая')
    normal_choice.painter(card_color, frame_color)
    normal_choice.show_text(10, 10, 'Нормальная')
    hard_choice.painter(card_color, frame_color)
    hard_choice.show_text(10, 10, 'Сложная')
    impossible_choice.painter(card_color, frame_color)
    impossible_choice.show_text(10, 10, 'Невозможная')
    while choice == True:
        play_again_choice = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_pos, y_pos = event.pos
                for i in range(4):
                    if choice_cards[i].name.collidepoint(x_pos, y_pos):
                        choice_cards[i].painter(grey, grey)
                        pygame.display.update()
                        time.sleep(0.5)
                        window.fill(background)
                        choice = False
                        complexity_choice = i
                        play = True
        pygame.display.update()
        fps.tick(60)
    if complexity_choice == 0:
        amount_cards = 5
        timer = 20
        wait_complexity = 30
    elif complexity_choice == 1:
        amount_cards = 11 
        timer = 15
        wait_complexity = 25
    elif complexity_choice == 2:
        amount_cards = 16
        timer = 15
        wait_complexity = 25
    elif complexity_choice == 3:
        amount_cards = 16
        timer = 15
        wait_complexity = 20
    cards = list()
    create_cards(amount_cards, x, y)
    counter_text.show_text(10, 10, 'ВРЕМЕНИ ОСТАЛОСЬ:')
    points_text.show_text(10, 10, 'ВАШИ ОЧКИ:')
    while play == True:
        points_str = str(points)
        time_str = str(timer)
        points_counter.painter(background, background)
        points_counter.show_text(0, 10, points_str)
        counter.painter(background, background)
        counter.show_text(0, 10, time_str)
        time_wait += 1
        if timer != 0 and points != 5:
            if time_wait == 60:
                timer -= 1
                time_wait = 0      
            if wait == 0:
                where_will_title = random.randint(0,len(cards) - 1)
                for i in range(amount_cards):
                    cards[i].painter(card_color, frame_color)
                cards[where_will_title].show_text(6, 30)
                wait = wait_complexity
            else:
                wait -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y = event.pos
                    for i in range(amount_cards):
                        if cards[i].name.collidepoint(x,y):
                            if where_will_title == i:
                                cards[i].painter(green, frame_color)
                                points += 1
                            else:
                                cards[i].painter(red, frame_color)
                                points -= 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        sys.exit()
            fps.tick(60)
        if timer == 0:
            window.fill(background)
            window.blit(lose_txt, (125, 250))
            pygame.display.update()
            time.sleep(2)
            window.fill(background)
            pygame.display.update()
            play_again_rect.show_text(-25, -50, 'Хотите ли вы играть снова?')
            while play_again_choice == 0:
                play_again_rect.painter(card_color, frame_color)
                play_again_rect.show_text(20, 5, 'Да')
                exit_game.painter(card_color, frame_color)
                exit_game.show_text(20, 5, 'Нет')
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x_pos,y_pos = event.pos
                        for i in range(2):
                            if play_again[i].name.collidepoint(x_pos, y_pos):
                                play_again[i].painter(grey, grey)
                                pygame.display.update()
                                time.sleep(0.3)
                                if play_again[i] == play_again_rect:
                                    choice = True
                                    play = False
                                    points = 0
                                    window.fill(background)
                                    pygame.display.update()
                                    timer = 2
                                    play_again_choice = 1
                                else:
                                    sys.exit()
            pygame.display.update()
        elif points == 5:
            window.fill(background)
            window.blit(win_txt, (125, 250))
            pygame.display.update()
            time.sleep(2)
            window.fill(background)
            pygame.display.update()
            play_again_rect.show_text(-25, -50, 'Хотите ли вы играть снова?')
            while play_again_choice == 0:
                play_again_rect.painter(card_color, frame_color)
                play_again_rect.show_text(20, 5, 'Да')
                exit_game.painter(card_color, frame_color)
                exit_game.show_text(20, 5, 'Нет')
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x_pos,y_pos = event.pos
                        for i in range(2):
                            if play_again[i].name.collidepoint(x_pos, y_pos):
                                play_again[i].painter(grey, grey)
                                pygame.display.update()
                                time.sleep(0.3)
                                if play_again[i] == play_again_rect:
                                    choice = True
                                    play = False
                                    points = 0
                                    window.fill(background)
                                    pygame.display.update()
                                    timer = 2
                                    play_again_choice = 1
                                else:
                                    sys.exit()
        pygame.display.update()
    fps.tick(60)
    pygame.display.update()