import os
import sys
from dotenv import load_dotenv

# Add parent directory to path so we can import from sibling directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from azure.ai.evaluation import evaluate, RelevanceEvaluator, EvaluatorConfig
from custom_llm_judge_evaluator.friendliness_evaluator import FriendlinessEvaluator
from custom_evaluator.length_evaluator import LengthEvaluator

load_dotenv()

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
}

evaluators = {
    "relevance": RelevanceEvaluator(model_config=model_config),
    "friendliness": FriendlinessEvaluator(model_config=model_config),
    "length": LengthEvaluator()
}

evaluator_config = {
    "relevance": EvaluatorConfig(
        column_mapping={
            "query": "${data.question}",
            "response": "${data.answer}"
        }
    ),
    "friendliness": EvaluatorConfig(
        column_mapping={
            "response": "${data.answer}"
        }
    ),
    "length": EvaluatorConfig(
        column_mapping= {
            "response": "${data.answer}"
        } 
    )
}

# Use absolute path for the data file
data_file_path = os.path.join(current_dir, "qna.jsonl")

results = evaluate(
    data=data_file_path,
    evaluators=evaluators,
    evaluator_config=evaluator_config,
    evaluation_name="Local Evaluation Run",
    fail_on_evaluator_errors=True,
    output_path=os.path.join(current_dir, "custom_batch_eval.json")
)

print(f"Results: {results}")