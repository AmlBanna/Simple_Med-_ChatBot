import streamlit as st
import json

# تحميل قاعدة البيانات
with open('data/medical_knowledge_with_keywords.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

# واجهة المستخدم
st.title("🤖 Medical ChatBot")
user_input = st.text_input("Ask a medical question...")

if user_input:
    # البحث البسيط عن الكلمات المفتاحية
    results = [item for item in knowledge_base if any(kw in user_input.lower() for kw in item.get('keywords', []))]
    
    if results:
        result = results[0]
        st.subheader("🔍 Result:")
        st.write("**Title:**", result['title'])
        st.write("**Summary:**", result.get('summary', 'No summary available'))
        st.write("**Category:**", result['category'])
    else:
        st.warning("Sorry, I couldn't find any matching information.")
