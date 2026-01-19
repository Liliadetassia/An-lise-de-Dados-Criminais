# 🔵 SSP-PI Intelligence: Análise de Dados Criminais em Teresina

Este projeto foi desenvolvido como resposta ao **Desafio de Análise de Dados** para a Secretaria de Segurança Pública. O objetivo é demonstrar como a Ciência de Dados pode apoiar a tomada de decisão operacional e a alocação eficiente de viaturas policiais em Teresina.

## 🎯 O Problema de Negócio

A cidade de Teresina apresenta dinâmicas criminais distintas dependendo da zona (Norte, Leste, Centro, etc.) e do horário. O desafio propôs analisar dados de:
* Bairro
* Horário
* Tipo de Ocorrência
* Desfecho

### 🔎 Estudo de Caso: A Av. Marechal Castelo Branco
Para validar o modelo, foquei em um problema real e recente da capital: **assaltos a mulheres que praticam caminhada cedo da manhã (05h-07h) na região da Ponte da Primavera.**

Enquanto a maioria das análises genéricas foca apenas na criminalidade noturna, este dashboard foi capaz de identificar **outliers (picos atípicos)** no início da manhã nessa região específica, provando a necessidade de policiamento dinâmico baseado em dados.

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* **Pandas:** Para limpeza, tratamento e estruturação do dataset.
* **Streamlit:** Para criação do dashboard interativo em tempo real.
* **Plotly Express:** Para visualização de mapas de calor e histogramas interativos.
* **Numpy:** Para simulação probabilística de cenários baseados na realidade local.

## 📊 Funcionalidades do Dashboard

1.  **Mapa de Calor (Heatmap):** Identificação visual imediata das "Zonas Quentes" de criminalidade.
2.  **Análise Temporal:** Histograma que revela os horários de pico de ocorrências por bairro.
3.  **Filtros Dinâmicos:** Permite ao gestor filtrar por Bairro (ex: Primavera, Ilhotas) e Tipo de Crime (ex: Roubo a Transeunte).
4.  **KPIs Operacionais:** Indicadores rápidos de horário crítico e bairro mais afetado.

## 🚀 Como Executar o Projeto

Pré-requisitos: Python instalado.

<img width="1332" height="563" alt="rr" src="https://github.com/user-attachments/assets/e759da99-7bbe-4662-9fb9-dab462c50482" />


1. **Instale as dependências:**
   ```bash
   pip install pandas streamlit plotly numpy
