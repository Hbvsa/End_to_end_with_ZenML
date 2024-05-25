import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
class Model(ABC):
    '''
    Abstract class for all models
    '''

    @abstractmethod
    def train(self, X_train, y_train):
        '''

        :param X_train:
        :param y_train:
        :return:
        '''
        pass

class LinearRegressionModel(Model):
    '''
    Linear Regression model
    '''

    def train(self, X_train, y_train, **kwargs):

        try:

            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return reg

        except Exception as e:

            logging.error(f"Error in training model {e}")
            raise e