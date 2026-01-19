import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configurações iniciais
np.random.seed(42)
n_ocorrencias = 500

# Dados base de Teresina
bairros_locais = {
    'Ilhotas': {'lat': -5.092, 'lon': -42.810},
    'Ininga': {'lat': -5.071, 'lon': -42.793},
    'Primavera': {'lat': -5.065, 'lon': -42.815}, # Perto da ponte
    'Centro': {'lat': -5.090, 'lon': -42.812},
    'Dirceu': {'lat': -5.110, 'lon': -42.760},
    'Jockey': {'lat': -5.080, 'lon': -42.780}
}

tipos = ['Roubo a Transeunte', 'Roubo de Veículo', 'Furto', 'Lesão Corporal', 'Tráfico']
desfechos = ['B.O. Registrado', 'Suspeito Preso', 'Investigação em Curso', 'Arquivado']

dados = []

# Gerando dados
for _ in range(n_ocorrencias):
    # Escolha aleatória ponderada (Simulando)
    bairro_nome = random.choice(list(bairros_locais.keys()))
    coords = bairros_locais[bairro_nome]
    
    # Variação pequena na lat/lon para não ficarem todos pontos um em cima do outro
    lat = coords['lat'] + np.random.normal(0, 0.002)
    lon = coords['lon'] + np.random.normal(0, 0.002)
    
    # Data aleatória nos últimos 30 dias
    dias_atras = random.randint(0, 30)
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    
    tipo_crime = random.choice(tipos)
    
    # --- SIMULAÇÃO DO CENÁRIO ESPECÍFICO (O Caso da Marechal) ---
    # Se for bairro Primavera ou Ilhotas (região da Marechal)
    if bairro_nome in ['Primavera', 'Ilhotas']:
        chance = random.random()
        # 40% de chance de alterar a hora para "cedo da manhã" (5h as 7h)
        if chance < 0.4:
            hora = random.randint(5, 7)
            tipo_crime = 'Roubo a Transeunte' # Pessoas caminhando
            # Ajustar coordenada para ficar bem perto da Avenida/Rio
            lat = -5.068 + np.random.normal(0, 0.001) 
    
    data_hora = datetime.now() - timedelta(days=dias_atras)
    data_hora = data_hora.replace(hour=hora, minute=minuto)
    
    dados.append({
        'data_hora': data_hora,
        'bairro': bairro_nome,
        'tipo_ocorrencia': tipo_crime,
        'latitude': lat,
        'longitude': lon,
        'desfecho': random.choice(desfechos)
    })

df = pd.DataFrame(dados)

# Salvar
df.to_csv('ocorrencias_teresina.csv', index=False)
print("Dados gerados com sucesso: ocorrencias_teresina.csv")