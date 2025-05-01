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

ml_client = MLClient(
       subscription_id=os.environ["SUBSCRIPTION_ID"],
       resource_group_name=os.environ["RESOURCE_GROUP"],
       workspace_name=os.environ["AI_FOUNDRY_PROJECT_NAME"],
       credential=DefaultAzureCredential()
)

# Create flow from the custom evaluator
local_path = "dist/FriendlinessEvaluator" # save this evaluation flow in /dist
pf_client = PFClient()
pf_client.flows.save(entry=FriendlinessEvaluator, path=local_path)

evaluator_name = "FriendlinessEvaluator"
custom_evaluator = Model(
    path=local_path,
    name=evaluator_name,
    description="custom prompt evaluator measuring response base on friendliness",
)

# Register the custom evaluator
registered_evaluator = ml_client.evaluators.create_or_update(custom_evaluator)
print("Registered evaluator id:", registered_evaluator.id)

versioned_evaluator = ml_client.evaluators.get(evaluator_name, label="latest")
print("Versioned evaluator id:", versioned_evaluator.version)