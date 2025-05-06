## User Goal
Develop an action plan that does the following:                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric to calculate the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.                    - Registers the two custom metrics in Azure AI Foundry.                    - Uploads a local jsonl file to AI Foundry and creates a dataset in Azure AI Foundry.                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.                    

## Constrain
All code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder.

## Execution Plan
### Step 1: custom_evaluator

Check tools/custom_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Create a new folder for the custom evaluator that calculates the length of the input. Implement a Python class that inherits from the base Evaluator class and override the evaluate method to return the character length of the input text. Include any necessary setup code and ensure that the folder structure is compatible with Azure AI Evaluation SDK."
```

### Step 2: custom_llm_judge_evaluator

Check tools/custom_llm_judge_evaluator folder for sample implementation of custom evaluator.

Arguments:
```json
"Create a new folder for the LLM-based obscenity check evaluator. Implement a Python class that inherits from the base Evaluator class and uses an LLM to classify whether the input contains obscene content. Use the prompty library to craft the prompt that the LLM will respond to and output a Boolean or a score indicating the confidence that the text contains obscenity."
```

### Step 3: register_evaluator_aif

Check tools/register_evaluator_aif folder for sample implementation of custom evaluator.

Arguments:
```json
"Register both the newly created custom evaluators (length metric and obscenity check) with Azure AI Foundry by referencing their folder locations, ensuring the metadata and evaluation configurations are properly set."
```

### Step 4: new_tool_upload_dataset_aif

There is no sample implementation, generate your own code.

Arguments:
```json
"Create a new tool named 'upload_dataset_aif' to upload a local JSONL file to Azure AI Foundry and create a new dataset. The tool should accept parameters like the local file path, a dataset name, and any relevant configuration for establishing the dataset in Azure AI Foundry."
```

### Step 5: cloud_exp

Check tools/cloud_exp folder for sample implementation of custom evaluator.

Arguments:
```json
"Run a cloud experiment referencing an existing dataset in Azure AI Foundry. Configure the experiment to use both custom metrics (the length metric and the LLM-based obscenity detection). Specify the dataset name and evaluator IDs, then trigger the experiment to run in the cloud environment."
```

