FROM python:3.8 as test

ADD ./requirements.txt /requirements.txt
RUN python -m pip install pip --upgrade
RUN python -m pip install pytest pylint
RUN python -m pip install -r /requirements.txt

ADD ./src /app/src
WORKDIR /app/src
RUN python -m pytest tests
RUN python -m pylint sc2sim

FROM python:3.8-slim-buster as runtime

RUN useradd worker -m
USER worker
ENV PATH=$PATH:/home/worker/.local/bin

ADD ./requirements.txt /requirements.txt
RUN python -m pip install pip --upgrade --user
RUN python -m pip install -r /requirements.txt --user

ADD ./src /app/src
WORKDIR /app/src
ENTRYPOINT ["python", "-m", "sc2sim"]
