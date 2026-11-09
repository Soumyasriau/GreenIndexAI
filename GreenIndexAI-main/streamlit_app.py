from pathlib import Path
import streamlit as st
from pathlib import Path
import requests
from pathlib import Path
from PIL import Image
from pathlib import Path
from io import BytesIO
from pathlib import Path
import json
from pathlib import Path
from agent1 import query_llm  # ← NEW IMPORT
from pathlib import Path
from agent2 import answer_followup_question
from pathlib import Path
import streamlit as st
from pathlib import Path
import time
from pathlib import Path

from pathlib import Path
st.set_page_config(page_title="GreenIndex AI", layout="wide")
from pathlib import Path

from pathlib import Path
# Initialize state
from pathlib import Path
if "allow_app" not in st.session_state:
from pathlib import Path
    st.session_state.allow_app = False
from pathlib import Path
if "start_time" not in st.session_state:
from pathlib import Path
    st.session_state.start_time = time.time()
from pathlib import Path

from pathlib import Path
# Splash Screen
from pathlib import Path
if not st.session_state.allow_app:
from pathlib import Path
    st.markdown(
from pathlib import Path
        "<h1 style='text-align: center; color: green;'>🌿 GreenIndex AI</h1>",
from pathlib import Path
        unsafe_allow_html=True
from pathlib import Path
    )
from pathlib import Path

from pathlib import Path
    with st.container():
from pathlib import Path
        st.error("""
from pathlib import Path
        **Notice:**  
from pathlib import Path
        This application uses geospatial NDVI data collected from sources like **MODIS**, **Sentinel**, and other public datasets.
from pathlib import Path

from pathlib import Path
        Due to limitations in regional boundaries:
from pathlib import Path
        - States like **Telangana and Andhra Pradesh** may appear merged.
from pathlib import Path
        - Some regions such as **POK** may be missing or distorted.
from pathlib import Path
        - Mention month and year 
from pathlib import Path
    
from pathlib import Path
        **Data Range:** January 2025 – June 2025
from pathlib import Path
        """, icon="⚠️")
from pathlib import Path

from pathlib import Path
    # Calculate time elapsed
from pathlib import Path
    elapsed = time.time() - st.session_state.start_time
from pathlib import Path

from pathlib import Path
    if elapsed >= 5:
from pathlib import Path
        if st.button("✅ Proceed", use_container_width=True):
from pathlib import Path
            st.session_state.allow_app = True
from pathlib import Path
            st.rerun()
from pathlib import Path
    else:
from pathlib import Path
        remaining = int(5 - elapsed)
from pathlib import Path
        st.info(f"Please read the notice. 'Proceed' button will be enabled in {remaining} second(s).")
from pathlib import Path
        time.sleep(1)
from pathlib import Path
        st.rerun()
from pathlib import Path

from pathlib import Path
    # Block app below
from pathlib import Path
    st.stop()
from pathlib import Path

from pathlib import Path

from pathlib import Path
st.set_page_config(page_title="GreenIndex AI", layout="wide")
from pathlib import Path
st.markdown(
from pathlib import Path
        "<h1 style='text-align: center; color: green;'>🌿 GreenIndex AI</h1>",
from pathlib import Path
        unsafe_allow_html=True
from pathlib import Path
    )
from pathlib import Path

from pathlib import Path
# Load fixed NDVI data from JSON
from pathlib import Path
with open(Path(__file__).resolve().parent / "ndvi_data.json", "r") as f:
from pathlib import Path
    ndvi_json_data = json.load(f)
from pathlib import Path

from pathlib import Path
# Initialize session state
from pathlib import Path
if "history" not in st.session_state:
from pathlib import Path
    st.session_state.history = []
from pathlib import Path
if "query_history" not in st.session_state:
from pathlib import Path
    st.session_state.query_history = []
from pathlib import Path

from pathlib import Path
# Layout
from pathlib import Path
left, right = st.columns([3, 1])
from pathlib import Path

