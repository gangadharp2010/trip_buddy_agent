
import gradio as gr

from agents.travel_agent import TravelAgent
from database.db_connection import init_db, seed_db


# ============================================================
# 1. INITIALIZE APPLICATION
# ============================================================

print("Initializing Trip Buddy...")

init_db()
seed_db()

agent = TravelAgent()

print("Database initialized successfully!")


# ============================================================
# 2. CUSTOM CSS
# ============================================================

CUSTOM_CSS = """
:root {
    --trip-primary: #0d9488;
    --trip-primary-dark: #0f766e;
    --trip-bg: #f5f8fa;
    --trip-card: #ffffff;
}

.gradio-container {
    max-width: 1450px !important;
    margin: auto !important;
    background: var(--trip-bg) !important;
}

#trip-header {
    background: linear-gradient(120deg, #134e4a, #0d9488);
    color: white;
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 18px;
}

#trip-header h1 {
    color: white !important;
    font-size: 34px !important;
    margin-bottom: 8px;
}

#trip-header p {
    color: #d9fffa !important;
}

#sidebar {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 18px;
}

#chat-panel {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 12px;
}

#chatbot {
    border: none !important;
    border-radius: 14px !important;
}

#message-box textarea {
    border-radius: 14px !important;
    padding: 14px !important;
}

.primary-action {
    background: #0d9488 !important;
    color: white !important;
    border: none !important;
}

.primary-action:hover {
    background: #0f766e !important;
}

.quick-button {
    border-radius: 12px !important;
    text-align: left !important;
    white-space: normal !important;
}

.section-title {
    color: #0f766e;
    font-weight: 700;
}

.footer-note {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 16px;
}

.status-card {
    background: #f0fdfa;
    border: 1px solid #ccfbf1;
    border-radius: 12px;
    padding: 12px;
}

@media (max-width: 768px) {
    #trip-header {
        padding: 20px;
    }

    #trip-header h1 {
        font-size: 26px !important;
    }
}
"""


# ============================================================
# 3. CHAT RESPONSE HANDLER
# ============================================================

def respond(message, history):

    if not message or not message.strip():
        return history or [], ""

    history = list(history or [])

    # Add user message immediately.
    history.append({
        "role": "user",
        "content": message.strip()
    })

    try:
        print(f"User question: {message.strip()}")

        # Call the existing MCP-enabled TravelAgent.
        answer = agent.ask(message.strip())

        if not isinstance(answer, str):
            answer = str(answer)

    except Exception as exc:

        print(
            f"Application error: {type(exc).__name__}: {exc}"
        )

        answer = (
            "Sorry, I encountered an issue while planning "
            "your trip.\n\n"
            f"**Error:** {type(exc).__name__}: {exc}"
        )

    history.append({
        "role": "assistant",
        "content": answer
    })

    return history, ""


# ============================================================
# 4. CLEAR CHAT
# ============================================================

def clear_chat():
    return [], ""


# ============================================================
# 5. QUICK PROMPT HANDLER
# ============================================================

def quick_prompt(prompt, history):
    return respond(prompt, history)


