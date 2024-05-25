FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and the script to the container
COPY requirements.txt .
COPY bot.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "bot.py"]
