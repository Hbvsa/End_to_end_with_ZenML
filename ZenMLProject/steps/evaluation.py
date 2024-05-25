import logging
import pandas as pd
from zenml import step
from src.evaluation import MSE, RMSE, R2
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated
import numpy as np
from zenml.client import Client
import mlflow
experiment_tracker = Client().active_stack.experiment_tracker


@step(experiment_tracker=experiment_tracker.name)
def evaluate_model(model: RegressorMixin,X_test: pd.DataFrame, y_test: pd.DataFrame) -> Tuple[
    Annotated[float, "r2"],
    Annotated[float, "rmse"],
    ]:
    '''
    Evalutes the model on the ingested data.
    Args:
        df: the ingested data
    '''

    try:
        y_pred = model.predict(X_test)

        mse_class = MSE()
        mse = mse_class.calculate_scores(y_test, y_pred)
        mlflow.log_metric("mse",mse)

        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test, y_pred)
        mlflow.log_metric("rmse", rmse)

        r2_class = R2()
        r2 = r2_class.calculate_scores(y_test, y_pred)
        mlflow.log_metric("r2", r2)
        return r2, rmse

    except Exception as e:
        logging.error(f"Error in evaluating model {e}")
        raise e

