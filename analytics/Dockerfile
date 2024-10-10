FROM public.ecr.aws/docker/library/python:3.10-slim

WORKDIR /src/app

COPY . /src/app

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py" ]