'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-06 16:42:43
LastEditors  : BDFD
Description  : 
FilePath     : \predict\predict.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template, request
import pandas as pd
import numpy as np
import tempproj as temp
import execdata as exe
predict = Blueprint('predict', __name__,
                    static_folder='static', template_folder='templates')

model, sample_le = temp.supervised_classification.Tele_Customer_Churn_0602()


@predict.route('/', methods=["POST", "GET"])
def predict_index():
    SeniorCiitizen = " "
    Partner = " "
    Dependents = " "
    tenure = " "
    OnlineSecurity = " "
    TechSupport = " "
    Contract = " "
    PaperlessBilling = " "
    PaymentMethod = " "
    MonthlyCharges = " "
    if request.method == "GET":
        return render_template('homepage/predict_index.html')
    else:
        para_list = []
        SeniorCiitizen = para_list.append(request.form["SeniorCiitizen"])
        Partner = para_list.append(request.form["Partner"])
        Dependents = para_list.append(request.form["Dependents"])
        tenure = para_list.append(exe.convint(request.form["tenure"]))
        OnlineSecurity = para_list.append(request.form["OnlineSecurity"])
        TechSupport = para_list.append(request.form["TechSupport"])
        Contract = para_list.append(request.form["Contract"])
        PaperlessBilling = para_list.append(request.form["PaperlessBilling"])
        PaymentMethod = para_list.append(request.form["PaymentMethod"])
        MonthlyCharges = para_list.append(request.form["MonthlyCharges"])
        print(para_list)
        return render_template('homepage/predict_index.html')
