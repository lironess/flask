FROM python:3.10.0-alpine
WORKDIR /code
ENV FLASK_APP=app/app.py

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python", "-m",  "flask", "run", "--host=0.0.0.0"]