import pandas as pd
import streamlit as st

data = pd.read_json("Tabela_CEST.json")
mercosul = pd.read_json("Tabela_NCM_20221009.json")

produtos = []
produtos_mercosul = []

anexo = ["4016.10.10","8483.20.00","4016.99.90","8483.30","68.13","8483.40","7007.11.00","8483.50","7007.21.00","8505.20","7009.10.00","8507.10.00","7320.10.00","85.11","8301.20.00","8512.20","8302.30.00","8512.30.00","8407.33.90","8512.40","8407.34.90","8512.90.00","8408.20","8527.2",
"8409.91","8536.50.90 ","8536.50.90 ","8409.99","8539.10","8413.30","8544.30.00","8413.91.00","8706.00","8414.80.21","87.07","8414.80.22","87.08","8415.20","9029.20.10","8421.23.00","9029.90.10","8421.31.00","9030.39.21","8431.41.00","9031.80.40","8431.42.00","9032.89.2","8433.90.90","9104.00.00","8481.80.99",
"9401.20.00","8483.10"]


st.title("CEST com código NCM")
prefixo = st.text_input("Prefixo", value="", max_chars=4)

for item in data["items"]:
    if (prefixo == item["nCM"].split(".")[0]):
        produtos.append([item["cEST"], item["nCM"], item["descricao"]])

cest_table = pd.DataFrame(produtos, columns=["CEST", "Código NCM", "Descrição"])
st.table(cest_table)

st.title("Consultas à Nomenclatura Comum do MERCOSUL")
for item in mercosul["Nomenclaturas"]:
    if (prefixo == item["Codigo"].split(".")[0] and item["Codigo"] in anexo):
        produtos_mercosul.append([item["Codigo"], item["Descricao"]])

ncm = pd.DataFrame(produtos_mercosul, columns=["Código", "Descrição"])
st.table(ncm)
