#https://www.deep-ml.com/problems/76?from=Linear%20Algebra

import numpy as np

def cosine_similarity(v1, v2):
    # Implement your code here
    return (np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)))
