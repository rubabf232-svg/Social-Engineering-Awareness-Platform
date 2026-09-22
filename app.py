import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Social Engineering Awareness Platform",
    page_icon="🛡️",
    layout="wide"
)

SCENARIOS = [
    {
        "title": "Phishing Email",
        "type": "Phishing",
        "scenario": (
            "You receive an email saying your account will be suspended "
            "within 30 minutes unless you click a link and verify your password."
        ),
        "question": "What is the safest first action?",
        "options": [
            "Click the link immediately",
            "Reply with your password",
            "Verify the message through the organization's official website or app",
            "Forward it to friends"
        ],
        "answer": 2,
        "red_flags": [
            "Urgency",
            "Threat of account suspension",
            "Unexpected credential request",
            "Link-based verification"
        ],
        "explanation": (
            "Urgency and credential requests are common phishing warning signs. "
            "Verify the request independently instead of using the message's link."
        )
    },
    {
        "title": "Fake IT Support Call",
        "type": "Vishing",
        "scenario": (
            "Someone calls claiming to be from IT and asks for your MFA code "
            "to 'fix a login problem'."
        ),
        "question": "What should you do?",
        "options": [
            "Give the code because they know your name",
            "Share only the current code",
            "End the call and contact IT using a trusted contact method",
            "Ask them to send another code"
        ],
        "answer": 2,
        "red_flags": [
            "Unsolicited call",
            "MFA code request",
            "Authority impersonation"
        ],
        "explanation": (
            "MFA codes should not be disclosed to callers. Contact the organization "
            "through a trusted channel."
        )
    },
    {
        "title": "Suspicious SMS",
        "type": "Smishing",
        "scenario": (
            "An SMS claims you have a parcel waiting and provides a shortened "
            "URL for a small delivery fee."
        ),
        "question": "What is the safest response?",
        "options": [
            "Open the URL to check the parcel",
            "Use the courier's official app or website directly",
            "Enter your card details but not your PIN",
            "Reply asking who sent it"
        ],
        "answer": 1,
        "red_flags": [
            "Unexpected delivery message",
            "Shortened URL",
            "Payment request"
        ],
        "explanation": (
            "Use a known official website or app instead of a link supplied "
            "by an unsolicited message."
        )
    },
    {
        "title": "Tailgating",
        "type": "Physical Social Engineering",
        "scenario": (
            "A person carrying several boxes asks you to hold a secure office "
            "door open because they say they forgot their access card."
        ),
        "question": "What should you do?",
        "options": [
            "Hold the door because they look like staff",
            "Let them follow you if they know your name",
            "Follow the organization's access-control procedure",
            "Give them your access card"
        ],
        "answer": 2,
        "red_flags": [
            "Pressure to bypass access control",
            "Plausible excuse",
            "Unverified identity"
        ],
        "explanation": (
            "Physical security controls should not be bypassed because of a "
            "convincing story or appearance."
        )
    },
    {
        "title": "Fake Prize Message",
        "type": "Baiting",
        "scenario": (
            "You receive a message saying you have won a new smartphone. "
            "It asks you to provide your account password to claim the prize."
        ),
        "question": "What is the safest response?",
        "options": [
            "Provide the password because the prize is valuable",
            "Provide only your username",
            "Do not provide credentials and verify the offer independently",
            "Forward the message to another person"
        ],
        "answer": 2,
        "red_flags": [
            "Unexpected prize",
            "Credential request",
            "Too-good-to-be-true offer"
        ],
        "explanation": (
            "Unexpected rewards combined with credential requests are strong "
            "warning signs. Never disclose passwords to claim a prize."
        )
    },
    {
        "title": "CEO Impersonation",
        "type": "Pretexting",
        "scenario": (
            "A message appears to come from your manager and asks you to "
            "purchase gift cards urgently and send the codes."
        ),
        "question": "What should you do?",
        "options": [
            "Complete the request immediately",
            "Send half of the codes first",
            "Verify the request through another trusted communication method",
            "Ask another employee to purchase them"
        ],
        "answer": 2,
        "red_flags": [
            "Authority impersonation",
            "Urgency",
            "Unusual payment request",
            "Gift-card request"
        ],
        "explanation": (
            "Attackers may impersonate managers or executives. Independently "
            "verify unusual financial requests."
        )
    }
]


