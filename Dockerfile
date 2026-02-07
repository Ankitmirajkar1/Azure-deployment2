# Use a more complete Python base to avoid needing apt-get
FROM python:3.11


# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application - copy the files from local to the container
COPY . .

# Streamlit port
EXPOSE 8501

# Run the app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
