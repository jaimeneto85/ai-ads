FROM python:3.12

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev

RUN pip install pipenv && \
  python -m pipenv --version


WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install

RUN pip install streamlit

RUN pip install openai

RUN pip install python-dotenv

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py"]