from scripts import label_image_scene as label_img_scene
import os
import cv2
import numpy as np
from flask import Flask, make_response, request, jsonify, current_app

from flask_cors import CORS, cross_origin
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

CORS(app)
# cors = CORS(app, resources={r"/": {"origins": "http://localhost:8001/"}})


@app.route("/", methods=["GET", "POST"])
def index():
    return "<h1> Deployed to Heroku</h1>"


@app.route("/getimage", methods=["POST"])
def getimage():
    try:

        data = (request.data.decode()).split(",")[1]
        body = base64.decodebytes(data.encode("utf-8"))
        img = Image.open(BytesIO(body))
        img = np.array(img)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # cv2.imshow("name", RGB_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        scene_class = label_img_scene.classify(RGB_img)
        # make_response = jsonify({"scene": scene_class})
        # make_response.headers.add(
        #     "Access-Control-Allow-Origin", "http://localhost:8001/"
        # )
        # make_response.headers.add(
        #     "Access-Control-Allow-Headers", "Content-Type,Authorization"
        # )
        # make_response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
        # make_response.headers.add("Access-Control-Allow-Credentials", "true")
        # print(make_response)
        return scene_class

    except Exception as e:
        print(e)
        return "error"


if __name__ == "__main__":
    app.run()
