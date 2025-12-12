{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "75cd0fb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-12-09 14:32:08.031 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "st.set_page_config(\n",
    "    page_title=\"Hospital Readmission Prediction\",\n",
    "    page_icon=\"🏥\",\n",
    "    layout=\"centered\",\n",
    ")\n",
    "\n",
    "# Animation\n",
    "st.markdown(\"\"\"\n",
    "    <style>\n",
    "    .title {animation: fadeIn 2s;}\n",
    "    @keyframes fadeIn {from {opacity:0;} to {opacity:1;}}\n",
    "    </style>\n",
    "\"\"\", unsafe_allow_html=True)\n",
    "\n",
    "# LOGO\n",
    "st.markdown(\"\"\"\n",
    "<center>\n",
    "<img src=\"https://cdn-icons-png.flaticon.com/512/2966/2966482.png\"\n",
    "     width=\"120\">\n",
    "</center>\n",
    "\"\"\", unsafe_allow_html=True)\n",
    "\n",
    "# TITLE\n",
    "st.markdown(\"<h1 class='title' align='center'>Hospital Readmission Prediction</h1>\", unsafe_allow_html=True)\n",
    "\n",
    "# DESCRIPTION\n",
    "st.write(\"Predict the chance of patient being readmitted within 30 days after discharge\")\n",
    "\n",
    "# LOAD MODEL\n",
    "model = pickle.load(open(\"model.pkl\",\"rb\"))\n",
    "\n",
    "# INPUT FORM\n",
    "st.subheader(\"Patient Inputs 👇\")\n",
    "\n",
    "age = st.number_input(\"Age\", min_value=0, max_value=120)\n",
    "\n",
    "days = st.number_input(\"Days in hospital\", min_value=1)\n",
    "\n",
    "glucose = st.number_input(\"Max Glucose\", min_value=0)\n",
    "\n",
    "a1c = st.number_input(\"A1C test result\", min_value=0.0, max_value=20.0, step=0.1)\n",
    "\n",
    "# BUTTON\n",
    "if st.button(\"Predict\"):\n",
    "    \n",
    "    features = np.array([[age, days, glucose, a1c]])\n",
    "\n",
    "    pred = model.predict(features)[0]\n",
    "    \n",
    "    if pred == 0:\n",
    "        result = \"NO readmission\"\n",
    "        color = \"green\"\n",
    "    elif pred == 1:\n",
    "        result = \"Readmission after 30 days\"\n",
    "        color = \"orange\"\n",
    "    else:\n",
    "        result = \"Readmission within 30 days\"\n",
    "        color = \"red\"\n",
    "    \n",
    "    st.markdown(f\"\"\"\n",
    "    <h2 style='color:{color};'>\n",
    "    🔥 Prediction: {result}\n",
    "    </h2>\n",
    "    \"\"\", unsafe_allow_html=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
