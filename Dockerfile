FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia
 
RUN pip install rdkit==2024.03.3
RUN pip install signaturizer==1.1.10
RUN pip install numpy==1.26.4

WORKDIR /repo
COPY . /repo