import streamlit as st
import sqlite3
import pandas as pd
import ollama

# --- PAGE CONFIG ---
st.set_page_config(page_title="Hardware AI Diagnostic MVP", layout="wide")
st.title("🛡️ Engineering Diagnostic Engine (Privacy-First MVP)")
st.info("NOTE: This repository uses generated dummy data to demonstrate architectural logic while protecting proprietary engineering case studies.")

# --- IN-MEMORY DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect(':memory:') 
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE fa_cases (id TEXT, component TEXT, mode TEXT, notes TEXT)')
    dummy_rows = [
        ('FA-001', 'Cooling System', 'Overheating', 'Fan bearing failure detected.'),
        ('FA-002', 'Power Supply', 'Voltage Drop', 'Capacitor degradation on 12V rail.'),
        ('FA-003', 'Storage Controller', 'Link Failure', 'Firmware handshake timeout.'),
        ('FA-004', 'NAND Flash', 'Performance Drop', 'SLC cache saturation observed.')
    ]
    cursor.executemany('INSERT INTO fa_cases VALUES (?,?,?,?)', dummy_rows)
    return conn

conn = init_db()

# --- TABBED INTERFACE ---
tab1, tab2 = st.tabs(["📊 SQL Diagnostic Tool", "📚 Knowledge Retrieval"])

with tab1:
    st.header("Automated SQL Generation")
    user_input = st.text_input("Query the database (e.g., 'Show me all unresolved cases'):")

    if st.button("Generate & Run"):
        if user_input:
            prompt = f"Convert to SQL SELECT. Table: fa_cases. Columns: id, component, mode, notes. Query: {user_input}. Return SQL only."
            response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
            sql = response['message']['content'].strip().replace("```sql", "").replace("```", "")
            
            st.code(sql, language='sql')
            try:
                df = pd.read_sql_query(sql, conn)
                st.table(df)
            except:
                st.error("Query Error. Ensure the request matches the schema columns.")

with tab2:
    st.header("Technical Root Cause Search")
    rag_query = st.text_input("Search knowledge base (e.g., 'What caused the link failure?'):")

    if st.button("Analyze"):
        if rag_query:
            # Simulated RAG Context using the dummy cases
            context = "FA-003: Recognition failure. Handshake timeout in firmware. FA-001: Overheating due to fan bearing wear."
            prompt = f"Using this context: {context}. Answer: {rag_query}"
            resp = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
            st.success(resp['message']['content'])

st.markdown("---")
st.caption("Developed by Luke Song")