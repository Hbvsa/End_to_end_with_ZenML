from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline, STAGE_NAME
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline, STAGE_NAME as STAGE_NAME_2
from src.cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline, STAGE_NAME as STAGE_NAME_3

from src.cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

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

        logger.info(f"*******************")
        logger.info(f">>>> stage {STAGE_NAME_3} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME_3} completed <<<<")

        STAGE_NAME = "Evaluation stage"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evalution = EvaluationPipeline()
        model_evalution.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e

