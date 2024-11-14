from src.dataScience import logger 
from src.dataScience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.dataScience.pipeline.data_validation_pipeline import DataValidationPipeline

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