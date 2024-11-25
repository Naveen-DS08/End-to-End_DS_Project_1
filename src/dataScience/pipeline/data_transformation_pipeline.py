from src.dataScience.config.configuration import ConfigurationManager
from src.dataScience.comkponents.data_transformation import DataTransformation
from src.dataScience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass 
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                cofig = ConfigurationManager()
                data_transformation_config = cofig.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_splittig()
            else:
                raise Exception("Your data schema is not valid")
        
        except Exception as e:
            print(e)