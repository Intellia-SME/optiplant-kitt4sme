FROM python:3.8-slim-bullseye

LABEL maintener="Michael Loukeris"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER=1

EXPOSE 8000

RUN apt-get update && apt-get install --no-install-recommends git -y \
   && rm -rf /var/lib/apt/lists/*

RUN groupadd -r intellia && useradd -r --create-home -g intellia intellia

USER intellia

ENV PATH="${PATH}:/home/intellia/.local/bin"

WORKDIR /home/intellia

COPY ./requirements.txt ./requirements.txt

RUN set -eux \
 && pip install --no-cache-dir --user --upgrade pip \
 && pip install --no-cache-dir --user -r requirements.txt

COPY . .

WORKDIR /home/intellia/src

ENTRYPOINT ["uvicorn", "optiplant.main:app", "--host", "0.0.0.0", "--port", "5000"]
