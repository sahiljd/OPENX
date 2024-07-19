import cv2
import random
from cvzone.HandTrackingModule import HandDetector
import cvzone as cvz
import pygame

# Initialize Pygame for audio playback
pygame.mixer.init()

# Load beep sound
collect = beep_sound = pygame.mixer.Sound("collect.mp3")

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

detector = HandDetector(maxHands=2, detectionCon=0.7)
number_to_guess = random.randint(1, 10)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    
    cvz.putTextRect(img, f'Guess the number:', [10, 30], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(40, 180, 250))
    if hands:
        total_fingers = sum(sum(detector.fingersUp(hand)) for hand in hands)
        cv2.putText(img, f"Total fingers: {total_fingers}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        
        if total_fingers == number_to_guess:
           
            cv2.putText(img, "Congratulations! You guessed the number!", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            pygame.mixer.Sound.play(collect)
        elif total_fingers < number_to_guess:
            cv2.putText(img, "Try a higher number.", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        else:
            cv2.putText(img, "Try a lower number.", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
    
    else:
        number_to_guess = random.randint(1, 10)
        cv2.putText(img, "Generating a random number.", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Number Guessing Game", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
