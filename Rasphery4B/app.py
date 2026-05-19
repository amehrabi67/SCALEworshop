#!/usr/bin/env python3
"""
Pi Vision - Smart Object Recognition
Uses MobileNetV2 ONNX model - works on Windows, Mac, Linux, and Raspberry Pi
"""

import io, time
import numpy as np
from flask import Flask, render_template, request, jsonify
from PIL import Image
import onnxruntime as ort

app = Flask(__name__)

print("Loading MobileNetV2 ONNX model...")
session = ort.InferenceSession("mobilenet_v2.onnx")
input_name = session.get_inputs()[0].name
print("Model loaded!")

with open("imagenet_labels.txt") as f:
    labels = [line.strip() for line in f.readlines()]
print(f"{len(labels)} classes ready")

def preprocess(pil_image):
    img = pil_image.convert("RGB").resize((224, 224), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406])
    std  = np.array([0.229, 0.224, 0.225])
    arr = (arr - mean) / std
    arr = np.transpose(arr, (2, 0, 1))
    return np.expand_dims(arr, axis=0).astype(np.float32)

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()

def classify(pil_image):
    start = time.time()
    inp = preprocess(pil_image)
    out = session.run(None, {input_name: inp})[0][0]
    probs = softmax(out)
    elapsed = round((time.time() - start) * 1000, 1)
    top5 = np.argsort(probs)[::-1][:5]
    results = []
    for i in top5:
        label = labels[i] if i < len(labels) else "Unknown"
        label = label.replace("_", " ").title()
        results.append({"label": label, "confidence": round(float(probs[i]) * 100, 2)})
    return results, elapsed

FUN_FACTS = {
    "cat": "Cats sleep 12-16 hours a day and have 32 muscles in each ear!",
    "dog": "Dogs have a sense of smell 100,000x better than humans.",
    "banana": "Bananas are technically berries, but strawberries are not!",
    "pizza": "Americans eat approximately 3 billion pizzas per year.",
    "laptop": "The first laptop weighed 10.7 kg (24 lbs)!",
    "phone": "There are more mobile phones on Earth than people.",
    "flower": "Flowers have been around for at least 130 million years!",
}

def get_fun_fact(label):
    for key, fact in FUN_FACTS.items():
        if key in label.lower():
            return fact
    return None

@app.route("/")
def index():
    return render_template("index.html", use_pi_camera=False)

@app.route("/classify", methods=["POST"])
def classify_route():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400
        pil_image = Image.open(request.files["image"].stream)
        results, elapsed = classify(pil_image)
        top_label = results[0]["label"] if results else "Unknown"
        return jsonify({
            "success": True,
            "predictions": results,
            "inference_time_ms": elapsed,
            "top_label": top_label,
            "fun_fact": get_fun_fact(top_label)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": "MobileNetV2-ONNX"})

if __name__ == "__main__":
    print("\n Pi Vision is running!")
    print("Open your browser at: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
