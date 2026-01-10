#beta agent for fast execution

from agents import Agent, Runner

# Cache class/method references locally
AgentCls = Agent
RunnerRun = Runner.run_sync

# Initialize agent
agent = AgentCls(name="Assistant", instructions="You are a helpful assistant")

# Run and get output with minimal lookups
res_final_output = RunnerRun(agent, "Write a haiku about recursion in programming.").final_output

print(res_final_output)