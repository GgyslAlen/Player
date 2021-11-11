from moviepy.editor import *
import pygame


def play(filename, windowname):
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0, 0)
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    pygame.display.set_caption(windowname)
    screen = pygame.display.set_mode((64, 64))
    screen.fill((0, 0, 1))
    video = VideoFileClip(filename)
    video.preview()
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
