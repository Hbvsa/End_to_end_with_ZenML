import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
class Evaluation(ABC):

    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        pass



class MSE(Evaluation):

    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:

        try:
            mse = mean_squared_error(y_true, y_pred)
            logging.info(f"MSE - {mse}")
            return mse

        except Exception as e:
            logging.error(f"Error in calculating MSE Loss {e}")
            raise e

class R2(Evaluation):

    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:

        try:
            r2 = r2_score(y_true, y_pred)
            logging.info(f"R2 Score - {r2}")
            return r2

        except Exception as e:
            logging.error(f"Error in calculating R2 Score {e}")
            raise e

class RMSE(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:

        try:
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            logging.info(f"RMSE - {rmse}")
            return rmse

        except Exception as e:
            logging.error(f"Error in calculating RMSE Loss {e}")
            raise e