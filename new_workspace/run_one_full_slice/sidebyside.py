# import numpy as np
# # import pylab
# import matplotlib.cm as cm
# import Image
# import matplotlib.pyplot as plt
# import os
# f = plt.figure()

# inputdir = "C:/Users/John/Desktop/UCSD/CT lab/new_workspace/run_one_full_slice/biopsy 1 png/"
# outputdir = "C:/Users/John/Desktop/UCSD/CT lab/new_workspace/run_one_full_slice/biopsy 1 splash/"

# inn = os.listdir(inputdir)
# out = os.listdir(outputdir)
# for i, f in enumerate(os.listdir(inputdir)):
# # for n, fname in enumerate(('1.png', '2.png')):
#     image=Image.open(fname).convert("L")
#     arr=np.asarray(image)
#     f.add_subplot(2, 1, n)  # this line outputs images on top of each other
#     # f.add_subplot(1, 2, n)  # this line outputs images side-by-side
#     plt.imshow(arr,cmap=cm.Greys_r)
# plt.title('Double image')
# plt.show()