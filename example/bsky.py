# Example for Pico W / PPP2W / PPP2 with RM2

import network
import requests
from atprototools import Session
from secrets import SSID, PASSWORD, BSKY_USERNAME, BSKY_PASSWORD
from time import sleep

# Uncomment if using RM2 on SP/CE connector
#network.wlan_set_pins(32, 35, 34, 33)

# connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while wlan.isconnected() is False:
    print('Waiting for connection...')
    sleep(1)

session = Session(BSKY_USERNAME, BSKY_PASSWORD)

# We now should have a Bluesky session - see the README for usage

# Print the text from @biglesp's latest post:
latest_bloot = session.getLatestBloot('biglesp.bsky.social').json()
print(latest_bloot['feed'][0]['post']['record']['text'])