def calculate_score(answers):
    score = 0

    for index, selected in answers.items():
        scenario = SCENARIOS[index - 1]

        if selected == scenario["options"][scenario["answer"]]:
            score += 1

    return score


def score_message(percentage):
    if percentage == 100:
        return (
            "Excellent awareness. You identified all simulated "
            "social-engineering scenarios correctly."
        )

    if percentage >= 75:
        return (
            "Good awareness. Review the scenarios you missed "
            "and continue practicing independent verification."
        )

    if percentage >= 50:
        return (
            "Some warning signs were missed. Review the awareness "
            "guide and security checklist."
        )

    return (
        "Several warning signs were missed. Review the guide carefully "
        "before responding to suspicious requests."
    )


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.title("🛡️ Security Awareness")

    page = st.radio(
        "Navigation",
        [
            "Awareness Guide",
            "Scenario Assessment",
            "Security Checklist",
            "About Project"
        ]
    )

    st.divider()

    st.info(
        "Educational defensive-security project. "
        "All scenarios are simulated."
    )


# -----------------------------
# Awareness Guide
# -----------------------------

if page == "Awareness Guide":

    st.title("🛡️ Social Engineering Awareness Platform")

    st.write(
        "Social engineering uses deception and psychological manipulation "
        "to influence people into revealing information, clicking unsafe "
        "links, transferring money, or bypassing security procedures."
    )

    st.divider()

    st.header("Common Attack Types")

    columns = st.columns(4)

    attack_types = [
        ("🎣 Phishing", "Fraudulent emails or websites."),
        ("📱 Smishing", "Phishing delivered through SMS."),
        ("☎️ Vishing", "Fraudulent or deceptive phone calls."),
        ("🎭 Pretexting", "A fabricated identity or story.")
    ]

    for column, (title, description) in zip(columns, attack_types):
        with column:
            st.subheader(title)
            st.write(description)

    st.divider()

    st.header("🚩 Common Red Flags")

    red_flags = [
        "Unexpected requests for sensitive information",
        "Urgency or threats",
        "Requests for passwords, OTPs, PINs, or MFA codes",
        "Unknown links or attachments",
        "Requests to bypass normal security procedures",
        "Unexpected payment requests",
        "Too-good-to-be-true rewards",
        "Impersonation of managers, banks, IT staff, or authorities"
    ]

    for flag in red_flags:
        st.write("⚠️", flag)

    st.divider()

    st.header("🛡️ SAFE Response Method")

    st.markdown(
        """
### S — Stop
Do not act immediately because someone creates pressure or urgency.

### A — Assess
Check the sender, request, link, attachment, and context.

### F — Find a trusted channel
Contact the person or organization independently using a known phone
number, website, application, or internal directory.

### E — Escalate
Report suspicious activity using the appropriate security process.
"""
    )


# -----------------------------
# Scenario Assessment
# -----------------------------

