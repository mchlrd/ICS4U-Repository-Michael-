from turtle import right
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
#r'C:\Users\Larettie\VSProjects\ICS4U-Repository-Michael-\Final-Comp-Sci-Project\aicoachmp4s\6.mp4'

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

# Curl counter variables
left_counter = 0
left_stage = None
right_counter = 0
right_stage = None

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates for left hand
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Calculate angle for left hand
            leftarm_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

            # Get coordinates for right hand
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate angle for right hand

            rightarm_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

            # Get coordinates for left leg

            left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            # Calculate angle for left leg

            leftleg_angle = calculate_angle(left_hip, left_knee, left_ankle)
            
            # Get coordiantes for right leg

            right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            
            # Calculate angle for right leg

            rightleg_angle = calculate_angle(right_hip, right_knee, right_ankle)
            

            # Visualize angles

            # Arm angles
            cv2.putText(image, f"Left: {leftarm_angle}", tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, f"Right: {rightarm_angle}", tuple(np.multiply(right_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Leg angles
            # cv2.putText(image, f'Left: {leftleg_angle}', tuple(np.multiply(left_knee, [640,480]).astype(int)),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
            # cv2.putText(image, f'Right: {rightleg_angle}', tuple(np.multiply(right_knee, [640,480]).astype(int)),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)

            # Curl counter logic for left hand
            if leftarm_angle > 165:
                left_stage = "down"
            if leftarm_angle < 80 and left_stage == 'down':
                left_stage = "up"
                left_counter += 1
                print("Left Hand Reps:", left_counter)

            # #Logic for left leg
            # if leftleg_angle > 140:
            #     left_stage = 'down'
            # if leftleg_angle < 110 and left_stage == 'down':
            #     left_stage = 'up'
            #     left_counter += 1
            #     print('Left Leg Reps:', left_counter)
            

            # # Curl counter logic for right hand
            if rightarm_angle > 165:
                right_stage = "down"
            if rightarm_angle < 80 and right_stage == 'down':
                right_stage = "up"
                right_counter += 1
                print("Right Hand Reps:", right_counter)

            #Logic for right leg

            # if rightleg_angle > 140:
            #     right_stage = 'down'
            # if rightleg_angle < 110 and right_stage == 'down':
            #     right_stage = 'up'
            #     right_counter += 1
            #     print('Right Leg Reps:', right_counter)

            
        except Exception as e:
            print("Error:", e)
            pass

        # Render counters
        # Setup status boxes
        cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

        # Left rep data
        cv2.putText(image, 'LEFT REPS', (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(left_counter),
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # Right rep data
        cv2.putText(image, 'RIGHT REPS', (110, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(right_counter),
                    (110, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
        
        #Render detections

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness=3, circle_radius=4),
                                  mp_drawing.DrawingSpec(color=(245,66,230), thickness=3, circle_radius=4))

        cv2.imshow('Mediapipe Feed', cv2.resize(image, (480, 640)))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()