FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia
 
RUN pip install rdkit-pypi
RUN pip install signaturizer==1.1.10 

WORKDIR /repo
COPY . /repo