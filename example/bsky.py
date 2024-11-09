# Example for Pico W / PPP2W / PPP2 with RM2

import network
import mip

from secrets import SSID, PASSWORD, COUNTRY, BSKY_USERNAME, BSKY_PASSWORD
import ntptime
import rp2
from time import sleep

# Uncomment if using RM2 on SP/CE connector
#network.wlan_set_pins(32, 35, 34, 33)

# connect to wifi
rp2.country(COUNTRY)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while wlan.isconnected() is False:
    print('Waiting for connection...')
    sleep(1)

# Make sure time is set
ntptime.settime()

# Make sure datetime is available
try:
    import datetime
    del datetime
except ImportError:
    mip.install("datetime")

from atprototools import Session

# Establish Bluesky session
session = Session(BSKY_USERNAME, BSKY_PASSWORD)

# Print the text from your latest post:
latest_bloot = session.getLatestBloot(BSKY_USERNAME).json()
print(latest_bloot['feed'][0]['post']['record']['text'])

# Make a new post
new_post = input("Enter text to post: ")
post = session.postBloot(new_post)

# See the README for further usage of the Bluesky session
