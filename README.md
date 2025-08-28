# 🥔 Potato Disease Detection

Detect **Early Blight**, **Late Blight**, or **Healthy** potato leaves using a ResNet50 feature-extractor + cosine similarity pipeline.  
The project supports both a **local Tkinter GUI** (desktop) and a **Google Colab** notebook workflow.

---

## 🔍 Project Overview

This project uses transfer learning (ResNet50 pretrained on ImageNet) to extract 2048-D feature vectors from leaf images. Instead of training a classifier from scratch, the system compares the farmer's image to labeled groups (Early Blight, Late Blight, Healthy) using **cosine similarity** and selects the class with the highest average similarity. The app also outputs actionable treatment steps for the predicted disease and visualizes confidence as a pie chart.

---

## ✅ Features

- Uses **ResNet50** for robust feature extraction (no model training required)
- **Cosine similarity** based classification (works with small datasets)
- **Tkinter GUI** for local desktop usage (upload dataset folders & farmer image)
- **Google Colab** notebook option (upload zip files and image)
- Displays **treatment steps** per disease
- Generates a **pie chart** showing similarity distribution

---

## 🧰 Tech Stack

- Python 3.8+
- TensorFlow / Keras (ResNet50)
- scikit-learn (cosine similarity)
- Pillow (PIL) / OpenCV for image handling
- Matplotlib for visualization
- Tkinter for local GUI (desktop)
- Google Colab compatible notebook for cloud execution

---

## 📁 Repository Structure (suggested)
