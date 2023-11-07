'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-07 12:19:32
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

df = pd.read_csv(
    'https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_Preprocessed.csv',
    encoding='utf-8')
seniorcitizen_lists = df['SeniorCitizen'].unique().tolist()
seniorcitizen_lists.sort()
print(seniorcitizen_lists)
partner_lists = df['Partner'].unique().tolist()
partner_lists.sort()
dependents_lists = df['Dependents'].unique().tolist()
dependents_lists.sort()
onlinesecurity_lists = df['OnlineSecurity'].unique().tolist()
onlinesecurity_lists.sort()
techsupport_lists = df['TechSupport'].unique().tolist()
techsupport_lists.sort()
contract_lists = df['Contract'].unique().tolist()
contract_lists.sort()
paperlessbilling_lists = df['PaperlessBilling'].unique().tolist()
paperlessbilling_lists.sort()
paymentmethod_lists = df['PaymentMethod'].unique().tolist()
paymentmethod_lists.sort()


@predict.route('/', methods=["POST", "GET"])
def predict_index():
    SeniorCitizen = " "
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
        return render_template('homepage/predict_index.html', seniorcitizen_lists=seniorcitizen_lists,
                               partner_lists=partner_lists, dependents_lists=dependents_lists,
                               onlinesecurity_lists=onlinesecurity_lists, techsupport_lists=techsupport_lists,
                               contract_lists=contract_lists, paperlessbilling_lists=paperlessbilling_lists,
                               paymentmethod_lists=paymentmethod_lists)
    else:
        para_list = []
        SeniorCitizen = para_list.append(request.form["SeniorCitizen"])
        Parnter = para_list.append(request.form["Parnter"])
        Dependents = para_list.append(request.form["Dependents"])
        tenure = para_list.append(exe.convint(request.form["tenure"]))
        OnlineSecurity = para_list.append(request.form["OnlineSecurity"])
        TechSupport = para_list.append(request.form["TechSupport"])
        Contract = para_list.append(request.form["Contract"])
        PaperlessBilling = para_list.append(request.form["PaperlessBilling"])
        PaymentMethod = para_list.append(request.form["PaymentMethod"])
        MonthlyCharges = para_list.append(request.form["MonthlyCharges"])
        result = temp.supervised_classification.Tele_Customer_Churn_0602(
            para_list)
        if result:
            result = 'Will Be Churned.'
        else:
            result = 'Will Be Stay With Us.'
        return render_template('homepage/predict_index.html', SeniorCitizen=SeniorCitizen,
                               Partner=Partner, Dependents=Dependents, tenure=tenure,
                               OnlineSecurity=OnlineSecurity, TechSupport=TechSupport,
                               Contract=Contract, PaperlessBilling=PaperlessBilling,
                               PaymentMethod=PaymentMethod, MonthlyCharges=MonthlyCharges,
                               result=result)
