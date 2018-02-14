# Use an official Python runtime as a parent image
FROM python:3
LABEL maintainer="Naresh Mehta"

# Set the working directory to /app
WORKDIR /app

# I will just add the python code and requirements.text
# as I don't need anything else
ADD knn.py /app
ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# No port expose is needed for this docker image
# hence EXPOSE is overridden

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV NAME KNN_Regression

# Run knn.py when the container launches
CMD ["python", "knn.py"]
