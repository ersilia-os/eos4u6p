from src.service import load_model
from src.service import Service

import os

root = os.path.dirname(os.path.realpath(__file__))
mdl = load_model()

service = Service()
service.pack("model", mdl)
service.save()