elif page == "Scenario Assessment":

    st.title("🧠 Interactive Scenario Assessment")

    st.write(
        "These scenarios simulate common social-engineering situations. "
        "Choose the safest defensive response."
    )

    answers = {}

    for number, scenario in enumerate(SCENARIOS, start=1):

        st.subheader(
            f"{number}. {scenario['title']} — {scenario['type']}"
        )

        st.write(scenario["scenario"])

        answers[number] = st.radio(
            scenario["question"],
            scenario["options"],
            key=f"scenario_{number}",
            index=None
        )

        with st.expander("🚩 View warning signs"):
            for flag in scenario["red_flags"]:
                st.write("•", flag)

    st.divider()

    if st.button(
        "Calculate Awareness Score",
        type="primary",
        use_container_width=True
    ):

        unanswered = [
            number
            for number, answer in answers.items()
            if answer is None
        ]

        if unanswered:
            st.warning(
                f"Please answer all scenarios first. "
                f"Unanswered: {', '.join(map(str, unanswered))}"
            )

        else:
            score = calculate_score(answers)
            total = len(SCENARIOS)
            percentage = int((score / total) * 100)

            st.header("📊 Assessment Result")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Awareness Score",
                    f"{percentage}%"
                )

            with col2:
                st.metric(
                    "Correct Answers",
                    f"{score}/{total}"
                )

            st.progress(percentage / 100)

            if percentage == 100:
                st.success(score_message(percentage))
            elif percentage >= 75:
                st.info(score_message(percentage))
            elif percentage >= 50:
                st.warning(score_message(percentage))
            else:
                st.error(score_message(percentage))

            st.divider()

            st.header("📋 Scenario Review")

            for number, scenario in enumerate(SCENARIOS, start=1):

                correct_answer = scenario["options"][
                    scenario["answer"]
                ]

                if answers[number] == correct_answer:
                    st.success(
                        f"Scenario {number}: Correct — "
                        f"{scenario['title']}"
                    )

                else:
                    st.error(
                        f"Scenario {number}: Review needed — "
                        f"{scenario['title']}"
                    )

                    st.write(
                        f"**Correct response:** {correct_answer}"
                    )

                    st.caption(
                        scenario["explanation"]
                    )


# -----------------------------
# Security Checklist
# -----------------------------

elif page == "Security Checklist":

    st.title("🔐 Security Awareness Checklist")

    st.write(
        "Use this checklist to review your everyday security habits."
    )

    checklist = [
        "I never share passwords with other people.",
        "I never share OTP, PIN, or MFA codes with callers or messages.",
        "I verify unexpected requests through a trusted channel.",
        "I check links before opening them.",
        "I avoid unexpected email attachments.",
        "I use unique passwords for important accounts.",
        "I enable MFA where available.",
        "I report suspicious messages instead of forwarding them.",
        "I follow physical access-control procedures.",
        "I pause when a request creates unusual pressure or urgency."
    ]

    completed = 0

    for item in checklist:
        if st.checkbox(item):
            completed += 1

    total_items = len(checklist)
    percentage = int((completed / total_items) * 100)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Checklist Progress",
            f"{completed}/{total_items}"
        )

    with col2:
        st.metric(
            "Completion",
            f"{percentage}%"
        )

    st.progress(percentage / 100)

    if percentage == 100:
        st.success("Your checklist is complete. Keep these habits consistent.")
    elif percentage >= 70:
        st.info("Good progress. Review the unchecked items.")
    else:
        st.warning("Review the unchecked security practices.")


# -----------------------------
# About Project
# -----------------------------

elif page == "About Project":

    st.title("ℹ️ About This Project")

    st.write(
        "The Social Engineering Awareness Platform is a defensive "
        "cybersecurity education project."
    )

    st.header("Project Objectives")

    objectives = [
        "Teach users to recognize social-engineering warning signs.",
        "Demonstrate safe responses to suspicious requests.",
        "Promote independent verification.",
        "Improve awareness of credential and MFA protection.",
        "Encourage responsible security reporting."
    ]

    for objective in objectives:
        st.write("✅", objective)

    st.header("Technology")

    st.code(
        """
Python
Streamlit
        """
    )

    st.header("Ethical Scope")

    st.write(
        "This application does not send real phishing messages, "
        "collect credentials, bypass security controls, or attack "
        "real systems. Its scenarios are simulated for awareness "
        "and defensive training."
    )

    st.divider()

    st.caption(
        f"Social Engineering Awareness Platform • {datetime.now().year}"
    )