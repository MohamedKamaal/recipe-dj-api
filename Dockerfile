FROM python:3.12.6-alpine


# Set environment variable for buffered output
ENV PYTHONUNBUFFERED=1

#copy requirements.txt from host into image
COPY ./requirements.txt /requirements.txt

#install dependencies in image 
RUN pip install -r /requirements.txt


#make and set working directoy to /app in image 
RUN mkdir /app
WORKDIR /app
#copy from app directory into app in image 
COPY ./app /app

# Create a non-root user
RUN adduser -D user 
# switch to user 
USER user 


