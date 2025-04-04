import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="AI Cyber Risk Assessment", layout="centered")
st.title("🔒 AI Cyber Risk Assessment Tool")

st.markdown("""
This tool estimates the **expected economic damage** from AI-enabled cyberattacks using a probabilistic risk model. You can adjust parameters and explore scenario analysis and sensitivity of each variable.
""")

# Input sliders
attack_attempts = st.number_input("Number of attack attempts", min_value=0, value=1000, step=100)
p_phishing = st.slider("P(successful spearphishing campaign)", 0.0, 1.0, 0.3, 0.01)
p_malware = st.slider("P(successful malware development & deployment)", 0.0, 1.0, 0.2, 0.01)
p_persistence = st.slider("P(successful persistence & achieving objectives)", 0.0, 1.0, 0.4, 0.01)
severity_per_success = st.number_input("Economic severity per successful attempt ($)", min_value=0, value=500000, step=10000)

# Risk model computation
expected_successful_attacks = attack_attempts * p_phishing * p_malware * p_persistence
expected_economic_damage = expected_successful_attacks * severity_per_success

# Confidence interval based on 10000 samples
samples = np.random.binomial(attack_attempts, p_phishing * p_malware * p_persistence, size=10000)
damage_samples = samples * severity_per_success
lower = np.percentile(damage_samples, 5)
upper = np.percentile(damage_samples, 95)

# Output
st.subheader("📊 Results")
st.write(f"**Expected successful attacks:** {expected_successful_attacks:.2f}")
st.write(f"**Expected economic damage:** ${expected_economic_damage:,.2f}")
st.write(f"**90% Confidence Interval:** ${lower:,.0f} — ${upper:,.0f}")

# Histogram
st.subheader("🔍 Damage Distribution (Monte Carlo Simulation)")
fig, ax = plt.subplots()
ax.hist(damage_samples, bins=50, color='skyblue', edgecolor='black')
ax.set_xlabel("Estimated Economic Damage ($)")
ax.set_ylabel("Frequency")
ax.set_title("Simulated Distribution of Economic Damage")
st.pyplot(fig)

# Sensitivity Analysis
st.subheader("📈 Sensitivity Analysis")
sensitivities = {
    "Phishing": p_phishing,
    "Malware": p_malware,
    "Persistence": p_persistence,
}
labels = list(sensitivities.keys())
values = [expected_economic_damage * (s / sum(sensitivities.values())) for s in sensitivities.values()]
fig2, ax2 = plt.subplots()
ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.set_title("Relative Contribution to Total Risk")
st.pyplot(fig2)

# Notes
st.markdown("""
---
✅ This tool draws inspiration from probabilistic risk assessment (PRA) methods in nuclear safety (e.g., NRC SPAR). It is adapted here to model LLM-enabled cyber risks, using simplified chain-of-events modeling.
""")