# Pong Game made using Pygame

# Made By TANAY KAR

import os

import pygame
from pygame.locals import *
from sys import exit
import random

#__game_start__ = input("Start ?") # Only to be used to halt program startup during presentation

pygame.init()
pygame.font.init()
icon = pygame.image.load("Pictures/icon.png")

height = 480
width = 640

screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(icon)

# Sounds
pygame.mixer.music.load("Audio/Background.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("Audio/Hit.wav")


back = pygame.Surface((640, 480))
startback = pygame.image.load("Pictures/splashback.jpg")
startback = pygame.transform.scale(startback, (640, 480))
background = back.convert()
background.fill((0, 0, 0))
bar = pygame.Surface((10, 50))
bar1 = bar.convert()
bar1.fill((0, 0, 255))
bar2 = bar.convert()
bar2.fill((255, 0, 0))
circ_sur = pygame.Surface((15, 15))
circ = pygame.draw.circle(circ_sur, (255, 255, 0), (15 / 2, 15 / 2), 15 / 2)
circle = circ_sur.convert()
circle.set_colorkey((0, 0, 0))
Pause_Back = pygame.image.load("Pictures/PAUSE.png")
Pause_Back.set_alpha(100)
Pause_Back = pygame.transform.scale(Pause_Back, (640, 480))

# some definitions
bar1_x, bar2_x = 10., 620.
bar1_y, bar2_y = 215., 215.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0., 0.
speed_x, speed_y, speed_circ = 200., 200., 240.
bar1_score, bar2_score = 0, 0
# clock and font objects
clock = pygame.time.Clock()

font = pygame.font.Font("Other/Font.TTF", 40)
msg_font = pygame.font.Font("Other/Font.TTF", 30)
abt2_font = pygame.font.Font("Other/Font.TTF", 50)
abt_font = pygame.font.Font("Other/Font.TTF", 20)

# Font
PauseMSG1 = font.render("Game Paused", True, (255, 255, 255))
PauseMSG2 = msg_font.render("Press SPACE to resume", True, (255, 255, 255))
PauseMSG1_rect = PauseMSG1.get_rect(
    center=((width // 2), ((height // 2) - 35)))
PauseMSG2_rect = PauseMSG2.get_rect(
    center=((width // 2), ((height // 2) + 35)))
# -------
About_MSG1 = abt2_font.render("ABOUT", True, (255, 255, 255))
About_MSG1_rect = About_MSG1.get_rect(
    center=((width // 2), ((height // 2) - 86)))
About_MSG2 = abt_font.render("Pong Game", True, (255, 255, 255))
About_MSG2_rect = About_MSG2.get_rect(
    center=((width // 2), ((height // 2) - 38)))
About_MSG3 = abt_font.render("Version - 1.9", True, (255, 255, 255))
About_MSG3_rect = About_MSG3.get_rect(center=((width // 2), ((height // 2))))
About_MSG4 = abt_font.render("Developed by Tanay Kar", True, (255, 255, 255))
About_MSG4_rect = About_MSG4.get_rect(
    center=((width // 2), ((height // 2) + 38)))
About_MSG5 = abt_font.render("Press 'A' to resume game", True, (255, 255, 255))
About_MSG5_rect = About_MSG5.get_rect(
    center=((width // 2), ((height // 2) + 86)))
# -------
Help_MSG1 = abt2_font.render("Help",True,(255,255,255))
Help_MSG1_rect = Help_MSG1.get_rect(center = ((width // 2), ((height // 2) - 86)))
Help_MSG2 = abt_font.render("Press 'SPACE' to pause or resume game", True, (255, 255, 255))
Help_MSG2_rect = Help_MSG2.get_rect(
    center=((width // 2), ((height // 2) - 38)))
Help_MSG3 = abt_font.render("Press 'A' to show about page", True, (255, 255, 255))
Help_MSG3_rect = Help_MSG3.get_rect(center=((width // 2), ((height // 2))))
Help_MSG4 = abt_font.render("Press 'S' to take a screenshot of the game", True, (255, 255, 255))
Help_MSG4_rect = Help_MSG4.get_rect(
    center=((width // 2), ((height // 2) + 38)))
Help_MSG5 = abt_font.render("Press 'R' to restart game", True, (255, 255, 255))
Help_MSG5_rect = Help_MSG5.get_rect(
    center=((width // 2), ((height // 2) + 86)))
Help_MSG6 = abt_font.render("Press 'H' to return", True, (255, 255, 255))
Help_MSG6_rect = Help_MSG6.get_rect(
    center=((width // 2), ((height // 2) + 124)))

# --------

muted = True
pause = False
run = True
start = True



def count_files(path: str) -> int:

    file_entries = os.listdir(path)
    return len(file_entries)



def mute():
    global muted
    if muted is False:

        hit_sound.set_volume(0.0)

        pygame.mixer.music.pause()
    else:
        hit_sound.set_volume(1.0)

        pygame.mixer.music.unpause()


def paused():
    global pause

    screen.blit(Pause_Back, (0, 0))
    screen.blit(PauseMSG1, PauseMSG1_rect)
    screen.blit(PauseMSG2, PauseMSG2_rect)

    while pause:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.init()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_ESCAPE:
                    pause = False
        pygame.display.update()
        clock.tick(30)


def save():

    pygame.time.delay(300)
    print(count_files("Screenshots/"))
    file_name = "Screenshots/Pong_screenshot" + \
        str(count_files("Screenshots/") + 1) + ".png"
    pygame.image.save(screen, file_name)
    clock.tick(30)


def _help():
    global pause

    screen.blit(Pause_Back, (0, 0))
    screen.blit(Pause_Back, (0, 0))
    
    screen.blit(Help_MSG1, Help_MSG1_rect)
    
    screen.blit(Help_MSG2, Help_MSG2_rect)
    
    screen.blit(Help_MSG3, Help_MSG3_rect)
    
    screen.blit(Help_MSG4, Help_MSG4_rect)
    
    screen.blit(Help_MSG5, Help_MSG5_rect)
    
    screen.blit(Help_MSG6, Help_MSG6_rect)
    
    while pause:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.init()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_h:
                    pause = False
        pygame.display.update()
        clock.tick(30)


def about():
    global pause

    screen.blit(Pause_Back, (0, 0))
    screen.blit(About_MSG1, About_MSG1_rect)
    screen.blit(About_MSG2, About_MSG2_rect)
    screen.blit(About_MSG3, About_MSG3_rect)
    screen.blit(About_MSG4, About_MSG4_rect)
    while pause:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.init()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    pause = False
        pygame.display.update()
        clock.tick(30)


def START():
    global start, muted, pause
    while start:
        pygame.display.init()
        screen.blit(startback, (0, 0))
        mute()
        help_info_text = abt_font.render(
            "Press H for help", True, (255, 255, 255))
        screen.blit(help_info_text, (10, 450))
        for event in pygame.event.get():
            if event.type == QUIT:

                pygame.quit()
                start = False
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False
                elif event.key == K_a:
                    pause = True
                    about()
                elif event.key == K_m:
                    muted = not muted
                    mute()
                elif event.key == K_h:
                    pause = True
                    _help()
        clock.tick(30)
        pygame.display.flip()


while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.init()
            pygame.quit()
            run = False
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
            elif event.key == K_SPACE:
                pause = True
                paused()
            elif event.key == K_a:
                pause = True
                about()
            elif event.key == K_s:
                save()
            elif event.key == K_m:
                muted = not muted
                mute()
            elif event.key == K_h:
                pause = True
                _help()
            elif event.key == K_r:
                # restart()
                bar1_score = 0
                bar2_score = 0
                score1 = font.render(str(bar1_score), True, (255, 255, 255))
                score2 = font.render(str(bar2_score), True, (255, 255, 255))
                screen.blit(score1, (250., 210.))
                screen.blit(score2, (380., 210.))
                START()
                continue

        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.
    START()

    info_text = abt_font.render("Press SPACE to pause", True, (255, 255, 255))
    score1 = font.render(str(bar1_score), True, (255, 255, 255))
    score2 = font.render(str(bar2_score), True, (255, 255, 255))

    screen.blit(background, (0, 0))
    frame = pygame.draw.rect(screen, (255, 255, 255),
                             Rect((5, 5), (630, 470)), 2)
    middle_line = pygame.draw.aaline(
        screen, (255, 255, 255), (330, 5), (330, 475))
    screen.blit(bar1, (bar1_x, bar1_y))
    screen.blit(bar2, (bar2_x, bar2_y))
    screen.blit(circle, (circle_x, circle_y))
    screen.blit(info_text, (10, 450))
    screen.blit(score1, (250., 210.))
    screen.blit(score2, (380., 210.))

    bar1_y += bar1_move

# movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec
    ai_power = 1.5
# Algorithm of red paddle
    if circle_x >= 305.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed - ai_power
            if bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed + ai_power
        else:
            bar2_y == circle_y + 7.5

    if bar1_y >= 420.:
        bar1_y = 420.
    elif bar1_y <= 10.:
        bar1_y = 10.
    if bar2_y >= 420.:
        bar2_y = 420.
    elif bar2_y <= 10.:
        bar2_y = 10.
# Collision
    # Paddle collision
    if circle_x <= bar1_x + 15.:
        # Paddle 1 (Player)
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
            bar1_score += 1
            pygame.mixer.Sound.play(hit_sound)

    if circle_x >= bar2_x - 15.:
        # Paddle 2 (AI)
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
            bar2_score += 1
            pygame.mixer.Sound.play(hit_sound)

# Wall collision
    # No-Bounce
    if circle_x < 5.:
        bar2_score += 1
        value = random.randint(5, 475)
        circle_x, circle_y = 320., value

    elif circle_x > 620.:
        bar1_score += 1
        value = random.randint(5, 475)
        circle_x, circle_y = 307.5, value
    # Bounce
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()
