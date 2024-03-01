FROM python:3.9
RUN mkdir -p /microservices_boba && chown -R root:root /microservices_boba
WORKDIR /microservices_boba
ENV FLASK_APP=service/app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]




