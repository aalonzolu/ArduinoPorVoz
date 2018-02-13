from pyfirmata import Arduino, util

def arduAction(action):

    LED_PIN = 8
    ALARM_PIN =9
    BOARD = '/dev/cu.usbmodem1411'
    try:
        board = Arduino(BOARD)
        if (action == 'luz-on'):
            print("Encendiendo luz")
            board.digital[LED_PIN].write(1)
        if (action == 'luz-off'):
            print("Apagando luz")
            board.digital[LED_PIN].write(0)
        if (action == 'alarm-on'):
            print("Encendiendo alarma")
            board.digital[ALARM_PIN].write(1)
        if (action == 'alarm-off'):
            print("Apagando alarma")
            board.digital[ALARM_PIN].write(0)
    except:
        print("Error con aruduino")