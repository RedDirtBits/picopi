import machine
from utime import sleep_ms

def wireless_connected(count: int, duration: int):
    """
    wireless_connected : Use the onboard LED light to indicate
    wireless connected successfully

    Args:
        count (int): Number of times to blink the LE
        duration (int): Length of time in milliseconds LED will
        be on/off
    """
    led = machine.Pin("LED", machine.Pin.OUT)
    led.off()

    while count > 0:
        led.on()
        sleep_ms(duration)
        led.off()
        sleep_ms(duration)
        count -= 1


def wireless_connection_failed(count: int, duration: int):
    """
    wireless_connection_failed : Use the onboard LED light to indicate
    wireless failed to make a connection

    Args:
        count (int): Number of times to blink the LE
        duration (int): Length of time in milliseconds LED will
        be on/off
    """
    led = machine.Pin("LED", machine.Pin.OUT)
    led.off()

    while count > 0:
        led.on()
        sleep_ms(duration)
        led.off()
        sleep_ms(duration)
        count -= 1