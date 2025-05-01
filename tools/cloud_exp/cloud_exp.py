import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.evaluation import RelevanceEvaluator
from custom_evaluator.friendliness_evaluator import FriendlinessEvaluator

from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from promptflow.client import PFClient

from azure.ai.projects.models import (
    Evaluation,
    Dataset,
    EvaluatorConfiguration,
    ConnectionType
)
from azure.mgmt.machinelearningservices import AzureMachineLearningWorkspaces

load_dotenv()

data_id = os.environ["DATA_ID"]
custom_evaluator_id = os.environ["CUSTOM_EVALUATOR_ID"]

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["AI_FOUNDRY_CONNECTION_STRING"]
)
default_connection = project_client.connections.get_default(connection_type=ConnectionType.AZURE_OPEN_AI)
# Create model configuration for evaluators that need a model
model_config = default_connection.to_evaluator_model_config(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)
# Create an evaluation
evaluation = Evaluation(
    display_name="Cloud Evaluation 2",
    description="Cloud Evaluation",
    data=Dataset(id=data_id),
    evaluators={
        "relevance": EvaluatorConfiguration(
            id=RelevanceEvaluator.id, # in-built evaluator id
            init_params={
                "model_config": model_config
            },
            data_mapping={
                "query": "${data.question}",
                "response": "${data.answer}",
            }
        ),
        "friendliness": EvaluatorConfiguration(
            id=custom_evaluator_id, # custom evaluator id
            init_params={
                "model_config": model_config
            },
            data_mapping={
                "response": "${data.answer}",
            }
        ),

    },
)

evaluation_response = project_client.evaluations.create(
    evaluation=evaluation
)