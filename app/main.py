import streamlit as st
import plotly.graph_objects as go
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from predictor import predict_crop
from fertilizer import get_fertilizer_advice
from weather import get_weather
from translator import t

st.set_page_config(page_title="किसान मित्र | Kisan Mitra", page_icon="🌾", layout="wide")

# ── Language ──────────────────────────────────────────────────────
lang = st.sidebar.selectbox("Language / भाषा / भाषा", ["en", "hi", "mr"],
                             format_func=lambda x: {"en":"English","hi":"हिंदी","mr":"मराठी"}[x])
st.title(t("title", lang))
st.caption("किसान मित्र — AI-powered crop recommendation for Indian farmers 🇮🇳")

# ── Live Weather ───────────────────────────────────────────────────
st.sidebar.header("🌤 Live Weather")
city = st.sidebar.text_input("Enter city", "Pune")
if st.sidebar.button("Fetch Weather"):
    w = get_weather(city)
    if "error" in w:
        st.sidebar.error(w["error"])
    else:
        st.sidebar.metric("🌡 Temperature (°C)", w["temperature"])
        st.sidebar.metric("💧 Humidity (%)", w["humidity"])
        st.sidebar.info(w["description"])

# ── Input Form ─────────────────────────────────────────────────────
st.header(f"📋 {t('enter_farm', lang)}")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(f"🌱 {t('soil', lang)}")
    soil_type   = st.selectbox("Soil type", ["loamy", "sandy", "clay"])
    N  = st.slider("Nitrogen (N)",    0,   140, 60)
    P  = st.slider("Phosphorus (P)",  5,   145, 40)
    K  = st.slider("Potassium (K)",   5,   205, 40)
    ph = st.slider("Soil pH",        3.5,  9.5, 6.5, step=0.1)

with col2:
    st.subheader(f"🌡 {t('weather', lang)}")
    temperature = st.slider("Temperature (°C)", 8.0,  45.0, 25.0, step=0.5)
    humidity    = st.slider("Humidity (%)",    10.0, 100.0, 65.0, step=0.5)
    rainfall    = st.slider("Rainfall (mm)",   20.0, 300.0,100.0, step=5.0)

with col3:
    st.subheader(f"📍 {t('location', lang)}")
    state = st.selectbox("State", [
        "Maharashtra","Punjab","Uttar Pradesh","Karnataka",
        "West Bengal","Madhya Pradesh","Andhra Pradesh",
        "Rajasthan","Tamil Nadu","Gujarat"
    ])
    st.info("State-specific pricing & scheme data coming soon.")

# ── Predict ────────────────────────────────────────────────────────
if st.button("🔍 Get Crop Recommendation", use_container_width=True, type="primary"):
    with st.spinner("Analysing your farm data..."):
        try:
            results = predict_crop(N, P, K, temperature, humidity, ph, rainfall, soil_type)
        except FileNotFoundError as e:
            st.error(str(e))
            st.info("💡 Run `python scripts/train_model.py` from the project root to train the model first.")
            st.stop()
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.stop()

    best   = results[0]
    advice = get_fertilizer_advice(best["crop"])

    st.divider()
    st.header(f"✅ {t('best_crop', lang)}")

    r1, r2, r3 = st.columns(3)
    r1.metric("🌾 Crop",                best["crop"].upper())
    r2.metric(t("confidence", lang),    f"{best['confidence']}%")
    r3.metric(t("fertilizer", lang),    advice["fertilizer"])
    st.success(f"💡 **{t('tip', lang)}:** {advice['tip']}")

    # Alt crops
    st.subheader(t("alt_crops", lang))
    ac1, ac2 = st.columns(2)
    for i, alt in enumerate(results[1:]):
        with [ac1, ac2][i]:
            with st.expander(f"🌿 {alt['crop'].title()}  ({alt['confidence']}%)"):
                adv = get_fertilizer_advice(alt["crop"])
                st.write(f"**{t('fertilizer',lang)}:** {adv['fertilizer']}")
                st.write(f"**{t('tip',lang)}:** {adv['tip']}")

    # Bar chart
    st.subheader("📊 Prediction Confidence")
    fig = go.Figure(go.Bar(
        x=[r["crop"].title() for r in results],
        y=[r["confidence"] for r in results],
        marker_color=["#2E7D32","#66BB6A","#A5D6A7"],
        text=[f"{r['confidence']}%" for r in results],
        textposition="outside"
    ))
    fig.update_layout(yaxis_title="Confidence (%)", yaxis_range=[0,110],
                      plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    # Radar chart
    st.subheader("🧪 Soil Nutrient Profile")
    radar = go.Figure(go.Scatterpolar(
        r=[N, P, K, ph*10, humidity, rainfall/10],
        theta=["Nitrogen","Phosphorus","Potassium","pH×10","Humidity","Rainfall/10"],
        fill="toself", line_color="#388E3C"
    ))
    radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,200])),
                        paper_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(radar, use_container_width=True)

st.divider()
st.caption("किसान मित्र 🌾 · Built with ❤️ using Streamlit · scikit-learn · Plotly | Data: Kaggle Crop Recommendation Dataset")
