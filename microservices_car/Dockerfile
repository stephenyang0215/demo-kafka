FROM python:3.9
RUN mkdir -p /microservices_car && chown -R root:root /microservices_car
WORKDIR /microservices_car
ENV FLASK_APP=service/app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]




