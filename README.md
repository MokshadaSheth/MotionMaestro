# 🎮 Motion Maestro — Real-Time Gesture-Based Gaming System

**Motion Maestro** is an AI-powered, real-time gesture recognition system that transforms hand movements into game controls — enabling **completely hands-free gameplay**.

With \<30ms latency and accurate hand tracking, it delivers **intuitive**, **low-latency**, and **accessible** gaming experiences using **OpenCV**, **MediaPipe**, and **pydirectinput**.

-----

## 🚀 Features

  - ⚡ **Real-Time Gesture Control**
    Smooth and responsive gesture recognition with under 30ms latency.

  - 🖐️ **Robust Hand Tracking**
    Powered by **MediaPipe** for accurate and stable hand landmark detection.

  - ✅ **User-Tested & Validated**
    Tested with **200+ users**, resulting in improved precision and interaction quality.

  - 🧼 **Touchless Control**
    Perfect for hygiene-sensitive or public environments.

-----

## 🎥 Watch the Demo

▶ [Watch on YouTube](https://youtube.com/shorts/nSSYuMrAxec)

-----

## 📘 Documentation

📄 [**User Manual & Usage Guide**](https://drive.google.com/drive/folders/1VIweqyhdSRaRY0ucblNaBlsVfugNLJYs?usp=sharing)

-----

## 🛠️ Tech Stack

  - **Python 3.x**
  - **OpenCV**
  - **MediaPipe**
  - **pydirectinput**
  - **NumPy**

-----

## 📁 Use Cases

  - 🎯 Casual hands-free gaming
  - ♿ Accessibility for users with limited mobility
  - 🧠 Educational games using physical activity
  - 🧼 Touchless control for public/shared setups

-----

## 🔧 Installation & Setup

### 1\. Clone the Repository

📦 Installation & Setup Guide
Follow these steps to set up and run Motion Maestro on your local machine:

🧰 Prerequisites
Ensure you have the following installed:

| Tool | Version | Download Link |
| :--- | :--- | :--- |
| Python | 3.7 to 3.10 | [python.org/downloads](https://www.python.org/downloads/) |
| Git | Latest | [git-scm.com](https://git-scm.com/) |
| pip | Latest | Comes with Python (`python -m ensurepip --upgrade`) |

✅ Make sure Python is added to your system's PATH.

🚀 Installation Steps
1️⃣ Clone the Repository

```bash
git clone https://github.com/MokshadaSheth/MotionMaestro.git
cd MotionMaestro
```

2️⃣ Create and Activate a Virtual Environment
A virtual environment keeps dependencies isolated to this project.

🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

🐧 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

3️⃣ Install Project Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

⚠️ If requirements.txt is missing or incomplete, add the following manually:

```txt
opencv-python
mediapipe
numpy
pydirectinput
```

4️⃣ Run the Application

```bash
python manage.py runserver
```

The webcam will activate and begin tracking your hand gestures for controlling games.

🎮 Usage Tips
✅ Ensure your webcam is not being used by other apps.

✅ Good lighting improves hand tracking accuracy.

✅ Use full hand gestures (like thumbs up, palm open) for best detection.

✅ The system is optimized for games that use arrow keys, spacebar, etc.

🛠️ Optional: Create an Executable (Windows only)
To run the app without needing Python every time:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

You’ll find the `.exe` file in the `dist/` folder.

🧼 To Clean Up
When you're done:

```bash
deactivate  # Exit virtual environment
rm -r venv  # Delete the environment folder
```

On Windows: use `rmdir /s venv` instead of `rm`.

🧠 Troubleshooting
| Problem | Solution |
| :--- | :--- |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again inside your virtual environment |
| Webcam not working | Close apps like Zoom or Teams that might be using your camera |
| Gestures not detected | Ensure your full hand is visible and well-lit |
