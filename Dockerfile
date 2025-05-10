FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -y -c conda-forge numpy=1.23.5 # I did this to be able to pass tensorflow built error
RUN conda install -y -c conda-forge gxx=15.1.0
RUN conda install -y -c conda-forge pkg-config=0.29.2
RUN conda install -y -c conda-forge hdf5=1.14.6

RUN pip install rdkit-pypi==2022.9.5
RUN pip install signaturizer==1.1.10
RUN pip install tensorflow==2.11.0
RUN pip install numpy==1.21.6
RUN pip install typing_extensions==4.12.2
RUN pip install h5py==3.8.0

WORKDIR /repo
COPY . /repo
