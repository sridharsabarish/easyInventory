# Use an official lightweight Python image
FROM python:3.12-alpine  

# Set the working directory
WORKDIR /app  

# Copy project files into the container
COPY . /app  


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000  

# Command to run the app
CMD ["python", "app.py"]