import logging
import pandas as pd
from zenml import step
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig
from zenml.client import Client
import mlflow
from typing_extensions import Annotated
experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def model_train(X_train: pd.DataFrame, y_train: pd.DataFrame, config: ModelNameConfig) -> Annotated[RegressorMixin, "model"]:
    '''
    Trains model

    Args:
        df: the ingested data
    '''
    try:
        model = None

        if config.model_name == 'LinearRegression':
            mlflow.sklearn.autolog()
            model = LinearRegressionModel()
            trained_model = model.train(X_train, y_train)
            return trained_model

        else:
            raise ValueError(f"Model {ModelNameConfig.model_name} not supported")

    except Exception as e:
        logging.error(f"Error in training model {e}")
        raise e
    