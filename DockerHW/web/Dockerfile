FROM python:3.11-slim

WORKDIR /app

# copy all current folder's files to workdir /app
COPY . .

RUN pip install -r requirements.txt

# listening to port 5000 (need to specify local port while building)
EXPOSE 5000

CMD [ "python" , "main.py" ]