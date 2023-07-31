import network
import indicator
from utime import sleep, ticks_ms, ticks_diff

# You don't want to share your home wireless credentials, so store them
# in a separate file and exclude them from the repository.  We can then
# import that file and access the variables holding the credentials
import logins

# ticks_ms and ticks_diff are not strictly necessary but it makes for
# interesting additional information if for no other reason than logging.
#
# sleep, however is good to include as it provides time for the wireless
# to become active and establish the connection and provides a mechanism
# to break out of the connection process instead of the microcontroller
# endlessly attempting to connect
from utime import sleep, ticks_ms, ticks_diff

def wireless_connect():

    # start the timer that will measure how long it takes to connect to WiFi
    start = ticks_ms()

    # provide a counter in which to use as a stopping point if there are issues
    # with connecting to wireless
    max_wait = 10

    # console message that connection attempt has begun
    print(f"Attempting to connect to wireless network: {logins.WANSSID}")

    # set WiFi to a variable
    wlan = network.WLAN(network.STA_IF)

    # activate wireless
    wlan.active(True)

    # connect to wireless pulling SSID and Password from credentials file
    wlan.connect(logins.WANSSID, logins.WANPASSWD)

    while max_wait > 0:

        # a status of 3 means connected
        if wlan.status() < 0 or wlan.status() >= 3:
            break

        max_wait -= 1
        print("Waiting for wireless connection...")
        sleep(1)

    if wlan.status() != 3:
        indicator.wireless_connection_failed(3, 1000)
        raise RuntimeError("Wireless network connection failed")
    else:
        status = wlan.ifconfig()
        print(f"Wireless connected.  IP address: {status[0]}")
        print(f"Connected in: {ticks_diff(ticks_ms(), start)}ms")
        indicator.wireless_connected(10, 150)
        