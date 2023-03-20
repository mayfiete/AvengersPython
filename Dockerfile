# Dockerfile: blueprint for building images
# Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image
# Docker image is a read-only template with instructions for creating a Docker container
# Docker container is a runtime instance of an image

FROM python:3.9

ADD fetch_heroes.py .
ADD DbConnx.py .
ADD format_json.py . 
ADD MarvelClass.py . 
ADD persist.py . 
ADD pivot_db_data.py . 

RUN pip install requests datetime pandas 

CMD [ "python", "./fetch_heroes.py","./format_json.py", "./persist.py", "./pivot_db_data.py" ]

# docker build -t avengerspython .
# docker run avengerspython
