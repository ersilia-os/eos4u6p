FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia
 
RUN pip install rdkit-pypi==2022.9.5
RUN pip install signaturizer==1.1.10
RUN pip install tensorflow==2.11.0
RUN pip install numpy==1.21.6


WORKDIR /repo
COPY . /repo
