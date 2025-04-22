# Signature verification module
import cv2
import numpy as np

def verify_signature(file_path, reference_signature_path, test_signature_path, uploaded_signature_path):
    img1 = cv2.imread(file_path)
    if img1 is None:
        raise FileNotFoundError(f"Failed to load image from {file_path}")

    img1 = cv2.resize(img1, (300, 150))
    # ... rest of your code
    # Read both images
    img1 = cv2.imread(reference_signature_path, 0)
    img2 = cv2.imread(uploaded_signature_path, 0)

    # Resize to same shape
    img1 = cv2.resize(img1, (300, 150))
    img2 = cv2.resize(img2, (300, 150))

    # ORB detector for feature matching
    orb = cv2.ORB_create()

    # Find the keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Match features using BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    if des1 is None or des2 is None:
        return 0  # No features found

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Calculate similarity
    match_score = len(matches) / max(len(kp1), len(kp2)) * 100
    match_score = round(match_score, 2)

    return match_score

#def verify_signature(uploaded_signature_path, reference_signature_path='models/reference_signature.png'):
    # Read both images
    img1 = cv2.imread(reference_signature_path, 0)
    img2 = cv2.imread(uploaded_signature_path, 0)

    # Resize to same shape
    img1 = cv2.resize(img1, (300, 150))
    img2 = cv2.resize(img2, (300, 150))

    # ORB detector for feature matching
    orb = cv2.ORB_create()

    # Find the keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Match features using BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    if des1 is None or des2 is None:
        return 0  # No features found

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Calculate similarity
    match_score = len(matches) / max(len(kp1), len(kp2)) * 100
    match_score = round(match_score, 2)

    return match_score
