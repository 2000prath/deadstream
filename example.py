#
# usage: python example.py <path>
#
# For lists of commands, events and properties consult the mpv reference:
#
#   http://mpv.io/manual/stable/#list-of-input-commands
#   http://mpv.io/manual/stable/#list-of-events
#   http://mpv.io/manual/stable/#property-list
#

import sys
import time
import threading

from timemachine import GD


if __name__ == "__main__":
    # Open the video player and load a file.
    archive = GD.GDArchive("/home/steve/projects/deadstream/metadata")
    tape = archive.best_tape('1979-11-02')
    player = GD.GDPlayer(tape)
    GD.logger.setLevel(10)

    # Seek to 5 minutes.
    player.seek(600)

    # Start playback.
    player.play()

    # Playback for 15 seconds.
    time.sleep(15)

    # Pause playback.
    player.pause()

    # Wait again.
    time.sleep(3)

    # Terminate the video player.
    #mpv.close()

    # move to track 4
    player.file_loaded_event.clear()
    _ = [player.prev() for i in range(4)]
    try:
      player.file_loaded_event.wait(timeout = 20)
      print (F" loaded event set?:{player.file_loaded_event.is_set()}")
      dcs = player.get_property('demuxer-cache-state')
      print(dcs)
    except:
      print (F" failed to get cache state")
 
    # wait for player to be ready
