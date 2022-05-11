import numpy as np

text = "@Tesmanian_com The Tesla China team is amazing"
y = np.expand_dims(text, axis=0)
print(y, text)
