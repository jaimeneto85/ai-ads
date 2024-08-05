# AI-ADS - by @jaimeflneto

[github - @jaimeneto85](https://github.com/jaimeneto85)
[linkedin - @jaimeflneto](https://linkedin.com/in/jaimeflneto)

## Description

This project is a simple implementation of AI suggestions for ads.
The app check the best results, verify the best values and generate a new csv file with the suggestions.
The app is a Streamlit app, so you can run it locally.
It create suggestion from current ads, set the best values and generate a new csv file with the suggestions.

## How to setup

1. Clone the repository

2. Install the dependencies

3. Run the project

## Install dependencies

### Dependencies

- Python 3.12+

- pipenv

- VS Code

- devContainer

- Docker

- OpenAI API Key

### Auto install

- Execute and build project from devContainer

- Create a .env file with the following variables (see .env.example):

- OPENAI_API_KEY=your_openai_api_key

- ENGINE_NAME=your_engine_name

- Build the project

- Run the project

### Manual install

- `pipenv install`

- `pip install streamlit`

- `streamlit run app.py`

## How to use

- Go to Google Ads - go to campaigns - ads - see details of the ad - export the ad to a csv file

- Go to http://localhost:8501

- Upload the csv file

- The app will generate a new csv file with the suggestions

- You can download the new csv file
