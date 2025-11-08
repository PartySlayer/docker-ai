import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image as i

class FoodClassification:

    def __init__(self):
        self.model = tf.keras.models.load_model("pizza_steak.keras")
        self.image = None
        self.masked_image = None

    def main(self, image):
        """
        Parse and compute the image provided
        """
        self.parse_image(image)

        #get the prediction from nn
        prediction = self.model.predict(self.image)
        if prediction >= 0.5:
            return "steak"
        else:
            return "pizza"
        
    def parse_image(self, image):
        """
        Function that parses the image given
        """
        img = i.load_img(image, target_size =(224,224)) # amount of neurons of our nn
        self.image = i.img_to_array(img)
        self.image = np.expand_dims(self.image, axis=0) # adds a batch dimension, we train batches in neural networks
        self.image /= 255.0 #n ormalizing to 0-1, better and faster to compute

    # since it's a different thread no need to name = main