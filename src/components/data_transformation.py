import sys
from dataclasses import dataclass
import os
from src.utils import save_object

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
 preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            ##Check for EDA analysis 
            numerical_cols = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
            'BILL_AMT1', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5',
            'PAY_AMT6']
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('scaler',StandardScaler())
                ]
            )
            preprocessor=ColumnTransformer([('num_pipeline',num_pipeline,numerical_cols)])
            logging.info('Pipeline Completed')
            return preprocessor

        except Exception as e:
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        try:
            ## Reading train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')
            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name='Payment_default'
            drop_columns = [target_column_name,'ID','PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT2',
                'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']
            ## Renaming Target Column names

            train_df.rename(columns={'default.payment.next.month':'Payment_default'},inplace=True)
            test_df.rename(columns={'default.payment.next.month':'Payment_default'},inplace=True)

            ## Dropping Columns
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df= pd.DataFrame(train_df[target_column_name])
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df= pd.DataFrame(test_df[target_column_name])

            print(f"Train DF: {type(input_feature_train_df)}")
            print(f"Target DF:{type(target_feature_train_df)}")

            ## Transforming using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)
