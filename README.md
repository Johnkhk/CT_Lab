# CTLAB
---
### Running inference:
Everything is set up as absolute paths for now. <br>


To run inference, change variable *inputdir = yourdicomdir* in *batch_inference*

`python batch_inference.py`


### Files to note:

**new_workspace/run_one_full_slice/batch_inference.py**

**maskrcnn/Mask_RCNN/samples/tumor/tumor.py**
<br>
<br>
added Flask folder **flask_serv** with file **test.py**
tumor.py is now imported as a module, and its main function can be run inside scripts passing arguments by a list of string or in the CLI as so: 
<br>

`python test.py, "splash", "--weights=C:/Users/John/Desktop/UCSD/CT lab/maskrcnn/Mask_RCNN/logs/tumor20211231T1726/mask_rcnn_tumor_0030.h5", "--folder=C:/Users/John/Desktop/UCSD/CT lab/CTMR_robot_lab/data/export_reslice/biopsy 7"`

<br>

