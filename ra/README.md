# Execution Plan

## User Goal

Develop a plan of actions that does the following things - develops two new custom metrics which can be used with azure ai evalution sdk and then register those to AI foundry and run a cloud evalution. Finally make a CI pipeline which triggers every time there is a pull request against the main branch. The pipeline should run the evaluation using the two custom evaluators.

## Generated Plan

### Step 1: Develop two new custom metrics to be used with Azure AI Evaluation SDK. This will involve understanding the problem, defining metrics that help achieve the business goal, and coding these metrics following the SDK's framework.

### Step 2: Test the custom metrics extensively. Ensure they work as expected, handle edge cases, and provide insightful results that aid decision-making.

### Step 3: Use the `register_evaluator_aif` to register the new custom evaluators to Azure AI Foundry. Ensure that the evaluators are correctly registered and usable within the ecosystem.

### Step 4: Use the `cloud_exp` to run an experiment in the cloud on Azure AI Foundry using the registered evaluators. This will be an iterative process where results from the run are analyzed, issues are addressed, and the experiment is rerun until the desired outcome is achieved.

### Step 5: Develop a CI pipeline that gets triggered every time a pull request is made onto the main branch. This pipeline should automates the experiment execution process, ensuring that the quality of code pushed into the main branch is maintained.

### Step 6: Integrate the evaluators into the CI pipeline, so that every time it triggers, the evaluation using the custom evaluators runs. This ensures that at every stage the model's performance metrics are kept in check.

### Step 7: Monitor the system, particularly after pull requests, to check the CI pipeline and the evaluators are running as expected. Quickly address any issues that may come up.

