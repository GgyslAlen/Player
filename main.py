import cv2

def play(filename, windowname, interframe):
    cap = cv2.VideoCapture(filename)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    cv2.namedWindow(windowname, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(windowname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while (True):
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(windowname, frame)
        if cv2.waitKey(interframe) & 0x7F == ord('q'):
            print("Exit requested.")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    file_name = r"/home/pi/test_64_64.mp4"
    window_name = "window"
    interframe_wait_ms = 30
    play(file_name, window_name, interframe_wait_ms)
