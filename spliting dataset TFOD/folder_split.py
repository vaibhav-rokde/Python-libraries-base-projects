import os
import random
from sklearn.model_selection import train_test_split

# Path to the directory containing the images and annotations
data_dir = "/path/to/data/dir"

# Get a list of all the image filenames
image_files = [f for f in os.listdir(data_dir) if f.endswith(".jpg")]

# Split the image filenames into train and test sets with an 80:20 ratio
train_files, test_files = train_test_split(image_files, test_size=0.2)

# Create subdirectories for the train and test sets
train_dir = os.path.join(data_dir, "train")
test_dir = os.path.join(data_dir, "test")
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Move the train images and annotations to the train subdirectory
for file in train_files:
    image_file = os.path.join(data_dir, file)
    annotation_file = os.path.join(data_dir, file.replace(".jpg", ".xml"))
    os.rename(image_file, os.path.join(train_dir, file))
    os.rename(annotation_file, os.path.join(train_dir, file.replace(".jpg", ".xml")))

# Move the test images and annotations to the test subdirectory
for file in test_files:
    image_file = os.path.join(data_dir, file)
    annotation_file = os.path.join(data_dir, file.replace(".jpg", ".xml"))
    os.rename(image_file, os.path.join(test_dir, file))
    os.rename(annotation_file, os.path.join(test_dir, file.replace(".jpg", ".xml")))
