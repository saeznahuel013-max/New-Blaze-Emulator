FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt || echo "No requirements"
EXPOSE 42124
CMD ["python", "serverfifa.py"]
