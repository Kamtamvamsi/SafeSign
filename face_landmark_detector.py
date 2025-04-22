# Facial Landmark Detection using dlib
import cv2
import dlib

def detect_facial_landmarks(image_path):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    landmarks_detected = False
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
        landmarks_detected = True

    result_path = image_path.replace(".", "_landmarks.")
    cv2.imwrite(result_path, img)
    return result_path, landmarks_detected
