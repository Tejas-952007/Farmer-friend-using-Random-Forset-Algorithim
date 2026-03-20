# 🌾 Farmer Crop Advisor (India-focused)

AI-powered crop recommendation system for Indian farmers using Machine Learning.

## Features
- Crop recommendation based on soil (N, P, K, pH, type) and weather (temperature, humidity, rainfall)
- Fertilizer suggestions per crop
- Live weather via OpenWeather API
- Multi-language support: English, Hindi (हिंदी), Marathi (मराठी)
- Plotly visualizations (bar chart + radar chart)
- Deployed on Streamlit Cloud

## Quick Start

```bash
# 1. Clone & install
pip install -r requirements.txt

# 2. Add your OpenWeather API key
cp .env.example .env
# Edit .env and add your key

# 3. Download dataset
# From: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
# Place in: data/raw/crop_recommendation.csv

# 4. Train the model
cd scripts && python train_model.py

# 5. Run the app
cd ..
streamlit run app/main.py
```

## Dataset
- **Source:** Kaggle — Crop Recommendation Dataset
- **Rows:** 2,200 | **Crops:** 22 | **Features:** N, P, K, temperature, humidity, ph, rainfall

## Model Performance
| Model          | Accuracy |
|----------------|----------|
| Random Forest  | ~99%     |
| Decision Tree  | ~90%     |
| Naive Bayes    | ~85%     |

## Tech Stack
`Python` · `scikit-learn` · `pandas` · `numpy` · `Streamlit` · `Plotly` · `OpenWeather API`

## Deployment
Deployed on [Streamlit Cloud](https://farmer-friend-using-random-forset-algorithim.streamlit.app/) — free hosting, connects directly to GitHub.
