from moviepy.editor import *
import pygame


def play(filename, windowname):
    pygame.display.set_caption(windowname)
    video = VideoFileClip(filename)
    video.resize((400, 400)).preview()
    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    file_name = r"E:\\test_64_64.mp4"
    window_name = "window"
    play(file_name, window_name)
