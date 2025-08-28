import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from google.colab import files
import zipfile
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt


# Step 1: Upload ZIP files for A, B, C (Healthy)

print("Upload ZIP file for group A (Early Blight) images")
uploaded_A = files.upload()
for fn in uploaded_A.keys():
    with zipfile.ZipFile(fn, 'r') as zip_ref:
        zip_ref.extractall("A")

print("Upload ZIP file for group B (Late Blight) images")
uploaded_B = files.upload()
for fn in uploaded_B.keys():
    with zipfile.ZipFile(fn, 'r') as zip_ref:
        zip_ref.extractall("B")

print("Upload ZIP file for group C (Healthy) images")
uploaded_C = files.upload()
for fn in uploaded_C.keys():
    with zipfile.ZipFile(fn, 'r') as zip_ref:
        zip_ref.extractall("C")


# Step 2: Upload Farmer image

print("Upload Farmer image")
uploaded_farmer = files.upload()
farmer_image_path = list(uploaded_farmer.keys())[0]


# Step 3: Feature extraction using ResNet50

model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def get_feature_vector(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x, verbose=0)
    return features  # 1x2048 vector


# Step 4: Compare farmer image to groups

A_images = [os.path.join("A", f) for f in os.listdir("A")]
B_images = [os.path.join("B", f) for f in os.listdir("B")]
C_images = [os.path.join("C", f) for f in os.listdir("C")]

farmer_vec = get_feature_vector(farmer_image_path)

def find_most_similar(group_images, farmer_vec):
    sims = []
    for img in group_images:
        vec = get_feature_vector(img)
        sim = cosine_similarity(vec, farmer_vec)[0][0]
        sims.append(sim)
    avg_sim = np.mean(sims)
    return avg_sim

sim_A = find_most_similar(A_images, farmer_vec)
sim_B = find_most_similar(B_images, farmer_vec)
sim_C = find_most_similar(C_images, farmer_vec)


# Step 5: Prediction

similarities = {"EARLY BLIGHT": sim_A, "LATE BLIGHT": sim_B, "HEALTHY": sim_C}
predicted_group = max(similarities, key=similarities.get)

print("Similarity scores:")
for group, score in similarities.items():
    print(f"{group}: {score:.4f}")

print(f"\nPrediction: Farmer image is closer to {predicted_group} ✅")


# Step 6: Pie chart visualization

total = sim_A + sim_B + sim_C
sizes = [sim_A/total*100, sim_B/total*100, sim_C/total*100]
labels = ["EARLY BLIGHT", "LATE BLIGHT", "HEALTHY"]
colors = ['#FF9999','#66B2FF','#99FF99']
explode = (0.05, 0.05, 0.05)

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title('Similarity Percentage with Farmer Image')
plt.show()
