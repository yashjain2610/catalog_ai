import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Constants (replace with your real ones in production)
FORM_ID = "1091525909677464"
#PAGE_ACCESS_TOKEN = "EAAKVhTIS4ZCQBOwElvvOMZARJV7YZC2qkVU9wOV6m9n84jhifciXPi5uX3oXTs5AM7bbamJeuNt2CXkFLadrfKkPSudpOjctFrVMvmkFaAOSGkyYN9pmSIEa09Gw2XVVeEjv2kJLYB3QBtpOT2Qpc7ZCzH5VRu3SeZAN4asODqDlD2Okvr39S7DEYY72E2x1Ld9itJnmyEJAMPU6YytVFbtriGMswCgZDZD"
#PAGE_ACCESS_TOKEN = "EAAKVhTIS4ZCQBOwzcup5tXsuKX5ZCsN00cUkymjBvm1OeYIe80NcGlO9BgCGr5AdKxjtIkiqYWHOzHAPItndGFmfF4JxOVbD1wcY8D7lwtxnC7jZBqWneesZASh9avIOrLepZBN2TCHoOabzsgbFNZCBsSdvyls79dcSiVtntnuOrZAgXQZC5xqdlL6m8PdlNeqbIRuZB"
# Fetch lead data from Meta
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
def fetch_leads():
    url = f"https://graph.facebook.com/v22.0/{FORM_ID}/leads?limit=500"
    params = {
        "access_token": PAGE_ACCESS_TOKEN,
        "fields": "created_time,field_data"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        leads = response.json().get("data", [])
        #print(leads)
        formatted = []
        for lead in leads:
            data = {
                "created_time": lead.get("created_time", ""),
                "full_name": "",
                "email": "",
                "phone": "",
                "store_name": ""
            }

            for field in lead.get("field_data", []):
                name = field.get("name", "").lower()
                value = ", ".join(field.get("values", [])) if "values" in field else ""

                if "name" in name and "store" not in name:
                    data["full_name"] = value
                elif "email" in name:
                    data["email"] = value
                elif "phone" in name:
                    data["phone"] = value
                elif "store" in name or "website" in name:
                    data["store_name"] = value

            formatted.append(data)

        return formatted
    else:
        st.error(f"Error fetching leads: {response.text}")
        return []

# Streamlit UI
st.title("Meta Leads Dashboard")

if st.button("Fetch Leads"):
    leads_data = fetch_leads()
    if leads_data:
        df = pd.DataFrame(leads_data)
        st.dataframe(df)
    else:
        st.info("No leads found.")