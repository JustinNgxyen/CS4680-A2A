from client.client import A2AClient

def main() -> None:
    agent_url = "https://echo-a2a-agent-701351129873.us-central1.run.app"

    with A2AClient(agent_url) as client:
        card = client.fetch_agent_card()

        agent_name = card.get("name", "<unknown>")
        skills = client.get_skills()

        print(f"Agent name: {agent_name}")
        print("Skills:")
        if skills:
            for skill in skills:
                if isinstance(skill, dict):
                    print(f"  - {skill.get('name', skill)}")
                else:
                    print(f"  - {skill}")
        else:
            print("  (none)")

        response = client.send_task("Hello from the client!")
        echoed = client.extract_text(response)

        print("\nResponse:")
        print(echoed)


if __name__ == "__main__":
    main()