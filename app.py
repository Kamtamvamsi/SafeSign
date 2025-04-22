import streamlit as st
import os
from signature_check import verify_signature
from deepfake_detector import detect_deepfake
from summarizer import generate_summary
from ela_analysis import detect_image_forgery
from report_generator import create_pdf_report

st.set_page_config(page_title="SafeSign - Digital Forgery & Deepfake Detection", layout="centered")
st.title("SafeSign - AI-Powered Digital Forgery Detection Suite")
st.markdown("Detect forged signatures, tampered images, and deepfakes in real-time.")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Do something with the file
    st.write("File uploaded:", uploaded_file.name)


uploaded_file = st.file_uploader("Upload any signature, image, or video file", type=["png", "jpg", "jpeg", "pdf", "mp4"])

if uploaded_file:
    file_path = f"uploads/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Uploaded: {uploaded_file.name}")

    file_ext = uploaded_file.name.split('.')[-1].lower()

    if file_ext in ["jpg", "jpeg", "png"]:
        st.image(file_path, caption="Uploaded Image", use_column_width=True)
        # Signature Verification
        match_score = verify_signature(file_path)
        st.info(f"Signature Match Score: {match_score}%")
        # ELA Forgery Detection
        forged, ela_img = detect_image_forgery(file_path)
        st.image(ela_img, caption="ELA Heatmap")
        st.warning("Forgery Detected!" if forged else "Image seems clean.")
        detection_type = "Image Forgery + Signature Match"
    elif file_ext in ["mp4"]:
        st.video(file_path)
        label, score = detect_deepfake(file_path)
        st.info(f"Deepfake Detection: {label} ({score}% confidence)")
        detection_type = "Video Deepfake Detection"
    else:
        st.warning("Only images and videos are supported in demo version.")
        detection_type = "Unknown"

    # GPT-4 Summary
    st.subheader("AI Summary")
    summary = generate_summary(file_path)
    st.write(summary)

    # Generate PDF
    st.subheader("Generate PDF Report")
    if st.button("Create Report"):
        pdf_path = create_pdf_report(file_path, detection_type, summary)
        with open(pdf_path, "rb") as f:
            st.download_button("Download Report", f, file_name="SafeSign_Report.pdf")
    
    # In your Streamlit app
    if uploaded_file is not None:
     with open("temp_uploaded_image.png", "wb") as f:
        f.write(uploaded_file.read())
    match_score = verify_signature("temp_uploaded_image.png")


