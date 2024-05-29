# End to end project using ZenML. The project uses ZenML to build data ingestion, training, evaluation pipelines with MLFlow integrated to monitor the model performance. The model is also deployed using MLFlow integrated with ZenML.

## Workflows
1. In src folder code classes which are necessary to execute the steps of a pipeline.
2. In the steps folder create a function which initiates and runs the classes. Use @step above the function to make it a step of the ZenML.
3. In the pipeline folder create a pipeline function to execute multiple step functions. Use @pipeline above the function to make it a pipeline of the ZenML.
4. Execute all pipelines in a python script.
