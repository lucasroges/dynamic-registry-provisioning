import sys
import json
import random

random.seed(0)

DATASETS = {
    "nodes=100;users_per_app=4": {
        "users": [
            {
                "type": "vehicle",
                "number_of_objects": 20,
            },
            {
                "type": "pedestrian",
                "number_of_objects": 108,
            }
        ],
        "users_per_app": 4,
    },
    "nodes=196;users_per_app=4": {
        "users": [
            {
                "type": "vehicle",
                "number_of_objects": 40,
            },
            {
                "type": "pedestrian",
                "number_of_objects": 216,
            }
        ],
        "users_per_app": 4,
    },
    "nodes=100;users_per_app=16": {
        "users": [
            {
                "type": "vehicle",
                "number_of_objects": 20,
            },
            {
                "type": "pedestrian",
                "number_of_objects": 108,
            }
        ],
        "users_per_app": 16,
    },
    "nodes=196;users_per_app=16": {
        "users": [
            {
                "type": "vehicle",
                "number_of_objects": 40,
            },
            {
                "type": "pedestrian",
                "number_of_objects": 216,
            }
        ],
        "users_per_app": 16,
    },
}

USER_TYPES = {
    "vehicle": {
        "mobility_model": "edge_sim_py.pathway",
        "seconds_to_move": {
            "min": 45,
            "max": 185
        },
    },
    "pedestrian": {
        "mobility_model": "edge_sim_py.pathway",
        "seconds_to_move": {
            "min": 333,
            "max": 1000
        },
    },
}

CONTAINER_IMAGES = json.load(open("templates/container_images.json", "r"))

for dataset, details in DATASETS.items():
    template = dataset.split(";")[0]

    number_of_users = sum([user["number_of_objects"] for user in details["users"]])
    users_per_app = details["users_per_app"]
    unique_applications = number_of_users // users_per_app

    app_container_images = random.sample(CONTAINER_IMAGES[1:], unique_applications)
    container_images = [CONTAINER_IMAGES[0]] + app_container_images
    
    template_data = json.load(open(f"templates/{template}.json", "r"))
    
    template_data["container_registries"]["specifications"]["images"] = [
        {
            "name": image["name"],
            "tag": image["tag"],
        } for image in container_images
    ]
    template_data["container_images"] = container_images
    template_data["applications"]["specifications"] = [
        {
            "label": f"app-{image['name']}",
            "number_of_objects": users_per_app,
            "services": [
                {
                    "label": f"service-{image['name']}",
                    "image_digest": image["digest"],
                    "state": 0,
                }
            ]
        } for image in app_container_images
    ]
    template_data["users"] = [
        {
            "number_of_objects": user["number_of_objects"],
            "mobility_model": USER_TYPES[user["type"]]["mobility_model"],
            "seconds_to_move": USER_TYPES[user["type"]]["seconds_to_move"],
            "type": user["type"],
        } for user in details["users"]
    ]
    
    output_filename = f"{dataset}.json"
    json.dump(template_data, open(output_filename, "w"), indent=4)