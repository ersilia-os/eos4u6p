import sys, os
import json
import csv
from signaturizer import Signaturizer

DATASETS = ["{0}{1}".format(x, y) for x in "ABCDE" for y in "12345"]

infile = sys.argv[1]
outfile = sys.argv[2]

ROOT = os.path.abspath(os.path.dirname(__file__))
checkpoints_dir = os.path.join(ROOT, "..", "checkpoints")

def get_model_path(ds):
    return os.path.join(checkpoints_dir, ds)

def predict(smiles_list):
    res_ = {}
    for ds in DATASETS:
        path = get_model_path(ds)
        sign = Signaturizer(model_name=path, local=True)
        X = sign.predict(smiles_list).signature
        res_[ds] = X
    result = []
    for i in range(len(smiles_list)):
        d = {}
        for k, v in res_.items():
            d[k] = list([float(x) for x in v[i]])
        result += [d]
    output = {
        'result': result,
        'meta': None
    }
    return output

with open(infile, "r") as f:
    smiles = []
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]

data = predict(smiles)

with open(outfile, "w") as f:
    json.dump(data, f, indent=4)
