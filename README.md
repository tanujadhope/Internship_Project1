## Credit-Card-Default-Prediction
## This is an End to End Machine Learning  project, used to predict credit card defaulter.The project is deployed on AWS 

## Overview
```
This is a classification model for a most common dataset, Credit Card defaulter prediction. Prediction of the next month credit card defaulter based on demographic and last six months behavioral data of customers
```

## Motivation
```
Credit risk is very important in the banking industry. Banks' primary businesses include lending, credit card, investment, mortgage, and other services. Credit cards have been one of the most successful financial services offered by banks in recent years. However, as the number of credit card users grows, banks face an increasing credit card default rate. In fасt, сredit саrd debts аrе usuаllу the first tо gеt оut оf hаnd in suсh situаtiоns due tо costly finаnсe сhаrges (соmроundеd оn dаily bаlаnсеs) аnd оthеr penalties. We may have missed credit card payments once or twice due to missing due dates or cash flow concerns. But what happens when this goes on for months? How do you predict if a customer will be deficient in the next months? As a result, data analytics can provide answers for dealing with the current issue and managing credit risks. In this project, machine learning based model has been develорed tо рrediсt customer defaulter based оn demоgrарhiс dаtа like gender, аge, marital stаtus аnd behаviоrаl dаtа like lаst раyments, раst trаnsасtiоns etс.```

## Information about Dataset
```
This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.Total 25 columns are presents in the dataset.
Information About Dataset
ID: ID of each client

LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary = credit)

SEX: Gender (1=male, 2=female)

EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)

MARRIAGE: Marital status (1=married, 2=single, 3=others)

AGE: Age in years

PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)

PAY_2: Repayment status in August, 2005 (scale same as above)
 PAY_3: Repayment status in July, 2005 (scale same as above) PAY_4: Repayment status in June, 2005 (scale same as above) PAY_5: Repayment status in May, 2005 (scale same as above)
 
PAY_6: Repayment status in April, 2005 (scale same as above) 
BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar) 
BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar) 
BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar) BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar) 
PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar) 
PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar) 
PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar) 
PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar) 
PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar) 
default.payment.next.month: Default payment (1=yes, 0=no)

## How to run this app


### create a virtual environment :conda create -n credit_card_defaulter python==3.7                                           
### activate the virtual environment :conda activate credit_card_defaulter
### Install all necessary libraries in requirements.txt:pip install -r requirements.txt
### Run app.py 
### Enter the value as per HTML form 
### click on Predict
### Result will be either 'Defaulter' or 'Not DEfaulter'




# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 
# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access
 
	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws

    #Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = 

    AWS_ECR_LOGIN_URI = 

    ECR_REPOSITORY_NAME = 

	
### follow these all steps

### 

## Project Documents:
### Project DPR:[https://github.com/tanujadhope/Internship_Project1/blob/main/Documentations/Credit_Card_Default.mp4]
### Project code demo:https://github.com/tanujadhope/Internship_Project1/blob/main/Documentations/Code%20demo.mp4
# Author
https://www.linkedin.com/in/tanujadhope/



