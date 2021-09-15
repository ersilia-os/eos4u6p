from signaturizer import Signaturizer
import pickle
import os

from typing import List
from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.types import JsonSerializable
from bentoml.service import BentoServiceArtifact

DATASETS = ["{0}{1}".format(x, y) for x in "ABCDE" for y in "12345"]

VERSION = "2020_02"


def load_model():
    mdl = SignaturizerModel()
    return mdl


class SignaturizerModel(object):
    def __init__(self):
        self.signaturizer = None

    def _load_signaturizer(self):
        if self.signaturizer is None:
            self.signaturizer = Signaturizer("GLOBAL", version=VERSION, verbose=True)

    def predict(self, smiles_list):
        self._load_signaturizer()
        X = self.signaturizer.predict(smiles_list).signature
        result = []
        for i in range(X.shape[0]):
            result += [{"signature": list(X[i])}]
        return result


class SignaturizerArtifact(BentoServiceArtifact):
    """Dummy artifact"""

    def __init__(self, name):
        super(SignaturizerArtifact, self).__init__(name)
        self._model = None
        self._extension = ".pkl"

    def _model_file_path(self, base_path):
        return os.path.join(base_path, self.name + self._extension)

    def pack(self, model):
        self._model = model
        return self

    def load(self, path):
        model_file_path = self._model_file_path(path)
        model = pickle.load(open(model_file_path, "rb"))
        return self.pack(model)

    def get(self):
        return self._model

    def save(self, dst):
        pickle.dump(self._model, open(self._model_file_path(dst), "wb"))


@artifacts([SignaturizerArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput(), batch=True)
    def predict(self, input: List[JsonSerializable]):
        input = input[0]
        smiles_list = [inp["input"] for inp in input]
        output = self.artifacts.model.predict(smiles_list)
        return [output]
