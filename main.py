import cv2
import screen_brightness_control as sbc
import time


def get_room_brightness(capture):
    ret, frame = (
        capture.read()
    )  # ret is a boolean that tells us if the frame was captured, the frame is stored in frame
    if not ret:
        print("Failed to grab frame")
        return None

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    avg_brightness = gray.mean()
    return avg_brightness


def adjust_screen_brightness(background_light):
    target_brightness = int(
        (background_light / 255) * 100
    )  # cam brightness returns from 0-255 so we need ot map or convert it to percentage so that we can adjust the brightness scroller

    target_brightness = max(
        10, target_brightness
    )  # this is to ensure that target brighness falls withing 10 and above so that it is never pitch black

    sbc.set_brightness(target_brightness)
    print(f"Room Light: {background_light:.1f} -> Screen Set To: {target_brightness}%")


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
    else:
        print("Adaptive brightness active! Press Ctrl+C in the terminal to stop.")

        try:
            while True:
                room_light = get_room_brightness(cap)
                if room_light is not None:
                    adjust_screen_brightness(room_light)

                time.sleep(3)
        except KeyboardInterrupt:
            print("\nShutting down adaptive brightness...")

        finally:
            # cleanup 
            cap.release()
            cv2.destroyAllWindows()
            print("Camera turned off successfully.")
