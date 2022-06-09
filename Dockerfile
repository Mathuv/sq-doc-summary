FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install required python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Download the required NLTK data
RUN [ "python", "-c", "import nltk; nltk.download('stopwords')" ]
RUN [ "python", "-c", "import nltk; nltk.download('punkt')" ]

COPY ./app /code/app

EXPOSE 8080
