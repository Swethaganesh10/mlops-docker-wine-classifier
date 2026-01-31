# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the model training script into the container
COPY src/ .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD ["python", "main.py"]