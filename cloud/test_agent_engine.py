from vertexai.preview import reasoning_engines
import vertexai

PROJECT_ID = "project-5bc66b5c-7c93-4826-9f5"
REGION = "us-central1"

vertexai.init(project=PROJECT_ID, location=REGION)

agent = reasoning_engines.ReasoningEngine(
    "projects/701351129873/locations/us-central1/reasoningEngines/3308360668989620224"
)

response = agent.query(message_text="Hello from Agent Engine!")
print(response)