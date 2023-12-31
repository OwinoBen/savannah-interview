FROM python:3.9.6-alpine as builder

WORKDIR /savannah_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY . .
# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /savannah_api/wheels -r requirements.txt

FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/app

#create the app user (non root user)
RUN  addgroup -S app && adduser -S app -G app

#create directories

ENV HOME=/home/app
ENV APP_HOME=/home/app/api
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles
RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

#install dependencies
RUN apk update && apk add libpq #c library for connecting to postgresql
COPY --from=builder /savannah_api/wheels /wheels
COPY --from=builder /savannah_api/requirements.txt .
RUN pip install --no-cache /wheels/*

#copy entrypoint.sh
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

#copy project
COPY . $APP_HOME

#chown all the files to the app user
RUN chown -R app:app $APP_HOME

#change the app user
USER app

EXPOSE 8000
#run entrypoint.prod.sh
ENTRYPOINT ["/home/app/api/entrypoint.prod.sh"]
