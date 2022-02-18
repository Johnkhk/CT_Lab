import sys
sys.path.insert(1, 'C:/Users/John/Desktop/UCSD/CT lab/flask_serv/samples/tumor')
from tumor import hello, dicom_folder_splash, main

# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy

# hello()
# dicom_folder_splash
# inputdir = "C:/Users/John/Desktop/UCSD/CT lab/CTMR_robot_lab/data/export_reslice/biopsy 7"
# uh=["splash", "--weights=C:/Users/John/Desktop/UCSD/CT lab/maskrcnn/Mask_RCNN/logs/tumor20211231T1726/mask_rcnn_tumor_0030.h5", "--folder="+inputdir
main()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= ''
# cb = SQLAlchemy(app)

# a = "sss"
# @app.route('/')
# def hello_world():
#     return a
#     # return 'Hello, World!'
# @app.route('/pushdicom', methods=['GET', 'POST'])
# def push():
#     if request.method == 'POST':



# if __name__ == '__main__':
#     app.run(debug=True)
