# 🔐 SafeSign: AI-Powered Forgery & Deepfake Detection Suite

SafeSign is a real-time AI-driven suite designed to detect digital forgery, deepfakes, tampered images, mismatched voices, and signature manipulations. It also generates smart forensic summaries and downloadable PDF reports.

---

## 🚀 Features

- ✍️ **Signature Verification** – Uses OpenCV feature matching to compare and verify signatures.
- 🎭 **Deepfake Detection** – Analyzes video frames for AI-generated facial inconsistencies.
- 🖼️ **Image Forgery Detection (ELA)** – Detects manipulation using Error Level Analysis.
- 🧠 **GPT Summary Generator** – Generates concise AI summaries using OpenAI's models.
- 📄 **PDF Report Generator** – Exports analysis into a forensic-style downloadable PDF.
- 👁️ **Facial Landmark Detection** – Maps 68 key facial points for biometric validation.
- 🎙️ **Voice Matching** – Compares voice embeddings to validate identity.
- ☁️ **Deployable** on Hugging Face Spaces and Streamlit Cloud.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, OpenCV, Pillow, fpdf
- **AI Models**: OpenAI GPT, Deepfake Detection (custom logic), dlib for landmarks
- **Voice Matching**: Cosine similarity (simulated), ready for ECAPA-TDNN upgrade
- **Deployment**: Hugging Face Spaces, Streamlit Cloud

---

## 📦 Installation

```bash
git clone https://github.com/your-username/SafeSign.git
cd SafeSign
pip install -r requirements.txt
streamlit run app.py
