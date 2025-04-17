# Overview

This is an interactive, web-based risk assessment tool using Python and [Streamlit](https://streamlit.io/). The app enables users to input empirical measurements (e.g., benchmark scores, evaluation results, incident reports) through an intuitive UI with sliders and numeric inputs. These inputs are mapped to the parameters of a simplified AI cyber risk model, which includes:

1. **N:** Number of attack attempts  
2. **P₁:** Probability of a successful spearphishing campaign  
3. **P₂:** Probability of successful malware development and deployment  
4. **P₃:** Probability of successful persistence and achievement of objectives  
5. **Severity:** Economic damage per successful attack  

### Risk Model
**Expected Risk = N × P₁ × P₂ × P₃ × Severity**

To propagate uncertainty and generate a more insightful view of outcomes, the app performs a **Monte Carlo simulation**, sampling attack outcomes and computing a range of potential damages. Users are shown:
- A point estimate for expected damages
- A histogram distribution of economic damages
- A sensitivity pie chart breaking down contributions of each stage

---

# Key Features

- ✅ **Interactive UI**: Adjust parameters live and observe impact on risk.
- 📊 **Monte Carlo Simulation**: Simulates 10,000 attack scenarios.
- 📉 **Damage Distribution Visualization**: Histogram of potential outcomes.
- 📈 **Sensitivity Analysis**: Pie chart of contributing risk sources.
- 🔁 **Modular Design**: Easily adaptable to new models or benchmarks.
- 🧠 **Inspired by PRA**: Modeled after risk assessments like those used in nuclear safety (e.g., NRC SPAR).

---

# How to Run the Code

### 1. Clone this repository or download the Python file
```bash
git clone https://github.com/your-repo/ai-cyber-risk-app.git
cd ai-cyber-risk-app
```

### 2. (Recommended) Set up a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install streamlit matplotlib numpy
```

### 4. Run the app
```bash
streamlit run ai_cyber_risk_app.py
```

### 5. View in your browser
By default, it should open at: [http://localhost:8501](http://localhost:8501)
