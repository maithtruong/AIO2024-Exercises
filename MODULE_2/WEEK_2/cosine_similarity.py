import numpy as np

def compute_cosine(v1, v2):
    v1 = np.asarray(v1)
    v2 = np.asarray(v2)
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    cos_sim = dot_product / (norm_v1 * norm_v2)
    return cos_sim
