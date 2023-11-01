# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application's source code into the container at /app/
COPY . /app/

# Expose a port for your application to listen on (if needed)
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn", "Ecommerce.wsgi:application", "--bind", "0.0.0.0:8000"]
