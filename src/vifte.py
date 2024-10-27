temp = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P1)
old_temp = temp - 1

def speed(temp):
    spd = 0
    if temp > 21:
        spd = 34 - ((21 - temp) * 11)

    if spd > 100:
        spd = 100

    return spd

def on_forever():
    global temp
    global old_temp

    old_temp = temp
    temp = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P1)

    serial.write_line("" + str(temp))
    serial.write_line("" + str(old_temp))
    if temp > 21:
        smarthome.motor_fan(AnalogPin.P2, True, speed(temp))
    else:
        smarthome.motor_fan(AnalogPin.P2, False)

def refresh_screen():
    OLED.clear()
    OLED.draw_line(0, 11, 144, 11)
    OLED.write_string_new_line("     Living Room")
    OLED.new_line()
    OLED.write_string_new_line(" Temperature: " + temp)
    OLED.write_string_new_line(" Fan speed: " + speed(temp) + "%")
    OLED.draw_line(0, 60, 144, 60)

def refresh_loop():
    if old_temp != temp:
        refresh_screen()

OLED.init(128, 64)
basic.forever(on_forever)
loops.every_interval(500, refresh_loop)