#official Python 3.10 image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# add app.py and models directory
COPY app.py .
COPY models/ ./models/

# add requirements.txt
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# specify default commands
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]