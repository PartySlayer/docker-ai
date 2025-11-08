from flask import Flask, request, jsonify
from pizza_class import FoodClassification
import os

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify_image():
    """
    this endpoint will take care of the communication between nn and docker
    """
    if "image" not in request.files:
        return "No Image :(", 400
    
    img_directory = "./input_images"
    if not os.path.exists(img_directory):
        os.mkdir(img_directory)

    img_file = request.files["image"]
    img_path = {img_directory} + "/" + {img_file}
    img_file.save(img_path)

    #process the image
    food = FoodClassification()
    prediction = food.main(img_path)

    # returns the result as json (which food it is)

    return jsonify({"food": prediction})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)


