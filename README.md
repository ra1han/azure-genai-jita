# TDD - Tool Driven Development

### Current Challenges 

- With existing end to end accelarators, when we need few parts of it, it's difficult to use that.

### Workflow

- Tools dir will have the implementation of the tools. Each tool will have a structured readme that summarises the purpose and the implementation of the tool. Structure of the README

        Purpose
        Dependency
        Implementation

- Tools dir will have a tools.jsonl which is a summary of all the tools.

- For any new RA, there will be a new dir under the ra dir. This dir will have a behaviour.json which will summarise the behaviour of the new ra.

- The prompt will generate a plan for the RA using function call and store in the RA dir.

- Copilot agent mode will generate a new RA using the plan. It will also generate eval prompt to evalute the new RA.

### Usecase - AI Foundry DevOps

This usecase demonstrates an end to end workflow of evaluating and deploying an Azure Function (w/ LLM usage). Project structure -

1. Az Function: It uses a prompt to detect phishing URLs
2. Data: It has a dataset of phishing URLs
3. Tools: It has the following tools -
 - Run local eval
 - Run cloud eval
 - Build Evaluators
 - IaC - Deploy Evaluators
 - IaC - Az Func
 - Deploy Az Func
 - CI workflow for ???
 - CD workflow for Evaluators
 - CD workflow for Az Func 
 4. `hyvec.py` file to use function calling to get a plan for a specific requirement. Like I want to create new evaluators and get associated CI/CD workflows in a new folder. It will leverage assocaited evals for each tool to generate eval plan.


copilot prompt - ai_foundry_custom_metrics.md has a user goal and steps to implement a solution for that goal. Follow the steps to implement the goal.


