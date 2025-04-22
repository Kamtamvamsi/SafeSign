# Voice Matching using speaker embedding (simulated demo)
from scipy.spatial.distance import cosine
import numpy as np

def match_voices(voice1_path, voice2_path):
    # Placeholder for real embeddings from models like ECAPA-TDNN or Resemblyzer
    np.random.seed(0)
    emb1 = np.random.rand(512)
    emb2 = np.random.rand(512)
    similarity = 1 - cosine(emb1, emb2)
    return round(similarity * 100, 2)
