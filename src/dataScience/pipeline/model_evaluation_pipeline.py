from pathlib import Path 
from src.dataScience import logger 
from src.dataScience.config.configuration import ConfigurationManager
from src.dataScience.comkponents.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipilne:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.log_into_mlflow()