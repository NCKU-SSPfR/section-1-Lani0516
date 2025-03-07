# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# it will automatically
# expose to port 8000 in the container
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]