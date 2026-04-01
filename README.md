


<img width="1315" height="853" alt="Ekran görüntüsü 2026-04-01 143913" src="https://github.com/user-attachments/assets/79617421-81db-4094-8d13-6f11d0d279a6" />



# 🏎️ Precision Auto AI: 100-Day Data Science Bootcamp Capstone Project

This project is the final **Capstone Project** developed as part of the **"Data Science & Machine Learning 2026: 100-Day Bootcamp"** led by **Atıl Samancıoğlu**. It represents a complete end-to-end machine learning pipeline, starting from raw data analysis to a fully functional, professionally designed web deployment.

---

## 📊 1. Dataset & Source
The model is trained on the popular **"100,000 UK Used Car Data set"**, focusing on luxury and standard vehicle segments in the UK market.

* **Dataset Source:** [Kaggle - 100,000 UK Used Car Data set](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes)
* **Comprehensive Analysis Notebook:** [Car Price Prediction - 96% Acc | XGBoost](https://www.kaggle.com/code/servetvarol/car-price-prediction-96-acc-xgboost)

---

## 🤖 2. Model Performance (XGBoost Regressor)
After testing various regression algorithms, the **XGBoost Regressor** was selected for its superior predictive power and generalization capability.

### **Training Set Performance**
- **RMSE:** 278,707.22
- **MAE:** 182,635.71
- **R² Score:** **0.9859**

### **Test Set Performance**
- **RMSE:** 417,254.68
- **MAE:** 265,369.81
- **R² Score:** **0.9682**

---

## 🎨 3. UI/UX Design: Deep Obsidian & Burnished Copper
The front-end was specifically crafted to reflect the premium nature of the luxury automotive segment. The visual identity was developed with the creative assistance of **Antigravity**.

* **Design Language:** Apple-like minimalist aesthetic with advanced Glassmorphism effects.
* **Color Palette:** Deep Obsidian Black and metallic Burnished Copper tones.
* **Technical Features:** Dynamic CSS `conic-gradient` gauge charts, asynchronous data transfer (Vanilla JS), and custom cursor animations.

---

## 🎓 4. About the Bootcamp (100-Day Challenge)
This project is the culmination of an intensive curriculum designed to master modern AI & Data Science competencies:
* **Data Foundations:** Numpy, Pandas, EDA, and advanced Feature Engineering.
* **Visualization:** Professional-grade plots using Matplotlib and Seaborn.
* **Machine Learning:** Regression, Classification, Supervised/Unsupervised Learning, and Model Serialization (Pickle/Joblib).
* **Deployment:** Transforming ML models into production-ready web apps using **FastAPI**.

---

## 🛠️ Installation & Usage

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Application:**
    ```bash
    uvicorn app:app --reload --port 8001
    ```
3.  **Access:** Open your browser and navigate to `http://127.0.0.1:8001`.

---

## 📂 Project Structure
- `app.py`: FastAPI backend and core prediction logic.
- `static/`: CSS styling, custom cursor assets, and branding.
- `templates/`: Modern HTML5 dashboard layout.
- `*.pkl`: Serialized XGBoost model, Scalers, and Encoders.

---

**Developer:** Servet Varol  
*Computer Engineering Graduate | AI & Data Science Enthusiast* [LinkedIn](https://www.linkedin.com/in/servetvarol/) | [Kaggle](https://www.kaggle.com/servetvarol) | [GitHub](https://github.com/Servetvrll)
