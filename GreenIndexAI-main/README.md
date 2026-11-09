# 🌿 GreenIndex AI – AI-Powered Vegetation Monitoring

GreenIndex AI is an AI-powered vegetation monitoring and analysis application that helps users explore vegetation health using Normalized Difference Vegetation Index (NDVI) data.

The application allows users to query vegetation information by state, month, and year using natural language and provides AI-generated insights based on the available dataset.

## 🚀 Features

- **Natural Language Queries:** Ask questions about NDVI data in simple English.
- **Vegetation Analysis:** Retrieve NDVI values for different states and time periods.
- **Climate Insights:** View temperature, rainfall, and soil moisture information.
- **NDVI Visualization:** Display vegetation-related images.
- **AI-Powered Analysis:** Generate insights and comparisons using Perplexity AI.
- **Follow-up Questions:** Ask additional questions based on previously retrieved data.
- **Interactive Dashboard:** Explore results through a Streamlit interface.

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

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Soumyasriau/GreenIndexAI.git
```

2. Navigate to the project directory:

```bash
cd GreenIndexAI
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables in a `.env` file:

```env
PERPLEXITY_API_KEY=your_perplexity_api_key
DATABASE_URL=your_postgresql_database_url
```

5. Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

## 🔑 API Configuration

The application uses the Perplexity AI API for natural-language query processing and follow-up analysis.

A PostgreSQL database connection is required for the Flask API functionality.

## 📊 Dataset

The project includes an NDVI dataset containing:

- State
- Month and year
- NDVI values
- Temperature
- Rainfall
- Soil moisture
- NDVI image URLs

**Available dataset period:** January 2025 – June 2025.

## 🎯 Project Objective

To make vegetation monitoring and environmental data analysis more accessible through AI-powered natural-language interaction and data-driven insights.

## 👩‍💻 Author

**Soumya**

GitHub: [Soumyasriau](https://github.com/Soumyasriau)

---

*GreenIndex AI – Making environmental data easier to understand with AI.*