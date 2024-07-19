import cv2 as cv
import cvzone as cvz
from cvzone.HandTrackingModule import HandDetector
import random
import pygame

# Initialize Pygame for audio playback
pygame.mixer.init()

# Load beep sound
point = beep_sound = pygame.mixer.Sound("point.mp3")
error = beep_sound = pygame.mixer.Sound("error.mp3")


cap = cv.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

detector = HandDetector(detectionCon=0.8, maxHands=1)

moves = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(moves)


while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    hands, frame = detector.findHands(frame)

    if hands:
        lmlist = hands[0]
        fingersUp = detector.fingersUp(lmlist)
        finger_count = sum(fingersUp)
        
        cvz.putTextRect(frame, f'Finger Count: {finger_count}', [20, 100], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(250, 0, 250))
        
        
        if finger_count == 2:
            player_move = "Scissors"
        elif finger_count == 5:
            player_move = "Paper"
        elif finger_count == 0:
            player_move = "Rock"    
        else:
            player_move = None
        
        if player_move:
            cvz.putTextRect(frame, f'Your Move: {player_move}', [20, 503], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(250, 0, 250))
            
            
            cvz.putTextRect(frame, f'Computer Move: {computer_move}', [20, 546], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(250, 0, 250))
            
            if player_move == computer_move:
                result = "It's a tie!"
                pygame.mixer.Sound.play(error)
            elif (player_move == "Rock" and computer_move == "Scissors") or \
                (player_move == "Paper" and computer_move == "Rock") or \
                (player_move == "Scissors" and computer_move == "Paper"):
                result = "You win!"
                pygame.mixer.Sound.play(point)
            else:
                result = "Computer wins!"
                pygame.mixer.Sound.play(error)
            
            cvz.putTextRect(frame, f'Result: {result}', [20, 610], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(250, 0, 250))
        if player_move==None:
            cvz.putTextRect(frame, 'Invalid Move!!', [20, 503], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(250, 0, 250))
            
            
    else:
        computer_move = random.choice(moves)
        cvz.putTextRect(frame, 'Changing Computer Move!!', [20, 503], 2, 2, offset=10, border=1,
                                   colorB=(130, 200, 255),colorR=(250, 0, 250))
            
                   
    
    cv.imshow("Frame", frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
