import numpy as np

genders = np.array(["M","F","F","M"])

unique = np.unique(genders)

one_hot = (genders[:, None] == unique).astype(int)

print(one_hot)
