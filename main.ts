let Choice = 0
let Lunch_options = ["Sushi", "Burger", "Steak", "Spaghetti", "Pizza", "Sausages", "Egg", "Baked potatoes"]
basic.forever(function on_forever() {
    
    while (edubitIrBit.isIrSensorTriggered()) {
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallHeart)
    }
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
    Choice = randint(0, Lunch_options.length - 1)
    basic.showString("" + Lunch_options[Choice])
    while (!edubitIrBit.isIrSensorTriggered()) {
        
    }
})
