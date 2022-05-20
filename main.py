number = 0
bestNumber = 0

def on_gesture_shake():
    global number, bestNumber
    number = randint(1, 6)
    basic.show_string("" + str((number)))
    bestNumber = 6
    if number == bestNumber:
        music.stop_all_sounds()
        music.play_melody("C E F G A B C5 C5 ", 170)
    else:
        music.stop_all_sounds()
        music.play_melody("C C C C C C C C ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
