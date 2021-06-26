cChoice = 0
Lunch_options = ["Sushi",
    "Burger",
    "Steak",
    "Spaghetti",
    "Pizza",
    "Sausages",
    "Egg",
    "Baked potatoes"]

def on_forever():
    global Choice
    while edubitIrBit.is_ir_sensor_triggered():
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_HEART)
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
    Choice = randint(0, len(Lunch_options) - 1)
    basic.show_string("" + (Lunch_options[Choice]))
    while not (edubitIrBit.is_ir_sensor_triggered()):
        pass
basic.forever(on_forever)
