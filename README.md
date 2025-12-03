# 🧠 Emotion Detection Web App

------------------------------------------------------------------------

## 📖 About This Project

This project is a **Text-Based Emotion Detection Web Application**
developed using **Python and Flask**.\
The application leverages a **pretrained Transformer model from
HuggingFace** to classify emotions from user input text.

The system is capable of detecting the following emotions: - Anger -
Disgust - Fear - Joy - Sadness

It also automatically determines the **dominant emotion** based on the
highest prediction score.

This project was created for the **Natural Language Processing (NLP)**
course.

------------------------------------------------------------------------

## 🧩 Key Features

-   AI-powered emotion classification from text
-   Displays confidence score for each emotion
-   Identifies dominant emotion automatically
-   Simple web-based interface using Flask
-   Powered by a Transformer deep learning model

------------------------------------------------------------------------

## ⚙️ System Requirements

-   Python version 3.7 or higher
-   Active internet connection (for first-time model download)
-   Virtual environment support (recommended)
-   Git (optional, for repository cloning)

------------------------------------------------------------------------

## 📂 Project Directory Structure

``` text
emotion_app/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

------------------------------------------------------------------------

## 🛠️ Installation Guide

### Step 1: Create Virtual Environment

``` bash
python -m venv venv
```

Activate the environment:

Windows:

``` bash
venv\Scripts\activate
```

Linux / MacOS:

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

### Step 2: Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ How to Run the Application

1.  Make sure the virtual environment is active
2.  Run the Flask server:

``` bash
python app.py
```

3.  Open your browser and access:

``` text
http://127.0.0.1:5000
```

The emotion detection system is now ready to use.

------------------------------------------------------------------------

## 📝 How to Use

1.  Input a sentence or paragraph into the text box.
2.  Click the **Run Sentiment Analysis** button.
3.  The application will display:
    -   Emotion probability values
    -   Dominant detected emotion

------------------------------------------------------------------------

## 📌 Additional Information

-   Pretrained model used:
    https://huggingface.co/j-hartmann/emotion-english-distilroberta-base
-   Initial execution may take several minutes due to large model
    download (\~300MB).
-   After the first run, the system will operate much faster.

------------------------------------------------------------------------

## 📄 License

This project is developed exclusively for **educational purposes**.\
You may add an MIT License if deployment is required.

------------------------------------------------------------------------

## 👤 Developer

Name: Nabila Alnovera\
Technology: Python & Flask

------------------------------------------------------------------------

[Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
[Project Type](https://img.shields.io/badge/project-NLP-orange)
[Usage](https://img.shields.io/badge/usage-education-green)
