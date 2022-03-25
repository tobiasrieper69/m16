FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/env

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH = "$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python3", "-m" ,"flask" ,"run", "--host=0.0.0.0"]


