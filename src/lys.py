lights_toggled = False

def on_forever():
    global lights_toggled

    if pins.analog_read_pin(AnalogPin.P1) < 9:
        pins.digital_write_pin(DigitalPin.P2, 1)
        lights_toggled = True
    elif lights_toggled:
        basic.pause(500)
        lights_toggled = False
        if pins.analog_read_pin(AnalogPin.P1) != 8:
            pins.digital_write_pin(DigitalPin.P2, 0)

basic.forever(on_forever)