# <a href="https://github.com/bdfd"><img height=40 src="https://cdn.jsdelivr.net/gh/bdfd/Personal_Image_Repo/4.Stamp/BDFD_Stamp.png" alt="GitHub Followers" /></a>Telco Customer Churn Prediction

<a href="https://github.com/bdfd"><img src="https://img.shields.io/github/followers/bdfd?label=Follow%20Me&logo=github" alt="GitHub Followers" /></a>
![ViewCount](https://views.whatilearened.today/views/github/bdfd/Section6.Project02-Tele_Customer_Churning_Prediction.svg?cache=remove)
![GitHub top language](https://img.shields.io/github/languages/top/bdfd/Section6.Project02-Tele_Customer_Churning_Prediction?style=flat)
![GitHub language count](https://img.shields.io/github/languages/count/bdfd/Section6.Project02-Tele_Customer_Churning_Prediction?style=flat)
<img height=20 src="https://cdn.jsdelivr.net/gh/bdfd/Personal_Image_Repo/7.Color-Icon/Status/On_Progress.svg" alt="bdfd" />

<!-- <img height=20 src="https://cdn.jsdelivr.net/gh/bdfd/Personal_Image_Repo/7.Color-Icon/Status/Finish.svg" alt="bdfd" /> -->

## Applied Learning Project

<img height="27" src="https://img.shields.io/badge/Prediction using Supervised ML -Level  Intermediate-blue.svg?&style=for-the-badge&logo=TheSparksFoundation&logoColor=red" />  
<!-- <img height="27" src="https://img.shields.io/badge/Prediction using Supervised ML -Level  Advanced-red.svg?&style=for-the-badge&logo=TheSparksFoundation&logoColor=red" /> -->

**Tools:** Colab/Jupyter Notebook, GitHub

**Algorithm Category:** Regression, Classification

**Purpose:** Data Cleaning, Apply Algorithm

**Algorithm:** Univariate Linear Regression, Multivariate Linear Regression

**Package Usage:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Execdata, Scipy, Imblean, Counter

**Projects:** Telco Customer Churn Prediction

**Problem Description**  
In our dataset, Total amount of Monthly charges are around 16,056,169$ from that 18% of amount loss around 2862927% Due to the customer churn.
Total number of customer around 7043 but 27% of people to be churn which around 1869 customer from the overall customer,
So we need to predict the person who are all wants to be churn.Its very important to that company because they want new customer as well as retain the previous customer to stay in there company.

**Problem Task**  
Churn prediction means detecting which customers are likely to cancel a subscription to a service based on how they use the service. It is a critical prediction for many businesses because acquiring new clients often costs more than retaining existing ones. Once you can identify those customers that are at risk of cancelling, you should know exactly what marketing action to take for each individual customer to maximise the chances that the customer will remain.

**Reason For Task**  
Customer churn is a common problem across businesses in many sectors. If you want to grow as a company, you have to invest in acquiring new clients. Every time a client leaves, it represents a significant investment lost. Both time and effort need to be channelled into replacing them. Being able to predict when a client is likely to leave, and offer them incentives to stay, can offer huge savings to a business.

**Problem Variables**  
There are two tables could be merged by ID

| Field            | Description                       | Unit | dtype               | Comments        |
| ---------------- | --------------------------------- | ---- | ------------------- | --------------- |
| Table 1          | Telco-Customer-Churn.csv          |      | Table Name          | ----------      |
| CustomerID       |                                   |      | Random Generate     | Drop Variable   |
| Gender           |                                   |      | Binary Category     | ----------      |
| SeniorCitizen    |                                   |      | Binary Category     | ----------      |
| Partner          |                                   |      | Binary Category     | ----------      |
| Dependents       |                                   |      | Binary Category     | ----------      |
| tenure           | Number of month stay with company |      | Continuous          | ----------      |
| PhoneService     |                                   |      | Tri Category        | ----------      |
| MutipleLines     |                                   |      | Tri Category        | ----------      |
| InternetService  |                                   |      | Tri Category        | ----------      |
| OnlineSecurity   |                                   |      | Tri Category        | ----------      |
| OnlineBackup     |                                   |      | Tri Category        | ----------      |
| DeviceProtection |                                   |      | Tri Category        | ----------      |
| TechSupport      |                                   |      | Tri Category        | ----------      |
| StreamingTV      |                                   |      | Tri Category        | ----------      |
| StreamingMovie   |                                   |      | Tri Category        | ----------      |
| Contarct         |                                   |      | Tri Category        | ----------      |
| PaperlessBilling |                                   |      | Binary Category     | ----------      |
| PaymentMethod    |                                   |      | Non Binary Category | ----------      |
| TotalCharges     |                                   |      | Continous           | ----------      |
| Churn            |                                   |      | Binary Category     | Traget Variable |

**Steps Involved in Model Development:**
Data Analysis (EDA)  
Data Preprocessing  
Feature Engineering  
Feature Selection (SelectKBest)  
Fit into Algorithm (ML Algorithm)  
Hyper Parameter Tunning (RandomSearchCV)  
Dump model (Pickle)  
Creating Web Application using Flask
Deployed in Web using Cloud Platform

**Run Project Procedure:**
In this project, First you need to download dataset Telco-Customer-churn.csv Then open your commant prompt and run this code pip install jupyterlab. After pip install requirements.txt all packages are needed in this project are automatically installed on your machine. After Download app.py files and run TelecomCustomerChurn.ipynb files into your machine And some inputs to check our model and Its accuracy of prediction

**Reference:**

<!-- Resource Reference:<a href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn/"><Resource Name-Kaggle> Kaggle Problem Reference</a>   -->
<!-- Github Reference:<a href="https://github.com/satz2000/End-to-end-project---Customer-churn"><Resource Name-Github> Github Repository</a>   -->

Dateset:<a href="https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_Original_Dataset.csv">Original Dataset.csv</a>  
Dateset:<a href="https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_Preprocessed.csv">Processed Dataset.csv</a>  
Dateset:<a href="https://github.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/blob/main/1.0%20dataset/S602_Mungged.csv">Mugged Dataset.csv</a>  
Train Processed Dataset:<a href="https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_X_train.csv">Train_X.csv</a>,
<a href="https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_y_train.csv">Train_y.csv</a>  
Test Processed Dataset:<a href="https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_X_test.csv">Test_X.csv</a>,
<a href="https://raw.githubusercontent.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/main/1.0%20dataset/S602_y_test.csv">Test_y.csv</a>  
Demo:<a href="https://github.com/bdfd/Section6.Project02-Telco_Customer_Churning_Prediction/blob/main/2.0%20colab/0602-Preprocessed.ipynb">Jupyter Notebook/Colab Link</a>

<!-- Visualization:<a href="https://github.com/bdfd/Section6.Project04_Customer_Segmentation/blob/main/display%20demo/Clustering_Bivariate.png">Train Result</a>,<a href="https://github.com/bdfd/Portfolio_Project_10-Salary_Prediction/blob/main/display%20demo/test%20result.png">Test Result</a> -->
<br>

<div align="center">

### Thanks For Watch This Repositories!

### <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30"><i>KEEP AWESOME & STAY COOL!</i><img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30">

### Feel Free To Fork And Report If You Find Any Issue :)

![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/bdfd?tab=repositories)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/bdfd)

</div>
