## User Goal

Develop an action plan that does the following:                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric to calculate the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.                    - Registers the two custom metrics in Azure AI Foundry.                    - Uploads a local jsonl file to AI Foundry and creates a dataset in Azure AI Foundry.                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.                    

## Constrain

All code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder. Except github workflow, which needs to be in a seperate directory.

## Execution Plan

### Step 1: custom_evaluator

Check tools/custom_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Create a new custom evaluator metric that calculates the length of the input using the Azure AI Evaluation SDK."
```

### Step 2: custom_llm_judge_evaluator

Check tools/custom_llm_judge_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Create a new custom metric that uses an LLM to detect obscenity in the input."
```

### Step 3: register_evaluator_aif

Check tools/register_evaluator_aif folder for sample implementation of custom evaluator.

Arguments:
```json
"Register the two newly created custom metrics in Azure AI Foundry."
```

### Step 4: upload_dataset_aif

There is no sample implementation, generate your own code.

Arguments:
```json
"Upload the local JSONL file to Azure AI Foundry and create a new dataset from that file."
```

### Step 5: cloud_exp

Check tools/cloud_exp folder for sample implementation of custom evaluator.

Arguments:
```json
"Run a cloud evaluation using the existing dataset in Azure AI Foundry with the newly registered custom metrics."
```

