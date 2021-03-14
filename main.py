from machine import Pin
import time
import stepper

stepPin = Pin(4, Pin.OUT)
dirPin = Pin(14, Pin.OUT)
sleepPin = Pin(5, Pin.OUT)
Stepper = stepper.Stepper(stepPin, dirPin, sleepPin)

print("stepper initialized")

buttonIn = Pin(12, Pin.IN, Pin.PULL_UP)
buttonOut = Pin(13, Pin.IN, Pin.PULL_UP)
bothButtonsPressed = False

print("buttons initialized")

while True:        
    buttonIn1 = buttonIn.value()
    buttonOut1 = buttonOut.value()

    time.sleep(0.01)

    buttonIn2 = buttonIn.value()
    buttonOut2 = buttonOut.value()

    if not buttonIn1 and not buttonOut1:
        print("both buttons pressed")
        bothButtonsPressed = True
        Stepper.power_off()
        print("stepper off")

    elif not buttonIn1 and buttonIn2:
        print("bothButtonsPressed:" + str(bothButtonsPressed))
        if bothButtonsPressed:
            print("both buttons pressed but not released")
            if buttonIn2 and buttonOut2:
                print("both buttons released")
                bothButtonsPressed = False

            continue

        print("buttonIn pressed")
        Stepper.power_on()
        print("stepper on")
        Stepper.revolution(5)
        print("stepper turned 1 revolution")
        Stepper.power_off()
        print("stepper off")

    elif not buttonOut1 and buttonOut2:
        print("bothButtonsPressed:" + str(bothButtonsPressed))
        if bothButtonsPressed:
            print("both buttons pressed but not released")
            if buttonIn2 and buttonOut2:
                print("both buttons released")
                bothButtonsPressed = False

            continue

        print("buttonOut pressed")
        Stepper.power_on()
        print("stepper on")
        Stepper.revolution(-5)
        print("stepper turned -1 revolution")
        Stepper.power_off()
        print("stepper off")