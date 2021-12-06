if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")
    get_wsgi_application()

import json
import logging
import os
from os.path import join

import requests
from django.conf import settings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # make tensorflow shut up

from apps.backend import models  # noqa: 402

class YourPredictor:
    def __init__(self):
        self.model_url = settings.TF_SERVING_BASE_URL + "<your_tfserving_modelname>:predict"
        self.file_path = join(settings.BASE_DIR, "data", "<your_tfserving_modelname>")
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Predictor initialized.")

    def preprocess(self, input: str):
        ...

    def call_model(self, model_url, processed_input):
        headers = {"content-type": "application/json"}
        data = json.dumps({"signature_name": "serving_default", "inputs": processed_input})
        json_response = requests.post(model_url, data=data, headers=headers)
        if json_response.status_code != 200:
            print(json_response.json()["error"])
            raise Exception()
        return json_response.json()["outputs"][0]

    def postprocess(self, prediction_result):
        ...

    def predict(self, input):
        input = self.preprocess(input)
        output = self.call_model(self.model_url, input)
        output = self.postprocess(output)
        return output


class YourBackbone:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.predictor = YourPredictor()

    def your_func(self, input):
        ...


if __name__ == "__main__":
    # The way it's done here is only for testing/debugging, in production (and also if you're not explicitly testing
    # tf-models), there is a docker-container instead!!

    from contextlib import nullcontext

    from apps.backend.util.tf_model_server import TFModelServer

    input, expected = "<input>", "<expected>"
    with (
        TFModelServer(8501, "<your_tfserving_modelname>", model_base_path=settings.BASE_DIR / "data" / "<your_tfserving_modelname>")
        if settings.TF_SERVING_HOST == "localhost"
        else nullcontext()
    ):
        predictor = YourPredictor()
        print(predictor.predict(input))

        backbone = YourBackbone()
        backbone.your_func(input)

