import pandas as pd
import base64
import io


def baixar_sugestoes(sugestoes):
    """Baixa as sugestões em um arquivo Excel."""
    # Cria um DataFrame com as sugestões
    df_sugestoes = pd.DataFrame(sugestoes, columns=["Sugestão"])

    # Gera o arquivo Excel com o DataFrame
    excel_file = io.BytesIO()
    df_sugestoes.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Codifica o arquivo em base64
    b64 = base64.b64encode(excel_file.read()).decode()

    # Força o download do arquivo
    st.markdown(
        "Clique no botão abaixo para fazer o download do arquivo Excel com as sugestões")
    st.markdown(
        f'<a href="data:application/octet-stream;base64,{b64}" download="sugestoes.xlsx">Baixar</a>', unsafe_allow_html=True)
