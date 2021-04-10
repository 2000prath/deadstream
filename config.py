
# State variables
INIT = 0
READY = 1
PAUSED = 2
STOPPED = 3
PLAYING = 4
PLAY_STATES = ['Init','Ready','Paused','Stopped','Playing']
SELECT_DATE = False
PLAY_STATE = INIT
DATE = None

# Hardware pins

year_pins = (16,22,23)   # cl, dt, sw
month_pins = (12,5,6)
day_pins = (13,17,27)

select_pin = None
play_pause_pin = None
rewind_pin = None
stop_pin = None
ffwd_pin = None

select_pin = 4   # pin 4 ok w/ Sound card
#play_pause_pin = 2 # from the I2C bus (may need to connect to ground)
#rewind_pin = 3  # from the I2C bus (may need to connect to ground)
stop_pin = 20   # pin 18 interferes with sound card
ffwd_pin = 26    # pin 26 ok with sound card.


