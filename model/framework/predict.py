import sys
import os
import csv
from signaturizer import Signaturizer

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

DATASETS = ["{0}{1}".format(x, y) for x in "abcde" for y in "12345"]

infile = sys.argv[1]
outfile = sys.argv[2]

ROOT = os.path.abspath(os.path.dirname(__file__))
checkpoints_dir = os.path.join(ROOT, "..", "checkpoints")

def get_model_path(ds):
    return os.path.join(checkpoints_dir, ds)

def predict_signatures(smiles_list):
    res_ = {}
    for ds in DATASETS:
        path = get_model_path(ds.upper())
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

def refactor(output_dict):
    data = output_dict['result']
    R = []
    for row in data:
        r = []
        for dataset in DATASETS:
            values = row[dataset]
            r += values
        R += [r]
    return R

header = []
for x in "abcde":
    for y in "12345":
        for i in range(128):
            header += ["{0}{1}_{2}".format(x, y, str(i).zfill(3))]

with open(infile, "r") as f:
    smiles = []
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]

data = predict_signatures(smiles)
outputs = refactor(data)


with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in outputs:
        writer.writerow(r)
