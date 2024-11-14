from src.dataScience.config.configuration import ConfigurationManager
from src.dataScience.comkponents.data_validation import DataValidation
from src.dataScience import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_ingestion_config)
        data_ingestion.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage --> {STAGE_NAME} Started <<<<< ")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>> Stage --> {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
        
