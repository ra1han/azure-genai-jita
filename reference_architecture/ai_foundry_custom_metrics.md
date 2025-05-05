## User Goal

Develop an action plan that does the following:                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric to calculate the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.                    - Registers the two custom metrics in Azure AI Foundry.                    - Uploads a local jsonl file to AI Foundry and creates a dataset in Azure AI Foundry.                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.                    

## Constrain

All code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder. Except github workflow, which needs to be in a seperate directory.

## Execution Plan

### Step 1: custom_evaluator

Arguments:
```json
"Implement a new custom evaluator to measure length of input text."
```

### Step 2: custom_llm_judge_evaluator

Arguments:
```json
"Implement a custom evaluator that uses an LLM to detect obscenity in the input text."
```

### Step 3: register_evaluator_aif

Arguments:
```json
"Register the two new custom evaluators (length metric and obscenity detection metric) with Azure AI Foundry."
```

### Step 4: create_dataset_aif

Arguments:
```json
"Upload the local JSONL file to Azure AI Foundry and create a new dataset for future experiments."
```

### Step 5: cloud_exp

Arguments:
```json
"Run a cloud evaluation with the newly registered metrics, referencing an existing dataset in Azure AI Foundry."
```

