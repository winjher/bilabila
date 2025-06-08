import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

# Loading dataset path directory
DATADIR = "C:/Users/jerwin/Documents/conservation/butterfly"
CATEGORIES = ['Butterfly-Clippers',
 'Butterfly-Common Jay',
 'Butterfly-Common Lime',
 'Butterfly-Common Mime',
 'Butterfly-Common Mormon',
 'Butterfly-Emerald Swallowtail',
 'Butterfly-Golden Birdwing',
 'Butterfly-Gray Glassy Tiger',
 'Butterfly-Great Eggfly',
 'Butterfly-Great Yellow Mormon',
 'Butterfly-Paper Kite',
 'Butterfly-Pink Rose',
 'Butterfly-Plain Tiger',
 'Butterfly-Red Lacewing',
 'Butterfly-Scarlet Mormon',
 'Butterfly-Tailed Jay',
 'Moth-Atlas',
 'Moth-Giant Silk ']

# Loop through categories
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)  # Path to category folder
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray")
        plt.show()
        break  # Break after first image to verify loading
    break  # Break to prevent unnecessary looping

# Print image shape
print(img_array.shape)  

# Resize image
IMG_SIZE = 50
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
image = cv2.imread(new_array, cv2.IMREAD_GRAYSCALE)

# Apply thresholding
_, segmented_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Show output
plt.imshow(segmented_image, cmap="gray")
plt.title("Thresholded Segmentation")
plt.show()

#Edge Detection (Canny) (Useful for detecting wing structures or waste edges):
segmented_image = cv2.Canny(image, 100, 200)
plt.imshow(segmented_image, cmap="gray")
plt.title("Canny Edge Detection")
plt.show()


import cv2
import numpy as np

image = cv2.imread("butterfly.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixels = image.reshape((-1, 3))

# Apply K-means clustering
k = 3  # Number of clusters
kmeans = cv2.kmeans(np.float32(pixels), k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), 10, cv2.KMEANS_RANDOM_CENTERS)[1]

segmented_image = kmeans.reshape(image.shape)
plt.imshow(segmented_image)
plt.title("K-Means Segmentation")
plt.show()
