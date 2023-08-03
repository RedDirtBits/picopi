# Pico Pi

My adventures and experimentations with [Raspberry Pi Pico and Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) using [Micropython](https://micropython.org/).

# A Work In Progress

This is very much a work in progress.  Not terribly long ago I was spending good chunks of time using various Micropython based microcontrollers.  In fact, I have a cabinet full of them along with various sensors and peripherals.  I started out with Arduino but just couldn't bring myself to invest in and dive into the C like language after having spent the time I had with [Python](https://www.python.org/), though I did try using the [Arduino Uno](https://store-usa.arduino.cc/products/arduino-uno-rev3?selectedStore=us) and the [Arduino Mega](https://store-usa.arduino.cc/products/arduino-mega-2560-rev3?selectedStore=us).  I was very interested in PLC's at the time and the Arduino seemed well suited for such things.

When I learned that you could use _python_ on a microcontroller, I was off to the races.  I needed something that could keep me in touch with Python (I was not using it at work nearly as much as I hoped) and Micropython based microcontrollers gave me that outlet.  I don't live in a really technically saturated area like you would find in much larger towns and cities so I spend a lot of time working through the various difficulties and challenges.  Great for really embedding those lessons, not so much for staying motivated.  As such, the time spent working with microcontrollers comes and goes as I take breaks to not get overwhelmed.  That in addition to work/life balance, family, all the usual things come with much higher priorities.

All that said to say that what you find here is very much a work in progress and very likely not the best of anything in the way of coding practices, ways to tackle certain tasks, etc. but I am willing to listen to critique and if you have some to offer to help my learning progress, please, feel free to do so.

# Utilities

Info on some utilities I have found useful in working with the Raspberry Pi Pico and Micropython in general

## rshell

_rshell_ is a command line utility that is largely useful for working with virtually any micropython based microcontroller.  To install it, run the following command:

```bash
sudo pip3 install rshell
```

You will also need add yourself (user) to the _dialout_ group:

```bash
sudo usermod -aG $(whoami)
```

You will need to logout and back in or reboot in order for the change to take effect.  Once you have rshell installed you simply plugin your microcontroller into your USB port, open a command prompt and type the command `rshell`.  You _should_ see output similar to that below:

```bash
$ rshell
Connecting to /dev/ttyACM0 (buffer-size 512)...
Trying to connect to REPL  connected
Retrieving sysname ... rp2
Testing if sys.stdin.buffer exists ... Y
Retrieving root directories ... /indicator.py/ /logins.py/ /main.py/ /secrets.py/ /wlan_connect.py/
Setting time ... Jul 31, 2023 18:57:18
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 1970
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
/home/reddirt>
```

When you run rshell you will be at a command prompt from which you can access the micropython REPL by simply running the command `repl`.  The down side appears to be that even if you use `Control-D`, `exit` or `exit()` it does not release you from the REPL and the only effective way I have found to get back to the rshell command prompt is to unplug the microcontroller, plug it back in and start over.  The good news is that you don't actually have to be at the rshell command prompt to run commands on the board.  For example, in the output above you can see a file named `secrets.py` that was used for testing.  It can be removed using the rshell utility without entering the rshell command prompt:

```bash
rshell rm /pyboard/secrets.py
```

You might be asking, where did `pyboard` come from?  That seems to be the default name for Pico devices but is also displayed in the rshell output when you enter the rshell command prompt as seen above with `Evaluating board_name ... pyboard`.  You can change this if desired:

```bash
echo 'name="PicoW"' > /pyboard/board.py
```

There are various other commands that can be used as well that can be seen by running the command `help` from the rshell command prompt:

```bash
> help

Documented commands (type help <topic>):
========================================
args    cat  connect  date  edit  filesize  help  mkdir  rm     shell
boards  cd   cp       echo  exit  filetype  ls    repl   rsync

Use Control-D (or the exit command) to exit rshell.
```

You can find more information by vising the Github link in the _Resource Links_ below.

## esptool

I use [esptool](https://github.com/espressif/esptool/) primarily to erase and flash ESP32 devices.  It can easily be installed with the command `pip3 install esptool`.  Microcontrollers such as the Pico use `/dev/ttyACM0` serial port.  Others such as the [TinyPico](https://www.tinypico.com/) use `/dev/ttyUSB0`.  Be sure when running the _erase_ and _flash_ commands you are targetting the correct serial port.

For the Raspberry Pi Pico, it doesn't find much use withe UF2 bootloader.  For most other ESP32 based boards it is quite handy.

To erase the flash:

```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```

The `--chip` flag needs to be correct as well.  For example, if you are using a microcontroller with the ESP32-C3 chip then change the flag to `--chip esp32c3`.

To write micropython to the microcontroller you need to first download the correct micropython firmware for your particular device such as the [TinyPico](https://www.tinypico.com/).  Once you have that you can flash it to the board with:

```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 tinypico-20230426-v1.20.0.bin
```

## MicroPico (a.k.a pico-w-go)

I truly wish there were some kind of extension like MicroPico for ESP32 based boards.  It's lightweight, has a functional intellisense, you can access the REPL and more.  There is a link to the GitHub for MicroPico in the Resource Links below.

# Resource Links

Resources to information, troubleshooting issues and the like

- [MicroPython for Kids](https://www.coderdojotc.org/micropython/)
  - Don't be put off by it being for kids.  If you are just starting out with the Pico, it is a good resource.
- [Raspberry Pi Pico W Firmware](https://micropython.org/download/rp2-pico-w/)
- [Raspberry Pi Pico Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
- [Raspberry Pi Pico Pinout](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf)
- [Connecting To The Internet With Pico](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf)
- [rshell](https://github.com/dhylands/rshell)
  - Hasn't been updated in a long time, but still very useful
- [pico-w-go](https://github.com/paulober/Pico-W-Go)
  - If you prefer to write micropython in VS Code, this extension for the Raspberry Pi Pico is awesome