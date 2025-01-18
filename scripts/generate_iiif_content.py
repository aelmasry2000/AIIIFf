import os
import json

BASE_URL = "https://aelmasry2000.github.io/AIIIFf/"
IMAGE_DIR = "images/"
MANIFEST_DIR = "manifests/"
SEARCH_DIR = "search/"

def generate_manifest(image_name):
    manifest = {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@id": f"{BASE_URL}{MANIFEST_DIR}{image_name.split('.')[0]}.json",
        "@type": "sc:Manifest",
        "label": image_name,
        "service": {
            "@id": f"{BASE_URL}{SEARCH_DIR}{image_name.split('.')[0]}.json",
            "@type": "search:Service"
        },
        "sequences": [
            {
                "@type": "sc:Sequence",
                "canvases": [
                    {
                        "@id": f"{BASE_URL}{IMAGE_DIR}{image_name}",
                        "@type": "sc:Canvas",
                        "label": image_name,
                        "height": 3000,  # Update these values based on your image dimensions
                        "width": 2000,
                        "images": [
                            {
                                "@type": "oa:Annotation",
                                "motivation": "sc:painting",
                                "on": f"{BASE_URL}{IMAGE_DIR}{image_name}",
                                "resource": {
                                    "@id": f"{BASE_URL}{IMAGE_DIR}{image_name}",
                                    "@type": "dctypes:Image",
                                    "format": "image/jpeg",
                                    "height": 3000,
                                    "width": 2000
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
    return manifest

def generate_search(image_name):
    search = {
        "@context": "http://iiif.io/api/search/1/context.json",
        "@id": f"{BASE_URL}{SEARCH_DIR}{image_name.split('.')[0]}.json",
        "@type": "search:Service",
        "resources": [
            {
                "@type": "oa:Annotation",
                "motivation": "sc:painting",
                "resource": {
                    "@type": "cnt:ContentAsText",
                    "chars": f"Searchable text for {image_name}"
                },
                "on": f"{BASE_URL}{MANIFEST_DIR}{image_name.split('.')[0]}.json#xywh=10,10,100,100"
            }
        ]
    }
    return search

# Ensure directories exist
os.makedirs(MANIFEST_DIR, exist_ok=True)
os.makedirs(SEARCH_DIR, exist_ok=True)

# Generate files for each image
for image_file in os.listdir(IMAGE_DIR):
    if image_file.endswith(".jpg"):
        # Generate manifest
        manifest = generate_manifest(image_file)
        with open(f"{MANIFEST_DIR}{image_file.split('.')[0]}.json", "w") as f:
            json.dump(manifest, f, indent=2)

        # Generate search file
        search = generate_search(image_file)
        with open(f"{SEARCH_DIR}{image_file.split('.')[0]}.json", "w") as f:
            json.dump(search, f, indent=2)

print("IIIF manifests and search files generated successfully.")
