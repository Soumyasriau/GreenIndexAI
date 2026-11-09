# 🌿 GreenIndexAI

**AI-Powered NDVI-Based Vegetation Monitoring and Analysis System**

## 📌 About the Project

GreenIndexAI is an AI-powered application designed to analyze vegetation health using Normalized Difference Vegetation Index (NDVI) data.

It allows users to ask questions about vegetation across different Indian states using natural language. The system retrieves relevant NDVI records and provides environmental information such as temperature, rainfall, and soil moisture.

The application uses AI to simplify environmental data analysis and generate meaningful insights.

## ✨ Features

- **AI-Powered Queries:** Ask questions about vegetation data in natural language.
- **NDVI Analysis:** Retrieve vegetation index values for different states.
- **Environmental Monitoring:** View temperature, rainfall, and soil moisture.
- **NDVI Visualization:** Display related vegetation images when available.
- **AI-Based Insights:** Generate answers using Perplexity AI.
- **Follow-up Questions:** Ask additional questions based on retrieved results.
- **Interactive Dashboard:** Explore information through a Streamlit interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- Flask
- Perplexity AI API
- PostgreSQL
- SQLAlchemy
- REST API
- JSON
- Pillow

## 📂 Project Structure

```text
GreenIndexAI/
│
├── agent1.py
├── agent2.py
├── app.py
├── streamlit_app.py
├── ndvi_data.json
├── requirements.txt
├── Procfile
├── LICENSE
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Soumyasriau/GreenIndexAI.git
```

**2. Navigate to the project folder**

```bash
cd GreenIndexAI
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file:

```env
PERPLEXITY_API_KEY=your_perplexity_api_key
DATABASE_URL=your_postgresql_database_url
```

**5. Run the Streamlit application**

```bash
streamlit run streamlit_app.py
```

## 📊 Dataset

The project uses an NDVI dataset containing:

- State
- Month
- Year
- NDVI values
- Temperature
- Rainfall
- Soil moisture
- NDVI image URLs

**Data period:** January 2025 – June 2025.

## 🏗️ System Architecture

1. User enters a natural-language query.
2. AI Agent processes the query using Perplexity AI.
3. Relevant records are retrieved from the NDVI JSON dataset.
4. Flask API provides environmental data and image information through database queries.
5. Results are displayed through the Streamlit dashboard.
6. A second AI agent answers follow-up questions using the retrieved data.

## 🎯 Project Objective

To simplify vegetation monitoring and environmental data analysis through artificial intelligence, natural-language processing, and NDVI-based data visualization.

## 👩‍💻 Author

**Soumya**

GitHub: [Soumyasriau](https://github.com/Soumyasriau)

---

⭐ If you find this project interesting, consider giving it a star on GitHub.

**GreenIndexAI – Turning Environmental Data into Meaningful Insights.**
