import os
import sys

import vertexai
from vertexai.preview import reasoning_engines

PROJECT_ID = "project-5bc66b5c-7c93-4826-9f5"
REGION = "us-central1"
STAGING = f"gs://{PROJECT_ID}-a2a-staging"

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from server.agent_engine_wrapper import EchoAgent

vertexai.init(
    project=PROJECT_ID,
    location=REGION,
    staging_bucket=STAGING,
)

remote_agent = reasoning_engines.ReasoningEngine.create(
    EchoAgent(),
    requirements=[
        "google-cloud-aiplatform[reasoningengine]==1.93.0",
        "fastapi==0.111.0",
        "uvicorn==0.29.0",
        "pydantic==2.11.1",
    ],
    extra_packages=["./server"],
    display_name="Echo A2A Agent",
    description="A2A Lab - Echo Agent on Agent Engine",
)

print("Deployed! Resource name:", remote_agent.resource_name)
print("Engine ID:", remote_agent.resource_name.split("/")[-1])