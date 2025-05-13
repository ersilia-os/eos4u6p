FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia


RUN conda install -c conda-forge numpy=1.23.5
RUN conda install -c conda-forge hdf5=1.14.6 
RUN pip install rdkit-pypi==2022.9.5
RUN pip install signaturizer==1.1.10
RUN pip install tensorflow==2.11.0 --no-deps
RUN pip install typing-extensions==4.12.2

WORKDIR /repo
COPY . /repo
