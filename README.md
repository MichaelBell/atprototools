## atprototools

Easy-to-use and ergonomic library for interacting with bluesky.

This fork has instructions for using ATProto with wireless enabled <br>
MicroPython, such as Pico W, to get as many people writing bsky code as possible. 

## Setup

- Copy the atprototools folder from this repo to your Micropython device.
- Copy [datetime.py](https://github.com/micropython/micropython-lib/blob/master/python-stdlib/datetime/datetime.py) to your Micropython device.

Create a secrets.py on your Micropython device containing:
```python
SSID = 'xx'
PASSWORD = 'xx'
BSKY_USERNAME="xx.bsky.social"
BSKY_PASSWORD="xx"
```
with your Wifi network and BlueSky credentials.

## Run the example

Now you can run the [example](example\bsky.py)

## Usage

Further usage examples:

```python
session = Session(BSKY_USERNAME, BSKY_PASSWORD)

# make a text post
resp = session.postBloot("hello world from atprototools")

# post an image
# session.postBloot("here's an image!", "path/to/your/image")

# get bloots/posts
latest_bloot = session.getLatestNBloots('klatz.co',1).content

# get archive
# carfile = session.getArchive().content

# reply to a post
#   Get first post details for replying to, you can also reply to other posts
#   from getting bloots other ways
# Using "hello world" bloot from above:
first_post = resp.json()
# Create reply_ref:
# - root is the highest up original post
# - parent is the comment you want to reply to directly
# if you want to reply to root make both the same
reply_ref = {"root": first_post, "parent": first_post}
session.postBloot("this is the reply", reply_to=reply_ref)

# reply to a fetched post
latest_bloot = session.getLatestBloot(BSKY_USERNAME).json()
prev_post = latest_bloot['feed'][0]['post']
reply_ref = {"root": prev_post, "parent": prev_post}
session.postBloot("this is another reply", reply_to=reply_ref)
```

### changelog

- Micropython supporting fork
- 0.0.17: chaged case to consistently be camelCase - thanks BSculfor!
- 0.0.16: replies! added to post_bloot, thanks to Jxck-S
- 0.0.15: get_bloot_by_url switched to getPosts instead of getPostThread
- 0.0.14: refactoring for cbase talk
- 0.0.13: register(), thanks Chief!
- 0.0.12: Set your own ATP_HOST! get_skyline. Thanks Shreyan.
- 0.0.11: images! in post_bloot.
- 0.0.10: follow, getProfile
- 0.0.9: move everything into a session class
- 0.0.8: get_bloot_by_url, rebloot
- 0.0.7: getRepo (car files) and get_latest_n_bloots

### Thanks to 

- alice
- [sirodoht](https://github.com/sirodoht)
