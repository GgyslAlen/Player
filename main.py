from moviepy.editor import *
import pygame


def play(filename, windowname):
    pygame.display.set_caption(windowname)
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    video = VideoFileClip(filename)
    video.preview(fullscreen=True)
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
    interframe_wait_ms = 30
    play(file_name, window_name)
