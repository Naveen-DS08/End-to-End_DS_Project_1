from pathlib import Path
from src.dataScience import logger 
from src.dataScience.config.configuration import ConfigurationManager 
from src.dataScience.comkponents.model_trainer import ModelTrainer

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

 