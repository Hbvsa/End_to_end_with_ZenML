from zenml import step, pipeline, get_step_context
from zenml.client import Client
@step
def test(r2score: float):
    print("Test step")
    step_context = get_step_context()
    pipeline_name = step_context.pipeline.name
    zenml_client = Client()
    dataset_artifact = zenml_client.get_artifact_version(name_id_or_prefix="model").uri
    print(dataset_artifact.uri)
    print(pipeline_name)