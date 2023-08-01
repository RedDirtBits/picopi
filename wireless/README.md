# Raspberry Pi Pico Wirless

Though connecting over wirless with the Pico is as straight forward as most other [Micropython](https://micropython.org/) based boards (esp32, esp8266, etc.) it never hurts to have some examples to at least get started and then build upon that into improved ways that include such things such as logging, error handling, etc.

My aim is simply to provide some examples that are as stand-alone as I can make them.  It won't be code so beautifully written it will leave you wondering about your place in the universe, but, it will work.  Well, insofar that I can test them in my set up.  Your mileage may vary and the variance dependent on your comfort and ability to modify accordingly.

I have tried to comment the code as best I can, but I tend to be a bit verbose as I tend to envision someone just starting out and looking to get a working example going that they can use to learn from.

Just remember, I am learning here also.

**example_001**:
Certainly not as basic as you get when it comes to setting up a wireless connection, but not terribly far off and could certainly be done in far fewer lines of code.  This example shows how to connect to WiFi the Pico W but adds in a few other bits of information along with using the onboard LED for an external visual indicator of connection status.  The LED will flast at one second intervals three times on a failed connection and will flash quickly 10 times at 150 millisecond intervals upon a successful wireless connection.