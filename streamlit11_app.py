{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "146d64f7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0b850bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "import importlib.util\n",
    "\n",
    "# Check if the model is installed\n",
    "model_name = \"en_core_web_sm\"\n",
    "model_spec = importlib.util.find_spec(model_name)\n",
    "\n",
    "if model_spec is None:\n",
    "    subprocess.run([\"python\", \"-m\", \"spacy\", \"download\", model_name])\n",
    "\n",
    "import spacy\n",
    "nlp = spacy.load(\"en_core_web_sm\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cf913a65",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-10 03:24:56.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-10 03:24:56.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "import streamlit as st\n",
    "import json\n",
    "\n",
    "# تحميل قاعدة البيانات\n",
    "with open('data/medical_knowledge.json', 'r', encoding='utf-8') as f:\n",
    "    knowledge_base = json.load(f)\n",
    "\n",
    "# واجهة المستخدم\n",
    "st.title(\"🤖 Medical ChatBot\")\n",
    "user_input = st.text_input(\"Ask a medical question...\")\n",
    "\n",
    "if user_input:\n",
    "    query = user_input.lower()\n",
    "    results = []\n",
    "\n",
    "    for item in knowledge_base:\n",
    "        title = item.get(\"title\", \"\").lower()\n",
    "        summary = item.get(\"summary\", \"\").lower()\n",
    "        content = item.get(\"content\", \"\").lower()\n",
    "\n",
    "        if query in title or query in summary or query in content:\n",
    "            results.append(item)\n",
    "\n",
    "    if results:\n",
    "        result = results[0]\n",
    "        st.subheader(\"🔍 Result:\")\n",
    "        st.write(\"**Title:**\", result['title'])\n",
    "        st.write(\"**Summary:**\", result.get('summary', 'No summary available'))\n",
    "        st.write(\"**Category:**\", result['category'])\n",
    "    else:\n",
    "        st.warning(\"Sorry, I couldn't find any matching information.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "959621d9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a41e499",
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
