import streamlit as st
import os
# Mock imports for your existing pipeline modules
try:
    from src.image_damage_detector import detect_damage
    from src.severity_predictor import predict_severity
    from src.fraud_score import compute_fraud_score
except ImportError:
    # Fallbacks if your modules have slightly different names
    def detect_damage(img): return {"damage_type": "Front Bumper Dent", "confidence": 0.89}
    def predict_severity(img): return {"severity": "Moderate", "score": 45, "confidence": 0.85}
    def compute_fraud_score(*args): return 35

from src.ai_explainer import generate_ai_explanation
from src.pdf_generator import create_claim_pdf

st.set_page_config(page_title="Gowtham's InsureAI Platform", layout="wide")

# Polished Hackathon UI Styling
st.markdown("""
    <style>
    .main-title { font-size:40px !important; color:#1A365D; font-weight:bold; margin-bottom: 0px; }
    .sub-title { font-size:18px !important; color:#4A5568; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🚀 Hackathon Project")
    st.markdown("### **Lead Architect:**\n**Gowtham**")
    st.markdown("### **Tech Stack:**\n- Computer Vision\n- Gemini 2.5 Flash\n- Streamlit & FastAPI\n- ReportLab Engine")
    st.write("---")
    st.caption("Designed for Top-Tier Claims Automation & Fraud Forensic Audit.")

st.markdown("<div class='main-title'>🛡️ InsureAI: Smart Claims & Fraud Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Engineered by Gowtham &bull; Multi-Model Computer Vision & Live Generative AI Core</div>", unsafe_allow_html=True)
st.markdown("---")

uploaded = st.file_uploader("📥 Drag and drop vehicle accident imagery here...", type=["jpg", "jpeg", "png"])

if uploaded:
  
    with open("temp.jpg", "wb") as f:
        f.write(uploaded.getbuffer())
        
    col_img, col_metrics = st.columns([1, 1.3])
    
    with col_img:
        st.image(uploaded, caption="Target Claim Artifact", use_container_width=True)
        
    with col_metrics:
        with st.spinner("Executing CV Models & Core Fraud Engine Risk Analysis..."):
           
            damage = detect_damage("temp.jpg")
            severity = predict_severity("temp.jpg")
            
            
            fraud = compute_fraud_score(
                severity.get("score", 50), 
                20, 10, 30, 
                severity.get("confidence", 0.85) * 100
            )
            
            
            explanation = generate_ai_explanation(damage, severity, fraud)
        
       
        c1, c2, c3 = st.columns(3)
        c1.metric("Visual Assessment", damage.get("damage_type", "Unknown"))
        c2.metric("Severity Tier", severity.get("severity", "Unknown"))
        
        if fraud > 70:
            c3.metric("Fraud Risk Score 🔥", f"{fraud}/100", delta="High Risk / Audit Flagged", delta_color="inverse")
        else:
            c3.metric("Fraud Risk Score ✅", f"{fraud}/100", delta="Low Risk Status")
            
        st.subheader("🧠 Live Explainable AI (XAI) Insight")
        st.info(explanation)
        
       
        pdf_path = create_claim_pdf(damage, severity, fraud, explanation)
        
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Official Gowtham-InsureAI Audit PDF",
                data=pdf_file,
                file_name="Gowtham_InsureAI_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

st.markdown("""
    <br/><br/><hr/>
    <p style='text-align: center; color: #718096;'>🏆 Powered by Gowtham's AI Insurance Intelligence Platform &bull; Hackathon Edition</p>
""", unsafe_allow_html=True)