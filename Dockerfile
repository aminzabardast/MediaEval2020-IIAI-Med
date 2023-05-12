FROM pytorch/pytorch:1.3-cuda10.1-cudnn7-runtime
LABEL authors="amin"

RUN conda install pytorch=1.3.1 torchvision=0.4.2 cudatoolkit=10.0 --yes
RUN pip install opencv-python==3.4.2.17 tensorboardX==2.0
