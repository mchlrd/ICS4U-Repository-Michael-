import cv2
import mediapipe as mp
import numpy as np

class Workout:
    def __init__(self):
        self.leftcounter = 0
        self.rightcounter = 0
        self.leftstage = None
        self.rightstage = None

    def calculate_angle(self, a, b, c):
        a = np.array(a)  # First
        b = np.array(b)  # Mid
        c = np.array(c)  # End

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle

    def update(self, landmarks):
        raise NotImplementedError("This method should be overridden by subclasses")

    def visualize(self, image):
        raise NotImplementedError("This method should be overridden by subclasses")


class DumbbellCurls(Workout):
    def update(self, landmarks):
        # Get coordinates for left arm
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        # Calculate angle for left arm
        leftarm_angle = self.calculate_angle(left_shoulder, left_elbow, left_wrist)

        # Get coordinates for right arm

        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
        
        # Calculate angle for right arm
        rightarm_angle = self.calculate_angle(right_shoulder, right_elbow, right_wrist)

        # Curl counter logic for left arm
        if leftarm_angle > 165:
            self.leftstage = "down"
        if leftarm_angle < 80 and self.leftstage == 'down':
            self.leftstage = "up"
            self.leftcounter += 1
            print("Left Arm Reps:", self.leftcounter)

        # Curl counter logic for right arm

        if rightarm_angle > 165:
            self.rightstage = 'down'
        if rightarm_angle < 80 and self.rightstage == 'down':
            self.rightstage = 'up'
            self.rightcounter += 1
            print('Right Arm Reps:', self.rightcounter)

    def visualize(self, image, landmarks):
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        cv2.putText(image, f"Left Arm Reps: {self.leftcounter}", tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, f'Right Arm Reps: {self.rightcounter}', tuple(np.multiply(right_elbow, [640,480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)


class LegSquats(Workout):
    def update(self, landmarks):
        # Get coordinates for left leg
        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
        left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
        left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

        # Calculate angle for left leg
        leftleg_angle = self.calculate_angle(left_hip, left_knee, left_ankle)

        # Get coordinates for right leg

        right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
        right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
        right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
        
        rightleg_angle = self.calculate_angle(right_hip, right_knee, right_ankle)

        # Squat counter logic for left leg
        if leftleg_angle > 140:
            self.leftstage = 'down'
        if leftleg_angle < 110 and self.leftstage == 'down':
            self.leftstage = 'up'
            self.leftcounter += 1
            print('Left Leg Reps:', self.leftcounter)

        # Squat counter logic for right leg

        if rightleg_angle > 140:
            self.rightstage = 'down'
        if rightleg_angle < 110 and self.rightstage == 'down':
            self.rightstage = 'up'
            self.rightcounter += 1
            print('Right Leg Reps:', self.rightcounter)

    def visualize(self, image, landmarks):
        left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
        right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
        cv2.putText(image, f"Left Leg Reps: {self.leftcounter}", tuple(np.multiply(left_knee, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, f'Right Leg Reps: {self.rightcounter}', tuple(np.multiply(right_knee, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)


class PushUps(Workout):
    def update(self, landmarks):
        # Get coordinates for right arm
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        # Calculate angle for right arm
        rightarm_angle = self.calculate_angle(right_shoulder, right_elbow, right_wrist)

        # Get coordinates for left arm
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        
        # Calculate angle for left arm
        leftarm_angle = self.calculate_angle(left_shoulder, left_elbow, left_wrist)

        # Push-up counter logic for right arm
        if rightarm_angle > 165:
            self.rightstage = "down"
        if rightarm_angle < 80 and self.rightstage == 'down':
            self.rightstage = "up"
            self.rightcounter += 1
            print("Right Arm Reps:", self.rightcounter)

        # Push-up counter logic for left arm
        if leftarm_angle > 165:
            self.leftstage = 'down'
        if leftarm_angle < 80 and self.leftstage == 'down':
            self.leftstage = 'up'
            self.leftcounter += 1
            print('Left Arm Reps:', self.leftcounter)

    def visualize(self, image, landmarks):
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        cv2.putText(image, f"Right Arm Reps: {self.rightcounter}", tuple(np.multiply(right_elbow, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, f"Left Arm Reps: {self.leftcounter}", tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)


# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def main():
    workout_choice = input("Choose a workout (1. Dumbbell Curls, 2. Leg Squats, 3. Push-ups): ")

    if workout_choice == '1':
        workout = DumbbellCurls()
    elif workout_choice == '2':
        workout = LegSquats()
    elif workout_choice == '3':
        workout = PushUps()
    else:
        print("Invalid choice")
        return

    cap = cv2.VideoCapture(r'C:\Users\Larettie\VSProjects\ICS4U-Repository-Michael-\Final-Comp-Sci-Project\aicoachmp4s\9.mp4')
    #C:\Users\Larettie\VSProjects\ICS4U-Repository-Michael-\Final-Comp-Sci-Project\aicoachmp4s
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

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
                workout.update(landmarks)
                workout.visualize(image, landmarks)
            except Exception as e:
                print("Error:", e)
                pass

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=3, circle_radius=4),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=3, circle_radius=4))

            cv2.imshow('Mediapipe Feed', cv2.resize(image, (600, 800)))

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
