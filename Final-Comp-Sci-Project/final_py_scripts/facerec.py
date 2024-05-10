import cv2
import dlib

# Load the pre-trained face detector
detector = dlib.get_frontal_face_detector()

# Load the pre-trained facial landmark detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the pre-trained face recognition model
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load a sample image
image = cv2.imread("sample_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

# Loop through each detected face
for face in faces:
    # Detect facial landmarks
    landmarks = predictor(gray, face)
    
    # Compute face descriptor
    face_descriptor = facerec.compute_face_descriptor(image, landmarks)
    
    # Draw a rectangle around the face
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
    
    # Print the face descriptor (optional)
    print(face_descriptor)

# Display the image
cv2.imshow("Facial Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
