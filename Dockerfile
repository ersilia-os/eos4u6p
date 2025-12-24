FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install signaturizer==1.1.16
RUN pip install rdkit==2025.09.1
RUN pip install ersilia-pack-utils==0.1.5

WORKDIR /repo
COPY . /repo
