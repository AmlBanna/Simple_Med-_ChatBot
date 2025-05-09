{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "63b57750",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-10 02:08:06.217 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.471 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\acer\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-05-10 02:08:06.473 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.474 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.474 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.478 Session state does not function when running a script without `streamlit run`\n",
      "2025-05-10 02:08:06.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 02:08:06.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import json\n",
    "import re\n",
    "from difflib import get_close_matches\n",
    "\n",
    "# تحميل قاعدة البيانات\n",
    "with open('data/medical_knowledge_with_keywords.json', 'r', encoding='utf-8') as f:\n",
    "    knowledge_base = json.load(f)\n",
    "\n",
    "def clean_text(text):\n",
    "    return re.sub(r'[^\\w\\s]', '', text.lower())\n",
    "\n",
    "def find_best_match(question):\n",
    "    question = clean_text(question)\n",
    "    matches = []\n",
    "\n",
    "    for item in knowledge_base:\n",
    "        title = clean_text(item['title'])\n",
    "        summary = clean_text(item.get('summary', ''))\n",
    "        content = clean_text(item.get('content', ''))\n",
    "\n",
    "        if question in title or question in summary or question in content:\n",
    "            matches.append(item)\n",
    "\n",
    "    if not matches:\n",
    "        all_titles = [clean_text(item['title']) for item in knowledge_base]\n",
    "        close_matches = get_close_matches(question, all_titles, n=1, cutoff=0.5)\n",
    "        if close_matches:\n",
    "            best_title = close_matches[0]\n",
    "            for item in knowledge_base:\n",
    "                if clean_text(item['title']) == best_title:\n",
    "                    return item\n",
    "\n",
    "    return matches[0] if matches else None\n",
    "\n",
    "# واجهة Streamlit\n",
    "st.title(\"🤖 الشات بوت الطبي\")\n",
    "st.markdown(\"اكتب سؤالك الطبي وسيقوم البوت بإيجاد المعلومات المناسبة من الكتب.\")\n",
    "\n",
    "user_input = st.text_input(\"اكتب سؤالك هنا...\")\n",
    "\n",
    "if user_input:\n",
    "    result = find_best_match(user_input)\n",
    "    if result:\n",
    "        st.subheader(\"🔍 تم العثور على نتيجة:\")\n",
    "        st.markdown(f\"**العنوان:** {result['title']}\")\n",
    "        st.markdown(f\"**الملخص:** {result.get('summary', 'لا يوجد ملخص')}\")\n",
    "        st.markdown(f\"**المصدر:** {result.get('book', '-')}\")\n",
    "    else:\n",
    "        st.warning(\"عذرًا، لا توجد معلومات متاحة لهذا السؤال.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb1ae186",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
