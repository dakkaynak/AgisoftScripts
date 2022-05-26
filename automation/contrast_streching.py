import numpy as np

import matplotlib.pyplot as plt

a = plt.imread('test.jpg')

N = 50
bins = np.linspace(0, 1, N + 1)

ha, ea = np.histogram(a.flatten(), bins=bins)

b = (a - a.min()) / (a.max() - a.min())

hb, eb = np.histogram(b.flatten(), bins=bins)

plt.figure(1, figsize=(10, 10))
plt.clf()

plt.subplot(221)
plt.imshow(a, vmin=0, vmax=1)
plt.axis('off')

plt.title("Low contrast original")

plt.subplot(223)
plt.imshow(b, vmin=0, vmax=1)
plt.axis('off')

plt.title("Contrast Stretched")

plt.subplot(222)
plt.bar(ea[:-1], 1.0 * ha / np.sum(ha), width=ea[1] - ea[0])
plt.xlim(0, 1)

plt.title("Histogram of low contrast image")

plt.subplot(224)
plt.bar(eb[:-1], 1.0 * hb / np.sum(hb), width=eb[1] - eb[0])
plt.xlim(0, 1)

plt.title("Histogram of contrast stretched image")
