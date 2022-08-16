from includes import *



def inputs():
    key = pygame.key.get_pressed()
    return key


def play(obj):
    keys = inputs()
    if keys[pygame.K_a]:
        obj.action("top", "play", 1)
    #obj.translate(vector)
    

if __name__ == "__main__":   
    pygame.init()
    window = Engine(600, 600, delay=100, caption="Test")
    scene = Scene("Main")
    player1 = GameObject("Player1", (100, 100), "first.png", None, 2)
    player2 = GameObject("top", (200, 200), "top.png", z_index=1)
    player1.script = play
    move = Actions("top", ["first.png", "1.png", "2.png", "3.png"])
    player1.set_action(move)
    scene.add_object(player1)
    scene.add_object(player2)
    window.update(scene)

