# import pyrebase
import csv
import io

import streamlit as st
import pandas as pd
from sugestoes import gerar_sugestoes
from download import baixar_sugestoes
from analise_performance import analise_dataframe

config = {
    "apiKey": 'AIzaSyCYwE6WewCwdHYjzwyW4jEAM75Cf0XtQ2g',
    "authDomain": "262247381339.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "262247381339.appspot.com",
    "type": "service_account",
    "project_id": "ablab-ci-leadads",
    "private_key_id": "006e384834584b426e1c408d6f7799d2227b3db8",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuMx7GzeZFXv4M\nKCDVUxkm8eTyTy0PJ5GCV9zHKSjnnrLxeHsD4w46JsuZrZfFz9sncoSEMWjibXQl\nRAaM9S2HpzcWJtSkU+zsjafPnv1hxFvPjrUldZO57IQKUhKkR1148EYocsgrqj16\n+GPLeRrhkXLmlALrq6n1Z7KqI7lywNdoSF2VnmQpDPGnHh2mLZEpgO+e/Oso57EB\nO0C38WBBPyi8hMZ4JfdjKPU66ZETmfJZN+xbzKpJrAq1x1WlxYVH758MdTJg6DhC\ng5ZbWhwOoOAUJG3SZkjSkdWsGIGugPfze8jY1XHj9LNFyMdO+Ty4g1+H/GL1AAzr\nKBeUIA4ZAgMBAAECggEAA5/5MzpcIRPrte2M11uSEaslcDxhC+hvIPb6l2NeIEm/\nYAJ5jthl9qRRhspjtuBPJ2g85TJRBCsyaEcc2siMUL8USJ/4u02qx7Zf6FRe4e6v\n2WcXEmc6snr/OWbBUA1THt3jG9rdmvkBLAKosvZ7bne0HCO21tgc4ogsodk59e8Q\nCZyMWmotVMbn9f829tdQItSQvH0FJtOFUQaJxLdHGHtckmEa1OyMZ2iuH8blZ9EX\nOb8Kjae/PEtJDIEfeR2C1a7Dtfc80QMS/KaJf/TKadSJOIrYsGf5ESHWJHyf+mkW\nNK5zZiGNcYRoYvBfGuPOrHpQtlbtRFxmNDA38s6gjQKBgQDm0bIHYNnwaKaQg1mL\nrbHeQ2ypTzLCe9/hipqvOB9OeB7iBecSQjcCK3lyInuIuSetV1xUPD07wIxY+7/2\nY1FSUldrGVxF3s7+8RvyojoMKkZQdu9Iq1fAE2kQG+ZILMStxhnLiGTpzjkS3Bzt\nSYzDBMqYghqRH+68iT9qTCZsvQKBgQDBNCj/cMjRPlxiwObJ/nAokiGvGFFiGXO4\npaF/qlR5i3gGL+U7UKikmcyaJVTkIXmJIehNg/rTqSw0+xZw0DsMZNh4JEoBiFxV\nSuyP95Sow+9dVoTtunqGGVQtQ3abfR/OI6+YfpSPNH/nThNGnR23RFA63Nb1fddw\nFx4ymlJyjQKBgQC2EWx7k3L1xqa0UVed7SnjZ43b02P3sty7PKidVAilzeyWXw+R\nAHgBlydZ10dYZqycd8+VhlrKuiw6uIIIKPlplRftm/iECKeAw9FGx55AIEyMhfRj\nfvxdvzHdihRQlDej1yJbwL/RCWFNtiB/L8f/wNTKDb5FAUpAn4ZNI7ofhQKBgFYt\n3w+6DkmPiIQgSZHWZc8jB9VjgoHAmqbFctlQb+fbd0lDOfwQSXlKhUJI3qn36I9r\nyYQyF8MsFeT4DxV5PK2Vmh1VCpHOcmk1R3ocVHpHE9FNk3O7F4YTbEHYcuJ+mJ5J\nurzJ0ZhjMZ5KbDy2PpgN57+p3FSasmt0VGr7/UTNAoGAQ/RKkBkRwLvAPwhIGLTC\n666vzyVE7bTbF+wcoEf7dFonr2qM2KwtQ/Zli3GXwzk8/U1gDNt1bpdPUsYAr8lT\nlUM2o35f9crchP91G7mqFqXatXinvwtR7oXYYTIYYvinHzTnGkBwm+klbvoslArj\ngVSo4vZF/sv2tFaK3C0+dws=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-zpu5r@ablab-ci-leadads.iam.gserviceaccount.com",
    "client_id": "106125408166322459650",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zpu5r%40ablab-ci-leadads.iam.gserviceaccount.com"
}

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# cred = credentials.Certificate("./auth/credentials.json")
# if not firebase_admin._apps:
#     firebase_app = firebase_admin.initialize_app(cred)
# firebase_admin.initialize_app(credential="./auth/credentials.json")

# Solicita o usuário e a senha do usuário
with st.form(key='login', clear_on_submit=True):
    login_input = st.sidebar.text_input("Usuário")
    password_input = st.sidebar.text_input("Senha", type="password")
    submit_button = st.sidebar.button("Login")

st.title("AI Ads")
st.text('Sua Inteligência Artificial para sugestão de conteúdo de alta performance!')


# def check_credentials(login, password):
#     try:
#         user = auth.sign_in_with_email_and_password(login, password)
#         return True
#     except Exception as e:
#         print('aqui', e)
#         return False


# Permite que o usuário selecione o arquivo CSV
st.subheader(
    'Acesse as variações de um anúncio e faça o download do arquivo em CSV e envie por aqui o resultado para receber sugestões de performance')
uploaded_file = st.file_uploader(
    "Selecione o arquivo CSV do Google Ads", type="csv")

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")

    corrected_content = io.StringIO()

    # Cria um leitor CSV para ler o conteúdo da string
    reader = csv.reader(io.StringIO(file_content))

    for linha in reader:
        if len(linha) < 3:
            # remove a linha incorreta
            continue
        corrected_content.write(",".join(linha) + "\n")

    # Reposiciona o ponteiro do buffer de string para o início
    corrected_content.seek(0)
    # Lê o arquivo CSV usando o pandas
    df = pd.read_csv(corrected_content,  error_bad_lines=False)
    # criar um novo arquivo para análisar o conteúdo e atribuir notas
    analise_dataframe(df)
    # Filtra os anúncios com nota acima de 7
    df = df[df['nota'] > 7]

    st.write('Melhores Recursos: ')
    st.dataframe(df)

    # Gera as sugestões
    sugestoes = gerar_sugestoes(df)

    # Exibe as sugestões em uma tabela
    st.dataframe(sugestoes)

    # Cria um botão de download
    st.button("Processar novamente!")
    # Baixa as sugestões
    baixar_sugestoes(sugestoes)
