import logging
import pandas as pd
from zenml import step

class IngestData:
    """
    Ingesting the data from the data_path.
    """
    def __init__(self):
        """
        Args:
            data_path: path to the data
        """
        pass

    def get_data(self):
        """
        Ingesting the data from the data_path.
        """
        logging.info(f"Ingesting data ")
        return pd.read_csv(r'data/olist_customers_dataset.csv')

@step
def ingest_data()-> pd.DataFrame:
    """
    Ingesting the data from the data_path.
    Returns:
        pd.DataFrame: the ingested data
    """
    try:
        ingest_data = IngestData()
        df = ingest_data.get_data()
        return df

    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e