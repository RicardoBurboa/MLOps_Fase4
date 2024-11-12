FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the model and server code
COPY absenteeism_model.pkl /app/
COPY main.py /app/
COPY Absenteeism_at_work.csv /app/

# Install dependencies
RUN pip install fastapi uvicorn scikit-learn pydantic pandas

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]