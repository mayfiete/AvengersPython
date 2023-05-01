# Dockerfile: blueprint for building images
# Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image
# Docker image is a read-only template with instructions for creating a Docker container
# Docker container is a runtime instance of an image

FROM python:3.9 

ADD app/ .

RUN app/requirements.txt .

# need to create a script to create a hero_names.txt file
RUN echo "Wolverine" > hero_names.txt


CMD [ "python", "script_runner.py"]

# docker build -t avengerspython .
# docker run avengerspython
