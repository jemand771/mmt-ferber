import numpy as np
import cv2
import matplotlib.pyplot as plt

WIDTH = 640
HEIGHT = 480

# Calculate the actual image size in the stream (accounting for rounding
# of the resolution)
FWIDTH = (WIDTH + 31) // 32 * 32
FHEIGHT = (HEIGHT + 15) // 16 * 16

def hist_from_file(file_name):
    with open(file_name, "rb") as f:
    # Load the Y (luminance) data from the stream
        Y = np.fromfile(f, dtype=np.uint8, count=FWIDTH*FHEIGHT).reshape((FWIDTH, FHEIGHT))
        # slice Y
        #Y = Yraw[:, :, 0]
        # create the histogram
        histogram, bin_edges = np.histogram(Y, bins=256, range=(0, 255))
    return histogram
    # print(bin_edges)

# gray = cv2.cvtColor(Y, cv2.COLOR_GRAY2RGB)
# plt.imshow(gray)
# plt.title('my picture')
# plt.show()
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("grayscale value")
# plt.ylabel("pixel count")
# plt.xlim([0.0, 255.0])  # <- named arguments do not work here

# plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.plot(hist_from_file("2mice.yuv") - hist_from_file("plain.yuv"))  # <- or here
plt.savefig('m2diff.png')
