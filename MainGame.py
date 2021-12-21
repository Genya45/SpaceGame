#   Игра на пайтоне с использованием PyGame


import pygame
from GameProcessClass import GameProcess



#WIN_WIDTH = 600
#WIN_HEIGHT = 600
#FPS = int(1000/60)
FPS = 10    #   частота обновления кадров
#clockFPS = pygame.time.Clock()





#   функция инициализации игрового процеса
def initGameProcess(win):
    gameClass = GameProcess(win)    #   инициализация класса игрового процесса

    
    while gameClass.isRunMainLoop:  #   цикл обновления игрового процесса
        pygame.time.delay(FPS)
        #clockFPS.tick(FPS) 
        gameClass.main_process_update()     #   обновление игрового процесса



if __name__ == "__main__":          #   входная точка
    #   размеры окна
    winWidth = 600
    winHeight = 600

    #   созданное окно
    #win = pygame.display.set_mode((winWidth,winHeight), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
    win = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
    #   название окна
    pygame.display.set_caption("Cosmo Game")
    initGameProcess(win)               #   вызов функции игры



pygame.quit()                       #   выход из игры