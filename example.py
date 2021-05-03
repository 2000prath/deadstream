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
GD.logger.setLevel(10)

if __name__ == "__main__":
    # Open the video player and load a file.
    archive = GD.GDArchive("/home/steve/projects/deadstream/metadata")
    tape = archive.best_tape('1979-11-02')
    p = GD.GDPlayer(tape)
    p.track_event.clear()
    
    # Seek to 5 minutes.
    #p.fseek(600)
   
    # Start playback.
    p.play()

    # Playback for 15 seconds.
    time.sleep(5)

    # Pause playback.
    p.pause()
    
   # for i in range(8): p.next()
    p.seek_to(8,0.0)

    p.status()
    p.play()
    time.sleep(5)
    #for i in range(3): p.fseek(-30)
"""
    print ("Seek testing")
    p.track_event.clear()
    for i in range(12): p.fseek(10) 
"""
"""
    # move to track 4
    p.file_loaded_event.clear()
    _ = [p.prev() for i in range(4)]
    try:
      p.file_loaded_event.wait(timeout = 20)
      print (F" loaded event set?:{p.file_loaded_event.is_set()}")
      dcs = p.get_property('demuxer-cache-state')
      print(dcs)
    except:
      print (F" failed to get cache state")
 
    # wait for player to be ready
"""