# ============================================================
# 6. BUILD GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    title="Trip Buddy | AI Travel Planner",
    css=CUSTOM_CSS
) as demo:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    gr.HTML("""
        <div id="trip-header">
            <h1>✈️ Trip Buddy</h1>
            <p>
                Your AI-powered travel companion.
                Discover destinations, calculate group budgets,
                and get smarter travel recommendations.
            </p>
        </div>
    """)

    with gr.Row(equal_height=False):

        # ====================================================
        # LEFT SIDEBAR
        # ====================================================

        with gr.Column(
            scale=1,
            min_width=260,
            elem_id="sidebar"
        ):

            gr.Markdown("## 🧭 Explore Trip Buddy")

            gr.Markdown(
                "Plan your next adventure with your friends."
            )

            gr.Markdown("### ⚡ Quick actions")

            btn_list = gr.Button(
                "📍 Explore destinations",
                elem_classes=["quick-button"]
            )

            btn_goa = gr.Button(
                "🏖️ Plan a Goa trip",
                elem_classes=["quick-button"]
            )

            btn_manali = gr.Button(
                "🏔️ Manali seasonal advice",
                elem_classes=["quick-button"]
            )

            btn_hampi = gr.Button(
                "🏛️ Calculate Hampi budget",
                elem_classes=["quick-button"]
            )

            btn_budget = gr.Button(
                "💰 Find trips within budget",
                elem_classes=["quick-button"]
            )

            gr.Markdown("---")

            gr.Markdown("### 🛠️ What I can do")

            gr.Markdown("""
            - 📍 Discover destinations
            - 💰 Calculate trip costs
            - 👥 Plan group travel
            - 🧠 Retrieve travel knowledge
            - 🌦️ Provide seasonal guidance
            """)

            gr.Markdown("---")

            gr.Markdown("### 🔌 Connected services")

            gr.HTML("""
                <div class="status-card">
                    <p>🟢 Travel MCP Server</p>
                    <p>🟢 Knowledge MCP Server</p>
                    <p>🟢 SQLite Database</p>
                    <p>🟢 RAG Retrieval</p>
                </div>
            """)

            gr.Markdown(
                """
                <div class="footer-note">
                    Demo estimates only. Not live travel quotes.
                </div>
                """
            )

        # ====================================================
        # RIGHT CHAT PANEL
        # ====================================================

        with gr.Column(
            scale=3,
            min_width=320,
            elem_id="chat-panel"
        ):

            with gr.Row():
                gr.Markdown("## 💬 Travel Assistant")

                clear_btn = gr.Button(
                    "🗑️ Clear chat",
                    size="sm",
                    variant="secondary"
                )

            chatbot = gr.Chatbot(
                height=520,
                show_label=False,
                placeholder=(
                    "👋 Welcome to Trip Buddy!\n\n"
                    "Tell me where you want to travel, "
                    "your budget and how many friends are joining."
                ),
                elem_id="chatbot"
            )

            # ------------------------------------------------
            # INPUT AREA
            # ------------------------------------------------

            with gr.Row():

                msg = gr.Textbox(
                    placeholder=(
                        "Ask me anything... e.g. "
                        "Plan Goa for 4 friends, 3 nights"
                    ),
                    show_label=False,
                    lines=2,
                    max_lines=5,
                    scale=8,
                    elem_id="message-box"
                )

                send_btn = gr.Button(
                    "➤ Send",
                    variant="primary",
                    scale=1,
                    elem_classes=["primary-action"]
                )

            gr.Markdown(
                """
                <div class="footer-note">
                    Trip Buddy uses MCP tools and RAG to answer
                    travel questions. Verify live prices and conditions
                    before booking.
                </div>
                """
            )

    # ========================================================
    # 7. EVENT HANDLERS
    # ========================================================

    # Enter key
    msg.submit(
        fn=respond,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    # Send button
    send_btn.click(
        fn=respond,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    # Quick prompt configuration
    quick_prompts = [
        (
            btn_list,
            "List destinations"
        ),
        (
            btn_goa,
            "We are 4 friends with ₹12,000 each. Can we do Goa for 3 nights?"
        ),
        (
            btn_manali,
            "Is Manali a good idea in July?"
        ),
        (
            btn_hampi,
            "How much is Hampi for 5 friends, 2 nights?"
        ),
        (
            btn_budget,
            "Which trips fit ₹8,000 each for 3 friends, 2 nights?"
        )
    ]

    for button, prompt in quick_prompts:

        button.click(
            fn=quick_prompt,
            inputs=[
                gr.State(value=prompt),
                chatbot
            ],
            outputs=[
                chatbot,
                msg
            ]
        )

    # Clear chat
    clear_btn.click(
        fn=clear_chat,
        inputs=None,
        outputs=[chatbot, msg],
        queue=False
    )


# ============================================================
# 8. LAUNCH APPLICATION
# ============================================================

if __name__ == "__main__":

    print("\nStarting Trip Buddy AI Travel Planner...")

    demo.queue().launch(
        server_name="127.0.0.1",
        server_port=7860,
        theme=gr.themes.Soft(),
        show_error=True
    )
