#!/usr/bin/env python3
"""
setup_model.py
Downloads MobileNetV2 TFLite model + ImageNet labels.
Run this ONCE before starting the app.
"""

import urllib.request
import os
import sys

print("=" * 55)
print("  Pi Vision - Model Setup")
print("=" * 55)

# ── Download MobileNetV2 TFLite model ──────────────────────
MODEL_URL = "https://storage.googleapis.com/tfhub-lite-models/tensorflow/lite-model/mobilenet_v2_1.0_224/1/default/1.tflite"
MODEL_PATH = "mobilenet_v2.tflite"

if os.path.exists(MODEL_PATH):
    print(f"✅ Model already exists: {MODEL_PATH}")
else:
    print("📥 Downloading MobileNetV2 model (~14 MB)...")
    print("   This is a CNN trained on 1.2 million ImageNet images.")
    
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            pct = min(100, downloaded * 100 // total_size)
            bar = "█" * (pct // 5) + "░" * (20 - pct // 5)
            print(f"\r   [{bar}] {pct}%", end="", flush=True)
    
    try:
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH, reporthook=progress)
        print(f"\n✅ Model saved: {MODEL_PATH}")
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print("   Try: wget", MODEL_URL)
        sys.exit(1)

# ── Download ImageNet labels ───────────────────────────────
LABELS_URL = "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"
LABELS_PATH = "imagenet_labels.txt"

if os.path.exists(LABELS_PATH):
    print(f"✅ Labels already exist: {LABELS_PATH}")
else:
    print("📥 Downloading ImageNet labels...")
    try:
        urllib.request.urlretrieve(LABELS_URL, LABELS_PATH)
        print(f"✅ Labels saved: {LABELS_PATH}")
    except Exception as e:
        print(f"❌ Labels download failed: {e}")
        sys.exit(1)

# Verify
with open(LABELS_PATH) as f:
    n = len(f.readlines())
print(f"\n✅ Setup complete! {n} object classes ready.")
print("\n🚀 Now run:  python3 app.py")
print("📱 Then open your browser to: http://<pi-ip-address>:5000\n")
