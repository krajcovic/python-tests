#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

image = np.random.rand(30,60)
plt.imshow(image, cmap=plt.cm.plasma)
plt.colorbar()
plt.show()


