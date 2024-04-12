import os
from PIL import Image

def is_panoramic(image_path, aspect_ratio_threshold=2):
    # Open an image file
    with Image.open(image_path) as img:
        width, height = img.size  # Get image dimensions
    
    # Calculate the aspect ratio
    aspect_ratio = width / height
    
    # Check if the aspect ratio exceeds the threshold
    return aspect_ratio >= aspect_ratio_threshold

def check_folder_for_panoramic_images(folder_path, aspect_ratio_threshold=2):
    # List all files in the directory
    files = os.listdir(folder_path)
    
    # Filter out files that are images based on common extensions (add or remove as needed)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    # Dictionary to store results
    panoramic_results = {}
    
    # Check each image file
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        if is_panoramic(image_path, aspect_ratio_threshold):
            panoramic_results[image_file] = "Panoramic"
        else:
            panoramic_results[image_file] = "Not Panoramic"
    
    return panoramic_results

# Example usage
folder_path = 'path_to_your_folder'
panoramic_images = check_folder_for_panoramic_images(folder_path)
for image_name, status in panoramic_images.items():
    print(f"{image_name}: {status}")
