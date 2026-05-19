# 🔬 SCALE Workshop — Machine Learning on Edge Hardware

**Practical ML for Arduino UNO R4 & Raspberry Pi**

> A hands-on workshop repository covering machine learning from first principles all the way to deployment on embedded hardware. If you want to run ML models on an **Arduino UNO R4** or a **Raspberry Pi**, this is your starting point.

---

## 📁 What's in This Repo

| File | Description |
|------|-------------|
| `ArduinoWorkshop (2).pdf` | Full workshop guide for running ML on **Arduino UNO R4** |
| `Pi4.pdf` | Full workshop guide for running ML on **Raspberry Pi 4** |
| `handwritten_digit_recognition_CNN.ipynb` | Complete CNN tutorial — the famous MNIST digit recognition problem, built step by step |

---

## 🚀 Getting Started

### Want to run ML on Arduino UNO R4?

**→ Open `ArduinoWorkshop (2).pdf` and follow the instructions inside.**

This guide walks you through setting up TensorFlow Lite or Edge Impulse on the Arduino UNO R4, deploying a trained model, and running inference directly on the microcontroller. No prior embedded ML experience required.

### Want to run ML on Raspberry Pi?

**→ Open `Pi4.pdf` and follow the instructions inside.**

This guide covers setting up your Pi environment, installing the necessary ML libraries, and running models efficiently on the Pi's hardware. Works with Raspberry Pi 4 (recommended) and compatible boards.

---

## 🧠 The CNN Notebook

The Jupyter notebook `handwritten_digit_recognition_CNN.ipynb` is the core ML tutorial of this workshop. It covers the famous **Post Office handwritten digit recognition problem** — the same challenge that motivated the invention of CNNs in the late 1980s.

It walks through 13 complete steps:

1. Loading and visualizing the MNIST dataset
2. Understanding images as pixel grids
3. Preprocessing and normalization
4. Why flat (Dense) networks struggle with images
5. The convolution operation — visualized from scratch
6. Building a full CNN architecture with BatchNorm and Dropout
7. Data augmentation for robustness
8. Training with learning rate scheduling and early stopping
9. Confusion matrices and per-class performance
10. Visualizing feature maps — what the network actually sees
11. Learned filter weights
12. Confident vs. uncertain vs. wrong predictions
13. Saving and loading the trained model

Every concept is explained in plain language before the code. No prior deep learning knowledge required.

---

## 🛠️ Requirements

### For the Notebook (local Python environment)

```bash
pip install tensorflow numpy matplotlib seaborn scikit-learn pillow scipy
```

Then launch:

```bash
jupyter notebook handwritten_digit_recognition_CNN.ipynb
```

Tested with Python 3.10+ and TensorFlow 2.x.

### For Arduino UNO R4

See `ArduinoWorkshop (2).pdf` for the full hardware and software requirements. You will need:

- Arduino UNO R4 (Minima or WiFi variant)
- Arduino IDE 2.x
- Required libraries listed in the PDF

### For Raspberry Pi

See `Pi4.pdf` for the full setup instructions. Recommended:

- Raspberry Pi 4 (2 GB RAM minimum, 4 GB recommended)
- Raspberry Pi OS (64-bit)
- Python 3.9+

---

## 🎯 Who This Is For

This workshop is designed for:

- Students and researchers getting started with applied ML
- Engineers who want to deploy models on constrained hardware
- Anyone curious about how CNNs work under the hood
- Makers and hobbyists exploring edge AI on Arduino and Pi

No specialized hardware is needed to follow the notebook — a standard laptop is enough to train the MNIST model. The PDF guides then walk you through taking that knowledge onto real embedded hardware.

---

## 📬 About

This repository was created as part of the **SCALE Workshop** series on practical, hardware-grounded machine learning.

If you have questions or run into issues following the guides, feel free to open an Issue on this repository.

---

*Built with TensorFlow · Keras · Arduino · Raspberry Pi*
