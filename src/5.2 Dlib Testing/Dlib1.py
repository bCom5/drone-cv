import cv2
import dlib

cap = cv2.VideoCapture('../../vid/swarm_drone.mp4')

# Create the correlation tracker - the object needs to be initialized
# before it can be used
tracker = dlib.correlation_tracker()

win = dlib.image_window()
# We will track the frames as we load them off of disk
tracker.start_track(img, dlib.rectangle(255, 575, 305, 625))
while True:
    ret, frame = cap.read()
    wK = cv2.waitKey(60) & 0xff
    if ret == False or wK == 27:
        break
    
    img = frame.copy()
    tracker.update(img)
    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(tracker.get_position())
    dlib.hit_enter_to_continue()