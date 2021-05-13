FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit
RUN pip install signaturizer

WORKDIR /repo
COPY . /repo
