import csv, os, struct, sys, json
from signaturizer import Signaturizer
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

DATASETS = ["{0}{1}".format(x, y) for x in "abcde" for y in "12345"]

infile = sys.argv[1]
outfile = sys.argv[2]

ROOT = os.path.abspath(os.path.dirname(__file__))
checkpoints_dir = os.path.join(ROOT, "..", "..", "checkpoints")


def read_smiles_csv(in_file):
  with open(in_file, "r") as f:
    reader = csv.reader(f)
    cols = next(reader)
    data = [r[0] for r in reader]
    return cols, data


def read_smiles_bin(in_file):
  with open(in_file, "rb") as f:
    data = f.read()

  mv = memoryview(data)
  nl = mv.tobytes().find(b"\n")
  meta = json.loads(mv[:nl].tobytes().decode("utf-8"))
  cols = meta.get("columns", [])
  count = meta.get("count", 0)

  smiles_list = [None] * count
  offset = nl + 1
  for i in range(count):
    (length,) = struct.unpack_from(">I", mv, offset)
    offset += 4
    smiles_list[i] = mv[offset : offset + length].tobytes().decode("utf-8")
    offset += length

  return cols, smiles_list


def read_smiles(in_file):
  if in_file.endswith(".bin"):
    return read_smiles_bin(in_file)
  return read_smiles_csv(in_file)


def write_out_csv(results, header, file):
  with open(file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in results:
      writer.writerow(r)


def write_out_bin(results, header, file):
  arr = np.asarray(results, dtype=np.float32)
  meta = {"columns": header, "shape": arr.shape, "dtype": "float32"}
  meta_bytes = (json.dumps(meta) + "\n").encode("utf-8")

  with open(file, "wb") as f:
    f.write(meta_bytes)
    f.truncate(len(meta_bytes) + arr.nbytes)

  m = np.memmap(
    file, dtype=arr.dtype, mode="r+", offset=len(meta_bytes), shape=arr.shape
  )
  m[:] = arr
  m.flush()


def write_out(results, header, file):
  if file.endswith(".bin"):
    write_out_bin(results, header, file)
  elif file.endswith(".csv"):
    write_out_csv(results, header, file)
  else:
    raise ValueError(f"Unsupported extension for {file!r}")


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
  output = {"result": result, "meta": None}
  return output


def refactor(output_dict):
  data = output_dict["result"]
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

smiles = read_smiles(infile)[1]
data = predict_signatures(smiles)
outputs = refactor(data)


write_out(outputs, header, outfile)
