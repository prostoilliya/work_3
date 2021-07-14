FROM python:3.8

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_ENV=development

CMD ["gunicorn", "app:ap p", "-b", "0.0.0.0:8000"]