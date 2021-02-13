import time
import cv2
import mss
import numpy
import time
import uuid
import read_grad

def run():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 90, "left": 1600, "width": 70, "height": 60}

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            img = img[:,:,:3]
            grad = read_grad.read(img)

            if len(grad) > 0 and grad[-1] == '%':
                gradient = int(grad[:-1])

                


            time.sleep(2)

run()
