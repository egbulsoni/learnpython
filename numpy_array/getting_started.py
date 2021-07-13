height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 85.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# float[] x = np_height.array(list(zip(np_height))
# float[] y = np_weight.array(list(zip(np_weight)))

# a fórmula é minha, eu faço como eu quiser!
# BMI boladão
# print(np.divide(np_height, np_weight / (np_weight ** 3)))

bmi = np_weight / np_height ** 2
print(bmi)

print(bmi > 23)
print(bmi[bmi > 23])

weight_kg = np.array(weight)
bmi_in_pounds = weight_kg * 2.2

print(bmi_in_pounds)
 