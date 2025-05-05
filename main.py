import json
import os
from openai import AzureOpenAI

generate_plan_tool = {
    "type": "function",
    "function": {
        "name": "generate_plan",
        "description": "Generate a plan to solve the user task using available tools",
        "parameters": {
            "type": "object",
            "properties": {
                "plan": {
                    "type": "array",
                    "description": "Array of steps to execute",
                    "items": {
                        "type": "object",
                        "properties": {
                            "step": {"type": "integer"},
                            "function": {"type": "string"},
                            "arguments": {"type": "string"}
                        },
                        "required": ["step", "function", "arguments"],
                    }
                }
            },
            "required": ["plan"]
        }
    }
}

def generate_plan(goal):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": goal}
    ]

    client = AzureOpenAI(
        api_key=os.getenv('AZURE_OPENAI_API_KEY'),
        api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )

    response = client.chat.completions.create(
        model=os.getenv('AZURE_OPENAI_DEPLOYMENT'),
        messages=messages,
        tools=[generate_plan_tool],
        tool_choice={"type": "function", "function": {"name": "generate_plan"}},
        # tool_parameter=json.dumps({"goal": goal, "available_tools": TOOLS})
    )

    tool_call = response.choices[0].message.tool_calls[0]
    plan_json = json.loads(tool_call.function.arguments)
    
    return plan_json.get("plan", [])

def display_plan(plan):
    print("\n🛠️ Execution Plan Generated:")
    for step in plan:
        print(f"🔹 Step {step['step']}: Call `{step['function']}` with args {step.get('arguments', {})}")

def save_plan_to_readme(ra_title, user_goal, plan):
    readme_path = os.path.join('reference_architecture', f'{ra_title}.md')
    
    # Read tools from tools.jsonl
    available_tools = []
    with open(os.path.join('tools', 'tools.jsonl'), 'r') as f:
        for line in f:
            if line.strip():
                tool = json.loads(line)
                available_tools.append(tool.get('name'))
    
    content = f"## User Goal\n\n{user_goal}\n\n\
                ## Constrain\n\nAll code changes should involve only new code generation without modifying existing code. Place all new code in the reference_architecture folder. Except github workflow, which needs to be in a seperate directory.\n\n\
                ## Execution Plan\n\n"
    for step in plan:
        content += f"### Step {step['step']}: {step['function']}\n\n"
        # Check if the function exists in tools.jsonl
        if step['function'] in available_tools:
            content += f"Check tools/{step['function']} folder for sample implementation of custom evaluator.\n\n"
        else:
            content += "There is no sample implementation, generate your own code.\n\n"
        
        if 'arguments' in step and step['arguments']:
            content += "Arguments:\n```json\n"
            content += json.dumps(step['arguments'], indent=2)
            content += "\n```\n\n"
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"\n✅ Plan saved to {readme_path}")

def load_system_prompt():
    with open(os.path.join('tools', 'tools.jsonl'), 'r') as f:
        tools = f.read()

    with open(os.path.join('prompts', 'planner_system_prompt.md'), 'r') as f:
        system_prompt = f.read()

    system_prompt = system_prompt.replace("{{tools}}", json.dumps(tools))

    return system_prompt

if __name__ == "__main__":
    ra_title = "ai_foundry_custom_metrics"
    user_goal = "Develop an action plan that does the following:\
                    - Creates two new custom metrics compatible with the Azure AI Evaluation SDK. One metric to calculate the length of the input. The other metric uses LLM as judge to detect any obscenity in the input.\
                    - Registers the two custom metrics in Azure AI Foundry.\
                    - Uploads a local jsonl file to AI Foundry and creates a dataset in Azure AI Foundry.\
                    - Runs a cloud evaluation using the two metrics which uses an existing dataset in Azure AI Foundry.\
                    "
    
    system_prompt = load_system_prompt()

    print(f"\n🎯 Generating plan for: {user_goal}")

    execution_plan = generate_plan(user_goal)

    display_plan(execution_plan)
    
    save_choice = input("\n💾 Do you want to save this plan? (Y/N): ")
    if save_choice.upper() == 'Y':
        save_plan_to_readme(ra_title, user_goal, execution_plan)

