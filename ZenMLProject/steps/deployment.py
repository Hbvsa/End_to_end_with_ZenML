from typing import Optional

from zenml import pipeline, step, get_step_context
from zenml.client import Client
from mlflow.tracking import MlflowClient, artifact_utils
from zenml.integrations.mlflow.services import MLFlowDeploymentService, MLFlowDeploymentConfig


@step
def deploy_model(score: float):
    # Deploy a model using the MLflow Model Deployer
    zenml_client = Client()
    model_deployer = zenml_client.active_stack.model_deployer
    model_uri = zenml_client.get_artifact_version(name_id_or_prefix="model").uri
    client = MlflowClient()
    mlflow_deployment_config = MLFlowDeploymentConfig(
        name="mlflow-model-deployment-example",
        description = "An example of deploying a model using the MLflow Model Deployer",
        pipeline_name= get_step_context().pipeline.name,
        pipeline_step_name= get_step_context().step_run.name,
        model_uri= model_uri,
        model_name = 'model',
        workers= 1,
        mlserver = False,
        timeout = 300,
    )
    service = model_deployer.deploy_model(config=mlflow_deployment_config)
    return service