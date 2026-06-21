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
    
    # --- SHOW THE LIVE VIDEO HERE ---
    # This creates a window and displays the current frame
    # cv2.imshow('Live Camera Feed', frame)
    # cv2.waitKey(1) # Necessary to refresh the window display
    # --------------------------------

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    avg_brightness = gray.mean()
    return avg_brightness


def adjust_screen_brightness(background_light, current_screen_brightness):
    # 1. Map raw light to a target percentage
    calculated_target = int((background_light / 255) *100) # cam brightness returns from 0-255 so we need ot map or convert it to percentage so that we can adjust the brightness scroller
    calculated_target = max(10, calculated_target)  # this is to ensure that target brighness falls withing 10 and above so that it is never pitch black
    
    
    # smooth transition logic
    smoothing_factor = 0.15
    
    new_brightness = current_screen_brightness + ((calculated_target - current_screen_brightness) * smoothing_factor)
    
    new_brightness = int(round(new_brightness))

    if new_brightness != current_screen_brightness:
        sbc.set_brightness(new_brightness)
        print(
            f"Room Light: {background_light:.1f} -> Calculated Target: {calculated_target}% -> Actual Screen Set To: {new_brightness}%"
        )
    else:
        print(f"Room Light: {background_light:.1f} -> Stable at: {new_brightness}%")

    return new_brightness


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
    else:
        print("Adaptive brightness active! Press Ctrl+C in the terminal to stop.")



        try: 
            current_brightness = sbc.get_brightness()[0]
        except Exception: 
            current_brightness = 50 #fallback brightness if all fails 
            
        try:
            while True:
                room_light = get_room_brightness(cap)
                if room_light is not None:
                    current_brightness = adjust_screen_brightness(room_light, current_brightness)

                time.sleep(5)
        except KeyboardInterrupt:
            print("\nShutting down adaptive brightness...")

        finally:
            # cleanup 
            cap.release()
            cv2.destroyAllWindows()
            print("Camera turned off successfully.")
