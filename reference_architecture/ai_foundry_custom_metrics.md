## User Goal
Develop an action plan that does the following:                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric to calculate the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.                    - Registers the two custom metrics in Azure AI Foundry.                    - Uploads a local jsonl file to AI Foundry and creates a dataset in Azure AI Foundry.                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.                    

## Constrain
All code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder.

## Execution Plan


### Step 1: custom_evaluator

Check tools/custom_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Implement the first custom metric to calculate the length of the input and place it into a separate folder compatible with Azure AI Evaluation SDK."
```

### Step 2: custom_llm_judge_evaluator

Check tools/custom_llm_judge_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Implement the second custom metric using LLM as judge to detect any obscenity in the input. Place this implementation into its own folder compatible with Azure AI Evaluation SDK."
```

### Step 3: register_evaluator_aif

Check tools/register_evaluator_aif folder for sample implementation of custom evaluator.

Arguments:
```json
"Register the two custom metrics implemented in steps 1 and 2 to Azure AI Foundry."
```

### Step 4: register_dataset_aif

Check tools/register_dataset_aif folder for sample implementation of custom evaluator.

Arguments:
```json
"Upload a local jsonl file and register it as a dataset in Azure AI Foundry."
```

### Step 5: cloud_exp

Check tools/cloud_exp folder for sample implementation of custom evaluator.

Arguments:
```json
"Run a cloud evaluation using the two registered metrics on an existing dataset in Azure AI Foundry."
```

