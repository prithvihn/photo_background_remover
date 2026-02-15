# ✨ AI Background Remover

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![RemBG](https://img.shields.io/badge/AI_Powered-RemBG-8A2BE2?style=for-the-badge)

A sleek, user-friendly web application built with Streamlit that allows users to instantly remove backgrounds from photos using AI-powered precision. 

## 📸 App Preview

![AI Background Remover Screenshot](assets/screenshot.png)



## 🌟 Features

* 🚀 **Fast:** Process and remove backgrounds in just a matter of seconds.
* 🎯 **Accurate:** Utilizes `rembg` for high-quality, AI-powered edge detection and background removal.
* 💯 **100% Free:** Completely free to use with no hidden watermarks or usage limits.
* 📁 **Easy Uploads:** Simple drag-and-drop interface supporting JPG, JPEG, and PNG files (up to 200MB).
* 👀 **Side-by-Side Comparison:** Instantly compare your original image with the newly generated transparent result.
* 💾 **Direct Download:** One-click download button to save your transparent PNG result directly to your device.

## 🛠️ Tech Stack

* **Frontend & Framework:** [Streamlit](https://streamlit.io/)
* **Background Removal AI:** [RemBG](https://github.com/danielgatis/rembg)
* **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites
Make sure you have Python installed (Python 3.8+ recommended).

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/prithvihn/photo_background_remover.git](https://github.com/prithvihn/photo_background_remover.git)
   cd photo_background_remover
   Create and activate a virtual environment (Recommended):

2. First, create the environment and proceed further

```Bash
python -m venv venv
Then, activate it depending on your operating system:

On Windows:

Bash
venv\Scripts\activate

On macOS/Linux:
Bash
source venv/bin/activate

Install the required dependencies:
Bash
pip install -r requirements.txt

Run the Streamlit app:
Bash
streamlit run app.py
