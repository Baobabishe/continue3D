import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import skimage as ski


image = im.open('dimond3.jpg')
image = np.asarray(image)
image = image.astype(np.uint8)

src = np.loadtxt('d3.txt')
dst = np.loadtxt('d0.txt')

# fmt: on

# Estimate the TPS transformation from these points and then warp the image.
# We switch `src` and `dst` here because `skimage.transform.warp` requires the
# inverse transformation!
tps = ski.transform.ThinPlateSplineTransform()
tps.estimate(dst, src)
warped = ski.transform.warp(image, tps)

# Plot the results
fig, axs = plt.subplots(1, 2)
axs[0].imshow(image, cmap='gray')
axs[0].scatter(src[:, 0], src[:, 1], marker='x', color='cyan')
axs[1].imshow(warped, cmap='gray', extent=(0, 640, 480, 0))
axs[1].scatter(dst[:, 0], dst[:, 1], marker='x', color='cyan')

point_labels = [str(i) for i in range(len(src))]
for i, label in enumerate(point_labels):
    axs[0].annotate(
        label,
        (src[:, 0][i], src[:, 1][i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha='center',
        color='red',
    )
    axs[1].annotate(
        label,
        (dst[:, 0][i], dst[:, 1][i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha='center',
        color='red',
    )

plt.show()