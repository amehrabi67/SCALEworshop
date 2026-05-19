# 🍓 Pi Vision — Smart Object Recognition for Raspberry Pi 4
### A CNN-powered AI camera app for students!

---

## What Does This Do?

Pi Vision is a web app that runs **entirely on your Raspberry Pi 4** (no internet needed after setup).  
You open a webpage on your phone or laptop, take a photo, and the Pi uses a **CNN (Convolutional Neural Network)** called **MobileNetV2** to identify what's in the picture from **1,000 different categories** — animals, food, vehicles, household objects, and more!

**What students learn:**
- How CNNs (deep learning) recognize images
- What "inference" means (running a trained model)
- Edge AI: running AI on small devices, not the cloud
- Python, Flask web servers, REST APIs

---

## Hardware Needed

| Item | Notes |
|------|-------|
| Raspberry Pi 4 Model B | Any RAM (2GB+ recommended) |
| MicroSD card | 16GB+ with Raspberry Pi OS |
| Phone or laptop (same WiFi) | To use the web interface |
| Pi Camera Module v2/v3 *(optional)* | OR just use phone camera + upload |

---

## STEP 1 — Flash Raspberry Pi OS

If you haven't already:
1. Download **Raspberry Pi Imager**: https://www.raspberrypi.com/software/
2. Flash **Raspberry Pi OS (64-bit, Bookworm)** to your SD card
3. Enable SSH & WiFi in the imager settings
4. Boot your Pi and connect via SSH or a monitor

---

## STEP 2 — Install System Dependencies

Open a terminal on your Pi and run these commands **one by one**:

```bash
# Update everything first
sudo apt update && sudo apt upgrade -y

# Install Python tools
sudo apt install -y python3-pip python3-venv git

# Install image libraries
sudo apt install -y libjpeg-dev zlib1g-dev libopenblas-dev

# If using Pi Camera Module v2/v3:
sudo apt install -y python3-picamera2
```

---

## STEP 3 — Copy the Project to Your Pi

On your Pi, create a project folder:

```bash
mkdir ~/pi_vision
cd ~/pi_vision
```

Then copy all these files into that folder:
- `app.py`
- `setup_model.py`
- `templates/index.html`

*(You can use `scp`, FileZilla, or just paste the code using nano/vim)*

---

## STEP 4 — Install Python Packages

```bash
cd ~/pi_vision

# Install required Python packages
pip3 install flask pillow numpy --break-system-packages

# Install TFLite Runtime (lightweight TensorFlow for Pi)
pip3 install tflite-runtime --break-system-packages
```

> **Why tflite-runtime and not full TensorFlow?**  
> Full TensorFlow is huge (~500MB) and slow on Pi. TFLite Runtime is only ~30MB and runs 5–10x faster!

---

## STEP 5 — Download the AI Model

```bash
cd ~/pi_vision
python3 setup_model.py
```

This downloads:
- **MobileNetV2** model (~14MB) — a CNN trained on 1.2 million images
- **ImageNet labels** — the 1,000 object categories it knows

---

## STEP 6 — Run Pi Vision!

```bash
cd ~/pi_vision
python3 app.py
```

You should see:
```
✅ Model loaded! Input size: 224x224
✅ 1001 classes available
🚀 Pi Vision is running!
📱 Open your browser and go to: http://<your-pi-ip>:5000
```

Find your Pi's IP address with:
```bash
hostname -I
```

Then open a browser on your phone/laptop and go to:
```
http://192.168.x.x:5000
```
*(replace with your actual IP)*

---

## How to Use

1. Open the webpage on your phone or laptop
2. Tap **"Upload a Photo"** and take a picture (or pick one from your gallery)
3. Press **"Identify Object"**
4. See the top 5 predictions with confidence percentages!

---

## How the CNN Works (Educational Explanation)

```
Your Photo (640x480)
        │
        ▼
   Resize to 224×224
        │
        ▼
  MobileNetV2 CNN
  ┌─────────────────────────────────────┐
  │  Layer 1: Detects edges & corners   │
  │  Layer 2: Detects shapes & textures │
  │  Layer 3: Detects object parts      │
  │  ...32 more layers...               │
  │  Final: 1000 class probabilities    │
  └─────────────────────────────────────┘
        │
        ▼
  "Golden Retriever: 94.2%"
```

MobileNetV2 uses a clever technique called **depthwise separable convolutions** which makes it 8–9x faster than a regular CNN while staying accurate — perfect for running on a Raspberry Pi!

---

## Performance on Pi 4

| Metric | Value |
|--------|-------|
| Inference time | ~150–400ms |
| Model size | 14 MB |
| RAM usage | ~80 MB |
| Accuracy (ImageNet) | ~71.8% top-1 |

---

## 🌟 Cool Extension Ideas for Students

1. **Plant Identifier** — retrain on a plant dataset (PlantNet)
2. **Recycle Sorter** — classify trash: plastic, paper, metal, glass  
3. **Face Emotion Detector** — use a different model for emotions
4. **Live Video Stream** — add continuous classification every 2 seconds
5. **Sound Alerts** — use `espeak` to say the object name out loud!
6. **LED Feedback** — light up different colored LEDs based on category

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'tflite_runtime'`**
```bash
pip3 install tflite-runtime --break-system-packages
```

**`ModuleNotFoundError: No module named 'flask'`**
```bash
pip3 install flask --break-system-packages
```

**App is slow on first run**
- Normal! The model takes a few seconds to warm up.
- After that, each classification takes ~200-400ms.

**Can't connect from phone**
- Make sure phone and Pi are on the same WiFi network
- Check your Pi's IP with: `hostname -I`
- Make sure firewall allows port 5000: `sudo ufw allow 5000`

**Pi Camera not working**
```bash
sudo raspi-config  # → Interface Options → Camera → Enable
sudo reboot
```

---

## File Structure

```
pi_vision/
├── app.py              ← Main Flask server + CNN inference
├── setup_model.py      ← Downloads MobileNetV2 model
├── mobilenet_v2.tflite ← CNN model (downloaded by setup)
├── imagenet_labels.txt ← 1000 class names (downloaded by setup)
├── README.md           ← This file
└── templates/
    └── index.html      ← Web interface (mobile-friendly)
```
