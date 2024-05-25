import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreprocessStrategy
from typing import Tuple
from typing_extensions import Annotated
@step
def clean_data(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"]
    ]:
    '''
    Cleans the data and divides into train and test

    Args:
        df: Raw Data

    Returns:
        X_train: Training data
        X_test: Testing data
        y_train: Training labels
        y_test: Testing labels
    '''
    try:
        process_strategy = DataPreprocessStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, divide_strategy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data cleaning completed")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        logging.error(f"Error in cleaning data {e} ")
        raise e