from pathlib import Path
# RIGHT PANEL — Natural Language Input
from pathlib import Path
with right:
from pathlib import Path
    st.header("NDVI Data Query (Natural Language)")
from pathlib import Path
    user_input = st.text_input("Ask a query like 'Show NDVI for states starting with A in June 2023'", key="nl_query")
from pathlib import Path

from pathlib import Path
    if st.button("Submit Query"):
from pathlib import Path
        if not user_input.strip():
from pathlib import Path
            st.warning("Please enter a query.")
from pathlib import Path
        else:
from pathlib import Path
            with st.spinner("Processing your query using AI..."):
from pathlib import Path
                try:
from pathlib import Path
                    query_list = query_llm(user_input, ndvi_json_data)  # ← REPLACED
from pathlib import Path
                    for i, query in enumerate(query_list):
from pathlib import Path
                        state = query.get("state", "").strip().lower()
from pathlib import Path
                        month = query.get("month", "").strip()
from pathlib import Path
                        year = int(query.get("year", 0))
from pathlib import Path

from pathlib import Path
                        if not (state and month and year):
from pathlib import Path
                            st.warning(f"⚠️ Skipping incomplete query #{i+1}")
from pathlib import Path
                            continue
from pathlib import Path

from pathlib import Path
                        entry = next(
from pathlib import Path
                            (row for row in ndvi_json_data if row["state"] == state and row["month"] == month and row["year"] == year),
from pathlib import Path
                            None
from pathlib import Path
                        )
from pathlib import Path

from pathlib import Path
                        if not entry:
from pathlib import Path
                            st.warning(f"⚠️ No data for {state}, {month} {year}")
from pathlib import Path
                            continue
from pathlib import Path

from pathlib import Path
                        # Try fetching image from local API
from pathlib import Path
                        img = None
from pathlib import Path
                        try:
from pathlib import Path
                            payload = {
from pathlib import Path
                                "state": state,
from pathlib import Path
                                "month": month,
from pathlib import Path
                                "year": year,
from pathlib import Path
                            }
from pathlib import Path
                            res = requests.post("https://greenindexai.onrender.com/query", json=payload)
from pathlib import Path
                            if res.status_code == 200:
from pathlib import Path
                                api_data = res.json()
from pathlib import Path
                                if "ndvi_url" in api_data:
from pathlib import Path
                                    img_res = requests.get(api_data["ndvi_url"])
from pathlib import Path
                                    if img_res.status_code == 200:
from pathlib import Path
                                        img = Image.open(BytesIO(img_res.content))
from pathlib import Path
                        except:
from pathlib import Path
                            pass
from pathlib import Path

from pathlib import Path
                        record = {
from pathlib import Path
                            "state": state,
from pathlib import Path
                            "month": month,
from pathlib import Path
                            "year": year,
from pathlib import Path
                            "ndvi_value": entry["ndvi_value"],
from pathlib import Path
                            "temperature": entry["temperature"],
from pathlib import Path
                            "rainfall": entry["rainfall"],
from pathlib import Path
                            "soilmoisture": entry["soilmoisture"],
from pathlib import Path
                        }
from pathlib import Path

from pathlib import Path
                        st.session_state.history.append({"meta": record, "image": img})
from pathlib import Path

from pathlib import Path
                        st.subheader(f"Result {i+1}")
from pathlib import Path
                        summary = (
from pathlib import Path
                            f"The NDVI data for **{state.title()}** in **{month} {year}** shows an NDVI value "
from pathlib import Path
                            f"of **{entry['ndvi_value']}**, with a temperature of **{entry['temperature']}°C**, "
from pathlib import Path
                            f"rainfall of **{entry['rainfall']}mm**, and soil moisture of **{entry['soilmoisture']}%**."
from pathlib import Path
                        )
from pathlib import Path
                        st.markdown(summary)
from pathlib import Path
                        if img:
from pathlib import Path
                            st.image(img, caption="NDVI Image", width=200)
from pathlib import Path

from pathlib import Path
                    st.rerun()
from pathlib import Path

from pathlib import Path
                except Exception as e:
