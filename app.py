import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Configuração da Página ---
st.set_page_config(page_title="SSP-PI Debug", layout="wide")

st.title("🛠️ Análise SSP-PI")

# --- Verificação de Arquivo ---
arquivo = 'ocorrencias_teresina.csv'

if not os.path.exists(arquivo):
    st.error(f"❌ O arquivo '{arquivo}' não foi encontrado na pasta!")
    st.warning("👉 Execute o comando: python gerar_dados.py")
    st.stop()

# --- Carregamento de Dados com Tratamento de Erro ---
try:
    df = pd.read_csv(arquivo)
    
    # Verifica se o arquivo está vazio
    if df.empty:
        st.error("❌ O arquivo CSV existe, mas está vazio.")
        st.stop()

    # Conversão de datas
    df['data_hora'] = pd.to_datetime(df['data_hora'])
    df['hora'] = df['data_hora'].dt.hour
    
    # Tradução de dias
    df['dia_semana'] = df['data_hora'].dt.day_name()
    dias_traducao = {
        'Monday': 'Segunda', 'Tuesday': 'Terça', 'Wednesday': 'Quarta',
        'Thursday': 'Quinta', 'Friday': 'Sexta', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
    }
    df['dia_semana'] = df['dia_semana'].map(dias_traducao)

    st.success(f"✅ Dados carregados com sucesso! {len(df)} ocorrências encontradas.")

except Exception as e:
    st.error(f"❌ Erro crítico ao processar os dados: {e}")
    st.stop()

