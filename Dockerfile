FROM python

WORKDIR /app
COPY . .

RUN pip install --upgrade pip setuptools
RUN python3 /app/setup.py install
