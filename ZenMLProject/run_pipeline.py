from pipelines.training_pipeline import training_pipeline

if __name__ == '__main__':
    from zenml.client import Client
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    training_pipeline()

#mlflow ui --backend-store-ui "file:C:\Users\hbvs9\AppData\Roaming\zenml\local_stores\10cacc46-20e0-4452-9b9e-76b62c6979e6\mlruns"