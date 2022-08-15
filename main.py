from includes import *
from win import *


def ps_code(code, maps, player):
    player.translate(code)
        

def handle_input():
    x = 0
    y = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        y = y + -32 
    if key[pygame.K_d]:
        x = x + 32
    if key[pygame.K_a]:
         x = x + -32 
    if key[pygame.K_s]:
        y = y + 32
    return (x, y)

def event_handle(wn, maps, player):
    while True:
        pygame.time.delay(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        code = handle_input()
        ps_code(code, maps, player)
        wn.update(maps)


if __name__ == "__main__":
    pygame.init()
    wn = Cr_Window(800, 600)
    wn.set_window("pytry")
    player = GameObject("player", (250, 250), "first.png")
    maps = Scene("Main")
    maps.add_object(player)
    event_handle(wn, maps, player)
