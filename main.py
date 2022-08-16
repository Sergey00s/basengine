from includes import *  

def handle_input():
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
    window = Engine(600, 600, delay=100, caption="Test")
    scene = Scene("Main")

    player1 = GameObject("Player1", (100, 100), "first.png", None, 2)
    player2 = GameObject("Player2", (200, 200), "first.png", None, 1)
    player1.script = play
    
    scene.add_object(player1)
    scene.add_object(player2)

    window.update(scene)

