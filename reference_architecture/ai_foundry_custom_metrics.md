## User Goal

Develop an action plan that does the following:                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric to calculate the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.                    - Registers the two custom metrics in Azure AI Foundry.                    - Uploads a local jsonl file to AI Foundry and creates a dataset in Azure AI Foundry.                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.                    

                ## Constrain

All code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder. Except github workflow, which needs to be in a seperate directory.

                ## Execution Plan

### Step 1: custom_evaluator

Check tools/custom_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Create a custom metric that calculates the length of the input. Implement the logic in a Python file that can be recognized by the Azure AI Evaluation SDK."
```

### Step 2: custom_llm_judge_evaluator

Check tools/custom_llm_judge_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Create a custom metric that uses an LLM-based approach to detect obscenity in the input. Implement the logic in a Python file recognized by the Azure AI Evaluation SDK."
```

### Step 3: register_evaluator_aif

Check tools/register_evaluator_aif folder for sample implementation of custom evaluator.

Arguments:
```json
"Register both newly created custom metrics (length-of-input and obscenity-detection) with Azure AI Foundry."
```

### Step 4: upload_jsonl_dataset_to_aif

There is no sample implementation, generate your own code.

Arguments:
```json
"Create a new tool that uploads a local JSONL file to Azure AI Foundry and creates a new dataset."
```

### Step 5: cloud_exp

Check tools/cloud_exp folder for sample implementation of custom evaluator.

Arguments:
```json
"Execute a cloud evaluation in Azure AI Foundry using the newly created metrics on an existing dataset."
```

### Step 6: create_requirements_file

There is no sample implementation, generate your own code.

Arguments:
```json
"Create a requirements.txt file listing necessary dependencies such as azure-ai-evaluation, openai, prompty, and others required for the solution."
```

