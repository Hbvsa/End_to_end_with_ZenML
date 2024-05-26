from cnnClassifier import logger
from cnnClassifier.pipeline import stage_01_data_ingestion
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline, STAGE_NAME
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline, STAGE_NAME as STAGE_NAME_2

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed<<<<")

        logger.info(f"*******************")
        logger.info(f">>>> stage {STAGE_NAME_2} started <<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME_2} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e


