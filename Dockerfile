# Use the official Python image
FROM --platform=linux/x86-64 python:3.11-slim

# Set the working directory
WORKDIR /app

# Install Flask
RUN pip install Flask flask-cors

# Copy the application code
COPY app.py /app/

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
