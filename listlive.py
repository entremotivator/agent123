import streamlit as st

# Page Config
st.set_page_config(page_title="Agent Network Links", layout="centered")

st.title("🤖 Your Agent Universe 🌐")
st.subheader("Explore all your deployed Streamlit agent apps")

st.markdown("### 🧠 Smart Agent Apps")

agents = {
    "Agent Monop": "https://agentmonop.streamlit.app/",
    "Agent Asia": "https://agentasia.streamlit.app",
    "Agent Edna": "https://agentedna.streamlit.app/",
    "Agent Flash": "https://agentflash.streamlit.app/",
    "Agent MSU": "https://agentmsu.streamlit.app/",
    "Agent Liah": "https://agentliah.streamlit.app/",
    "Agent Quinn": "https://agentquinn.streamlit.app/",
    "Agent Esther": "https://agentesther.streamlit.app/"
}

# Display the links with emoji bullets
for name, url in agents.items():
    st.markdown(f"🔗 **{name}** — [Launch App]({url})")

# Divider
st.markdown("---")

# Extra encouragement / notes section
st.success("YESSSSS — You're crushing it! 🚀")
st.info("Need to add more features or fix an agent? Let me know. Agents can evolve.")

# Footer note
st.caption("Built with ❤️ using Streamlit")
