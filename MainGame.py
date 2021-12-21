#   Игра на пайтоне с использованием PyGame


import pygame
from GameProcessClass import GameProcess



#WIN_WIDTH = 600
#WIN_HEIGHT = 600
#FPS = int(1000/60)
FPS = 10
#clockFPS = pygame.time.Clock()


winWidth = 600
winHeight = 600


win = pygame.display.set_mode((winWidth,winHeight), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Cosmo Game")




def initGameProcess():
    gameClass = GameProcess(win)

    while gameClass.isRunMainLoop:
        pygame.time.delay(FPS)
        #clockFPS.tick(FPS) 

        gameClass.eventTest()            
        gameClass.keyTest()
        gameClass.updateDisplay()


if __name__ == "__main__":
    initGameProcess()



pygame.quit()