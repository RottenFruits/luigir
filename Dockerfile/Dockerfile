FROM ubuntu:18.04

#set up timezone
#https://sleepless-se.net/2018/07/31/docker-build-tzdata-ubuntu/
RUN DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata
# timezone setting
ENV TZ=Asia/Tokyo

#print command
RUN set -x

#install R
RUN apt-get update && \
    apt-get install -y --no-install-recommends sudo ed clang ccache software-properties-common dirmngr gpg-agent gdebi-core

RUN sudo apt-get update && \
    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | sudo apt-key add - && \
    sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' && \
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
    sudo apt-get update && \
    sudo apt-get install -y r-base

#install luigi
RUN sudo apt install -y python-pip python3-pip &&\
    pip3 install luigi

RUN mkdir /home/examples
COPY examples/ /home/examples