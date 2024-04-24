import os

# Create folder
list_folder = [
    "images",
    "output",
    "models",
]

for folder in list_folder:
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder, exist_ok=True)

# Install model
print("Set up done")