from pathlib import Path
                    st.error(f"❌ AI Agent Error: {e}")
from pathlib import Path

from pathlib import Path
# LEFT PANEL — Display Results and Q&A
from pathlib import Path
with left:
from pathlib import Path
    top_container = st.container()
from pathlib import Path
    bottom_container = st.container()
from pathlib import Path

from pathlib import Path
    with top_container:
from pathlib import Path
        with st.container(height=400, border=False):
from pathlib import Path
            for i, item in enumerate(st.session_state.history):
from pathlib import Path
                m = item["meta"]
from pathlib import Path
                if m["state"].lower() == "ai response":
from pathlib import Path
                    st.markdown(f"**Q: {item['question']}**")
from pathlib import Path
                    st.markdown(f"**A: {item['answer']}**")
from pathlib import Path
                else:
from pathlib import Path
                    st.subheader(f"{m['state'].title()} — {m['month']} {m['year']}")
from pathlib import Path
                    if item["image"]:
from pathlib import Path
                        st.image(item["image"], width=500)
from pathlib import Path
                    summary = (
from pathlib import Path
                        f"In **{m['month']} {m['year']}**, the state of **{m['state'].title()}** experienced "
from pathlib import Path
                        f"an NDVI value of **{m['ndvi_value']}**, a temperature of **{m['temperature']}°C**, "
from pathlib import Path
                        f"rainfall measuring **{m['rainfall']}mm**, and soil moisture level of **{m['soilmoisture']}%**."
from pathlib import Path
                    )
from pathlib import Path
                    st.markdown(summary)
from pathlib import Path
                    st.markdown("---")
from pathlib import Path

from pathlib import Path

from pathlib import Path
    with bottom_container:
from pathlib import Path
        st.divider()
from pathlib import Path
        st.markdown("#### Ask a question based on the above data:")
from pathlib import Path
        user_query = st.text_input("Enter query here", key="query_input")
from pathlib import Path

from pathlib import Path
        if st.button("Ask"):
from pathlib import Path
            if user_query.strip() == "":
from pathlib import Path
                st.warning("Please enter a question.")
from pathlib import Path
            elif not st.session_state.history:
from pathlib import Path
                st.warning("No data available. Please run a query first.")
from pathlib import Path
            else:
from pathlib import Path
                context = ""
from pathlib import Path
                for i, h in enumerate(st.session_state.history):
from pathlib import Path
                    m = h["meta"]
from pathlib import Path
                    if m["state"].lower() == "ai response":
from pathlib import Path
                        continue
from pathlib import Path
                    context += (
from pathlib import Path
                        f"State={m['state']}, Month={m['month']}, Year={m['year']}, "
from pathlib import Path
                        f"NDVI={m['ndvi_value']}, Temperature={m['temperature']}°C, "
from pathlib import Path
                        f"Rainfall={m['rainfall']}mm, Soil Moisture={m['soilmoisture']}%\n"
from pathlib import Path
                    )
from pathlib import Path

from pathlib import Path
                try:
from pathlib import Path
                    with st.spinner("Generating analytical insight..."):
from pathlib import Path
                        answer = answer_followup_question(user_query, context)
from pathlib import Path
                        st.session_state.history.append({
from pathlib import Path
                            "meta": {
from pathlib import Path
                                "state": "AI Response",
from pathlib import Path
                                "month": "",
from pathlib import Path
                                "year": "",
from pathlib import Path
                                "ndvi_value": "",
from pathlib import Path
                                "temperature": "",
from pathlib import Path
                                "rainfall": "",
from pathlib import Path
                                "soilmoisture": ""
from pathlib import Path
                            },
from pathlib import Path
                            "image": None,
from pathlib import Path
                            "question": user_query,
from pathlib import Path
                            "answer": answer
from pathlib import Path
                        })
from pathlib import Path
                        st.rerun()
from pathlib import Path
                except Exception as e:
from pathlib import Path

from pathlib import Path
                    st.error(f"❌ AI Agent2 Error: {e}")
from pathlib import Path

from pathlib import Path

from pathlib import Path

