from includes import *


# def ps_code(code, maps, player):
#     player.translate(code)
        

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

# def event_handle(wn, maps, player):
#     while True:
#         pygame.time.delay(60)
#         for e in pygame.event.get():
#             if e.type == pygame.QUIT:
#                 pygame.quit()
#         code = handle_input()
#         ps_code(code, maps, player)
#         wn.render(maps)
def handle_input2():
    x = 0
    y = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        y = y + -32 
    if key[pygame.K_RIGHT]:
        x = x + 32
    if key[pygame.K_LEFT]:
         x = x + -32 
    if key[pygame.K_DOWN]:
        y = y + 32
    return (x, y)

def play(obj):
    vector = handle_input()
    obj.translate(vector)


if __name__ == "__main__":
    pygame.init()
    wn = Engine(800, 600, caption="myEngine")
    maps = Scene("Main")
    player = GameObject("player", (250, 100), "first.png")
    player.components["Dynamic"] = 1
    maps.add_object(player)
    player.script = play
    top = GameObject("top", (250, 300), "top.png")
    maps.add_object(top)
   
    wn.update(maps)

