import sys
import pandas as pd 
from src.exception import CustomException
from src.utils import load_object 


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        preprocessor_path="artifacts/preprocessor.pkl"
        model_path="artifacts/model.pkl"
        preprocessor=load_object(file_path=preprocessor_path)
        model=load_object(file_path=model_path)
        


class customData:
    def __init__(self,gender,race_ethinicity,parental_level_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender=gender
        self.race_ethinicity=race_ethinicity
        self.parental_level_education=parental_level_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict={
                "gender":[self.gender],
                "race_ethinicity":[self.race_ethinicity],
                "parental_level_of_education":[self.parental_level_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]

            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)