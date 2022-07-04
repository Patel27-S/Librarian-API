# We'll need and hence use the below base_image 
# to built our own image, from Docker Hub.
FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# The working directory inside of the container.
WORKDIR /code

# Copying requirements.txt from the same directory as
# the dockerfile to the working directory of the container.
COPY ./requirements.txt /code/

# Below command will run inside of the container and will 
# ensure that all the dependencies required for running this app
# will be installed inside the application of this container.
RUN pip install -r requirements.txt


# Eventually, copying all the code from the directory 
# same as that of the Dockerfile to the /code folder inside 
# the container.
COPY . /code