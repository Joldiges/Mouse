#!/usr/bin/sudo python3

import mouse
import time


if __name__ == "__main__":
    with open('mouseLog.log', 'a+') as f:
        start = time.time()
        lastLoc = None
        lastClick = None
        while (time.time() - start) < 14400:  # 4 hours
        # while (time.time() - start) < 5:  # 20 sec
            now = time.time()
            loc = mouse.get_position()
            leftClick = mouse.is_pressed(button='left')
            if (loc != lastLoc) or (leftClick and not lastClick):
                print('; '.join([str(i) for i in [now, loc, leftClick]]))
                f.write('; '.join([str(i) for i in [now, loc, leftClick]]) + '\n')
            lastLoc = loc
            lastClick = leftClick
