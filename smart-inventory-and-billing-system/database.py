import os
import streamlit as st
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", st.secrets.get("DB_HOST")),
        database=os.getenv("DB_NAME", st.secrets.get("DB_NAME")),
        user=os.getenv("DB_USER", st.secrets.get("DB_USER")),
        password=os.getenv("DB_PASSWORD", st.secrets.get("DB_PASSWORD")),
        port=os.getenv("DB_PORT", st.secrets.get("DB_PORT"))
    )

conn = connection()