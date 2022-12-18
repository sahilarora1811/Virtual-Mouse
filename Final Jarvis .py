import colorama
from colorama import Fore
print(Fore.BLUE+"HELLO BOSS JARVIS HERE😊")
print(Fore.MAGENTA+"You just have 1 chance")
print(Fore.BLUE+"Enter your password :)")
print(Fore.MAGENTA+"for HINT press 1")
a=int(input(Fore.BLUE+"If you know the password just enter it \n"))
if a==1:
    print(Fore.CYAN+"Hint: password=Team Number")
    b=int(input(Fore.YELLOW+"Please enter the password fast we are running out of time ⌚"))
    if b==148:
        import cv2
        import mediapipe as mp
        import pyautogui

        cap = cv2.VideoCapture(0)
        hand_detector = mp.solutions.hands.Hands()
        drawing_utils = mp.solutions.drawing_utils
        screen_width, screen_height = pyautogui.size()
        index_y = 0

        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks
            if hands:
                for hand in hands:
                    drawing_utils.draw_landmarks(frame, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        if id == 4:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            index_x = screen_width / frame_width * x
                            index_y = screen_height / frame_height * y
                            pyautogui.moveTo(index_x, index_y)
                        if id == 8:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            thumb_x = screen_width / frame_width * x
                            thumb_y = screen_height / frame_height * y
                            print('outside', abs(index_y - thumb_y))
                            if abs(index_y - thumb_y) < 50:
                                pyautogui.click()
                                pyautogui.sleep(1)
            cv2.imshow('Sasta Jarvis', frame)
            cv2.waitKey(1)
if a==(148):
    import cv2
    import mediapipe as mp
    import pyautogui
    cap=cv2.VideoCapture(0)
    hand_detector=mp.solutions.hands.Hands()
    drawing_utils=mp.solutions.drawing_utils
    screen_width,screen_height=pyautogui.size()
    index_y=0

    while True:
        _, frame=cap.read()
        frame=cv2.flip(frame,1)
        frame_height,frame_width,_ =frame.shape
        rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        output=hand_detector.process(rgb_frame)
        hands=output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame,hand)
                landmarks=hand.landmark
                for id,landmark in enumerate(landmarks):
                    x=int(landmark.x*frame_width)
                    y=int(landmark.y*frame_height)
                    if id==4:
                        cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                        index_x=screen_width/frame_width*x
                        index_y=screen_height/frame_height*y
                        pyautogui.moveTo(index_x,index_y)
                    if id==8:
                        cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                        thumb_x=screen_width/frame_width*x
                        thumb_y=screen_height/frame_height*y
                        print('outside',abs(index_y-thumb_y))
                        if abs(index_y-thumb_y)<50:
                            pyautogui.click()
                            pyautogui.sleep(1)
        cv2.imshow('Sasta Jarvis',frame)
        cv2.waitKey(1)
else:
    print(Fore.RED+"!!INVALID PASSWORD 🚫!!")
    print(Fore.RED+"😡!!IMPOSTER FOUND!!😡")
    print(Fore.RED + "💀 BOSS YOU ARE IN DANGER PLEASE REBOOT YOUR SYSTEM 💀")