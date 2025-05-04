## User Goal

Develop an action plan that does the following:                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric uses calculates the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.                    - Registers the two custom metrics in Azure AI Foundry.                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.                    

## Constrain

All code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder.

## Execution Plan

For each Tool name, there is a corresponding folder under the tools directory that contains sample code demonstrating a similar action.

### Step 1: 

Tool: custom_evaluator

Arguments:
```json
"Create a custom evaluator for Azure AI evaluation library that measures the length of the input."
```

### Step 2: 

Tool: custom_llm_judge_evaluator

Arguments:
```json
"Create a second custom evaluator using LLM as judge to detect any obscenity in the input."
```

### Step 3: 

Tool: register_evaluator_aif

Arguments:
```json
"Register both custom evaluators to Azure AI Foundry."
```

### Step 4: 

Tool: cloud_exp

Arguments:
```json
"Run a cloud evaluation using the registered evaluators on an existing dataset in Azure AI Foundry."
```

