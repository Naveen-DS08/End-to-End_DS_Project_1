from src.dataScience import logger 
from src.dataScience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.dataScience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.dataScience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.dataScience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.dataScience.pipeline.model_evaluation_pipeline import ModelEvaluationPipilne

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage --> {STAGE_NAME} Started <<<<< ")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>> Stage --> {STAGE_NAME} Completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> Stage --> {STAGE_NAME} Started <<<<< ")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>> Stage --> {STAGE_NAME} Completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> Stage --> {STAGE_NAME} Started <<<<< ")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>> Stage --> {STAGE_NAME} Completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>> Stage --> {STAGE_NAME} Started <<<<< ")
    obj = ModelTrainerPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>> Stage --> {STAGE_NAME} Completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Evaluation Stage"

try:
    logger.info(f">>>>> Stage --> {STAGE_NAME} Started <<<<< ")
    obj = ModelEvaluationPipilne()
    obj.initiate_model_evaluation()
    logger.info(f">>>>> Stage --> {STAGE_NAME} Completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e
        