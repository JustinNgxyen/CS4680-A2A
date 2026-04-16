# Virtual Environment
## Windows Powershell
python -m venv .venv
.\.venv\Scripts\activate.bat

# Install client/server dependencies
- pip install -r server/requirements.txt
- pip install httpx
- pip install "google-cloud-aiplatform[agent_engines]"

# Install and configure Google Cloud CLI
- Install Google Cloud CLI
- Run gcloud auth login
- Run gcloud auth application-default login
- Set the project:
gcloud config set project project-5bc66b5c-7c93-4826-9f5

# Start Docker Desktop

# Running the Local Server from project root
uvicorn server.main:app --host 0.0.0.0 --port 8000

# Running the Local Client Demo
set URL in client/demo.py: agent_url = "http://localhost:8000"
Run: python -m client.demo

# Deploying to Cloud Run
./cloud/deploy_cloud_run.sh
URL: https://echo-a2a-agent-701351129873.us-central1.run.app
Run: python -m client.demo

#Deploying to Vertex AI Agent Engine
1. Create the staging bucket
gsutil mb -l us-central1 gs://project-5bc66b5c-7c93-4826-9f5-a2a-staging
2. Deploy the agent engine
python cloud/deploy_agent_engine.py
3. Record the Engine ID
4. Test the deployed engine
Set the engine resource name in cloud/test_agent_engine.py, then run:
python cloud/test_agent_engine.py

Cloud Run Service URL:
https://echo-a2a-agent-njz24rvifq-uc.a.run.app

*Note: I used Claude and ChatGPT to help with error debugging.
