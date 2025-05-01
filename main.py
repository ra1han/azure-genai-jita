import openai
import json
import os
from openai import AzureOpenAI


# ------------------ Define Tools -------------------

# Load tools from tools.json file
with open(os.path.join('tools', 'tools.json'), 'r') as f:
    TOOLS = json.load(f)

# ------------------ Planner Tool -------------------

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
                            "arguments": {"type": "object"}
                        },
                        "required": ["step", "function"]
                    }
                }
            },
            "required": ["plan"]
        }
    }
}

# ------------------ Planning & Execution -------------------

# 🔹 Function to request a plan from OpenAI
def generate_plan(goal):
    messages = [
        {"role": "system", "content": f"You are a software architect who designs reference architectures. You have a set of certified tools. You prioritize the use of the certified tools over any other tools. If a task can't be developed using the cretified tools, you recommend cusotm steps. Certified tools: {json.dumps(TOOLS)}"},
        {"role": "user", "content": goal}
    ]

    client = AzureOpenAI(
        api_key=os.getenv('AZURE_OPENAI_API_KEY'),
        api_version='2024-02-15-preview',
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )

    response = client.chat.completions.create(
        model="gpt-4",  # or your actual deployment name
        messages=messages,
        tools=[generate_plan_tool],
        tool_choice={"type": "function", "function": {"name": "generate_plan"}},
        # tool_parameter=json.dumps({"goal": goal, "available_tools": TOOLS})
    )

    # Extract the tool call result
    tool_call = response.choices[0].message.tool_calls[0]
    plan_json = json.loads(tool_call.function.arguments)
    
    return plan_json.get("plan", [])

# 🔹 Function to display the plan
def display_plan(plan):
    print("\n🛠️ Execution Plan Generated:")
    for step in plan:
        print(f"🔹 Step {step['step']}: Call `{step['function']}` with args {step.get('arguments', {})}")

# 🔹 Function to save plan to a README file
def save_plan_to_readme(user_goal, plan):
    readme_path = os.path.join('ra', 'README.md')
    
    # Create content for README
    content = f"# Execution Plan\n\n## User Goal\n\n{user_goal}\n\n## Generated Plan\n\n"
    for step in plan:
        content += f"### Step {step['step']}: {step['function']}\n\n"
        if 'arguments' in step and step['arguments']:
            content += "Arguments:\n```json\n"
            content += json.dumps(step['arguments'], indent=2)
            content += "\n```\n\n"
    
    # Save to file
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"\n✅ Plan saved to {readme_path}")

# 🔹 Main program
if __name__ == "__main__":
    user_goal = "Develop a plan of actions that does the following things - develops two new custom metrics which can be used with azure ai evalution sdk and then register those to AI foundry and run a cloud evalution. Finally make a CI pipeline which triggers every time there is a pull request against the main branch. The pipeline should run the evaluation using the two custom evaluators."
    print(f"\n🎯 Generating plan for: {user_goal}")

    # Generate plan from OpenAI
    execution_plan = generate_plan(user_goal)

    # Display the execution plan
    display_plan(execution_plan)
    
    # Ask user if they want to save the plan
    save_choice = input("\n💾 Do you want to save this plan? (Y/N): ")
    if save_choice.upper() == 'Y':
        save_plan_to_readme(user_goal, execution_plan)

