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

# --- Interface e Filtros ---
try:
    st.sidebar.header("Filtros")
    
    # Filtro de Bairro
    bairros = df['bairro'].unique()
    bairro_selecionado = st.sidebar.multiselect(
        "Filtrar por Bairro", options=bairros, default=bairros
    )
    
    # Filtro de Tipo
    tipos = df['tipo_ocorrencia'].unique()
    tipo_selecionado = st.sidebar.multiselect(
        "Tipo de Ocorrência", options=tipos, default=tipos
    )

    # Aplicação dos filtros
    df_filtrado = df[
        (df['bairro'].isin(bairro_selecionado)) & 
        (df['tipo_ocorrencia'].isin(tipo_selecionado))
    ]

    if df_filtrado.empty:
        st.warning("⚠️ Nenhum dado encontrado com esses filtros.")
        st.stop()

    # --- Visualizações ---
    col1, col2 = st.columns(2)

    # Gráfico 1: Temporal
    with col1:
        st.subheader("Horários Críticos")
        fig_hist = px.histogram(df_filtrado, x="hora", nbins=24, title="Crimes por Hora")
        st.plotly_chart(fig_hist, use_container_width=True)

    # Gráfico 2: Mapa
    with col2:
        st.subheader("Mapa de Calor")
        fig_map = px.density_mapbox(
            df_filtrado, 
            lat='latitude', 
            lon='longitude', 
            radius=15,
            center=dict(lat=-5.08, lon=-42.80), 
            zoom=11,
            mapbox_style="open-street-map"
        )
        st.plotly_chart(fig_map, use_container_width=True)

    # Tabela
    st.divider()
    st.dataframe(df_filtrado.head(50))

except Exception as e:
    st.error(f"❌ Erro na visualização: {e}")