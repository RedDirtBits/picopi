import network
import indicator
from utime import sleep, ticks_ms, ticks_diff

# You don't want to share your home wireless credentials, so store them
# in a separate file and exclude them from the repository.  We can then
# import that file and access the variables holding the credentials
#
# The syntax could be WLAN1="my_ssid", WLAN1PASSWD="my_password".  You
# could even go so far as to use a python dictionary, etc.  I have a few
# different wireless networks in my home so I put the required info in the
# logins file and switch between them as needed.
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
    """
    wireless_connect : Connect to a wireless network.  When connected provide
    a visual indication via the onboard LED and provide via stdout how long
    it took to connect and the IP address provided (DHCP)

    Raises:
        RuntimeError: Raise a runtime error if connection is unsuccessful
    """

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

    # set the hostname for the device
    network.hostname("PicoW-A")

    # connect to wireless pulling SSID and Password from credentials file
    wlan.connect(logins.WANSSID, logins.WANPASSWD)

    while max_wait > 0:

        # a status of 3 means connected
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        
        # decrement the max_wait variable if no connection
        max_wait -= 1

        print("Waiting for wireless connection...")

        # sleep for one second
        # another option here is to put the board in idle mode while waiting
        # for the connection to be established with machine.idle().  Every little
        # bit helps when running on battery.  Save the power where you can.
        sleep(1)

    # unable to successfully connect to wireless
    if wlan.status() != 3:
        indicator.wireless_connection_failed(3, 1000)
        raise RuntimeError("Wireless network connection failed")
    
    # successfully connected
    else:
        status = wlan.ifconfig()

        # wlan.config() will return a tuple of 4 values:
        # - IP Address
        # - Subnet Mask
        # - Gateway IP Address (Likely your router)
        # - DNS Server (Likely your router but can be a dedicated server depending on your network)
        print(f"Wireless connected.  IP address: {status[0]}")

        # Not critical for wireless connections, but certainly can be interesting to see how long
        # or how fast wireless establishes a connection.  Time is in milliseconds
        print(f"Connected in: {ticks_diff(ticks_ms(), start)}ms")

        # add a visual indicator of wireless status via the onboard LED
        # call the function from indicator.py and pass in the number of times to flash the LED
        # and the duty cycle or time on/off in milliseconds
        indicator.wireless_connected(10, 150)
        