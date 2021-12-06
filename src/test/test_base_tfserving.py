import os
from contextlib import nullcontext

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")
get_wsgi_application()
from django.conf import settings  # noqa: E402

from apps.backend.util.tf_model_server import TFModelServer  # noqa: E402

#<import your predictor>

def test_something_tfserving():
    input, expected = "<input>", "<expected>"
    with (
        TFModelServer(8501, "<your_tfserving_modelname>", model_base_path=settings.BASE_DIR / "data" / "<your_tfserving_modelname>")
        if settings.TF_SERVING_HOST == "localhost"
        else nullcontext()
    ):
        # predictor = YourPredictor()
        # res = predictor.predict(input)
        # assert res == expected
        assert True
