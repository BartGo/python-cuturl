FROM python:3.8-alpine
ENV OSTYPE alpine

COPY . /deploy
WORKDIR /deploy

RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev alpine-sdk
RUN apk del .build-deps

RUN chmod +x /deploy/devinit.sh
RUN cd /deploy
RUN source devinit.sh

CMD ["python", "manage.py", "runserver"]
