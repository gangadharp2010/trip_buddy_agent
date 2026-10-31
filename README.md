# Trip Buddy Agent

Trip Buddy Agent is an AI-powered travel planner built with Python, Gradio, OpenAI, and MCP (Model Context Protocol) tools. It helps users explore destinations, estimate trip costs, compare budgets, and get seasonal travel guidance for travel planning in India.

## Features

- AI-powered travel planning assistant
- Destination discovery and budget comparison
- Group trip cost estimation for multiple friends
- Seasonal travel advice using knowledge retrieval
- MCP-powered tool orchestration for travel data and travel knowledge
- Interactive web UI with Gradio
- SQLite-backed demo travel data

## Demo capabilities

The app can help with questions like:

- "Plan a Goa trip for 4 friends for 3 nights"
- "Which destinations fit within ₹8,000 per person?"
- "Is Manali a good idea in July?"
- "How much is Hampi for 5 friends, 2 nights?"

Important: the app uses demo/sample travel estimates and should not be treated as live pricing or booking data.

## Tech stack

- Python 3.10+
- Gradio
- OpenAI Python SDK
- SQLite
- MCP client/server architecture
- Retrieval-augmented knowledge search
- dotenv for environment configuration

## Project structure

```text
trip_buddy_agent/
├── agents/
│   ├── __init__.py
│   └── travel_agent.py
├── data/
├── database/
├── mcp_client/
├── mcp_servers/
│   ├── knowledge_mcp_server.py
│   ├── test_knowledge_mcp.py
│   └── travel_mcp_server.py
├── rag/
├── tools/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── test_agent.py
├── test_knowledge_mcp.py
├── .gitignore
└── trip_buddy.db
```

## How it works

Trip Buddy uses a multi-layered architecture:

1. Gradio frontend renders the chat interface.
2. `TravelAgent` orchestrates travel requests.
3. MCP tools expose travel and knowledge capabilities.
4. The travel MCP server provides destination and budget logic.
5. The knowledge MCP server provides travel guidance and seasonal advice.
6. SQLite stores sample travel data and demo estimates.
7. OpenAI is used for natural-language understanding and tool orchestration when an API key is configured.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gangadharp2010/trip_buddy_agent.git
cd trip_buddy_agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
DATABASE_PATH=trip_buddy.db
```

If you do not provide an OpenAI API key, the app falls back to deterministic MCP-based behavior.

## Run the app

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:7860
```

## Example prompts

```text
Plan Goa for 4 friends, 3 nights
Which trips fit within ₹10,000 per person?
Is Hampi a good winter destination?
How much would a 2-night trip to Manali cost for 3 friends?
```

## Notes and limitations

- The application is designed for demo/travel-planning workflows.
- Costs are sample estimates based on database records.
- Intercity travel, live weather, booking availability, and real-time pricing are not included.
- Always verify official local advisories and live prices before booking travel.

## Roadmap ideas

- Add real API integrations for hotels, flights, and weather
- Support multiple regions and languages
- Improve itinerary generation and recommendations
- Add enhanced RAG sources for local experiences and safety guidance
- Add user authentication and saved trip history

## Contributing

Contributions are welcome. If you want to improve the app:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Open a pull request with a clear description.

## Contact

For questions or collaboration, please open an issue in the repository.
