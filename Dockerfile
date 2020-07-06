FROM python:3.8-alpine
RUN apk add --no-cache gcc
RUN apk add build-base
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "gunicorn" ]
CMD [ "-b :5000", "application:app" ]
