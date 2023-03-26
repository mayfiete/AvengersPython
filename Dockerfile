# Dockerfile: blueprint for building images
# Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image
# Docker image is a read-only template with instructions for creating a Docker container
# Docker container is a runtime instance of an image

FROM python:3.9 

ADD app/ .

RUN pip install requests datetime pandas 

CMD [ "python", "./app/fetch_heroes.py", "./app/format_json.py", "./app/persist.py", "./app/pivot_db_data.py", "./app/write_to_mongodb.py"]

# docker build -t avengerspython .
# docker run avengerspython
