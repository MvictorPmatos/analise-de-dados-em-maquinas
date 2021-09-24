
# Bibliotecas
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates
import numpy as np

df = pd.read_csv('/content/equipe_4 (2).csv') # Leitura do database
#display(df) # Amostra do dataframe
#print(df.info()) # Print das informações do dataframe

df = df.drop(['volt', 'Unnamed: 0', 'idade_maquina', 'modelo', 'ID_maquina'], axis = 1) # Apagando colunas consideradas irrelevantes para a análise
df['Tempo'] = pd.to_datetime(df['Tempo'], errors = 'coerce') # Conversão da coluna tempo para tipo datetime
#display(df) # Amostra do dataframe
#print(df.info()) # Print das informações do dataframe

# Derros é o dataframe apenas com os erros e falhas
Derros = df.drop(['rotacao', 'pressao', 'vibracao'], axis = 1)
Derros = Derros.drop_duplicates()
Derros['tipo_erro'] = Derros['tipo_erro'].astype(str)
Derros['falha'] = Derros['falha'].astype(str)
#display(Derros)

# Criando gráficos de Erros x Tempo e Falhas x Tempo
fig = make_subplots(rows=2, cols=1, subplot_titles = ("Erros x Tempo", "Falhas x Tempo"))
fig.add_trace(go.Scatter(x = Derros['Tempo'], y=Derros['tipo_erro'], mode = 'markers', showlegend=True, name = 'Erros'), row=1, col=1)
fig.add_trace(go.Scatter(x = Derros['Tempo'], y=Derros['falha'], mode = 'markers', showlegend=True, name = 'Falhas'), row=2, col=1)
fig.update_layout(plot_bgcolor = 'white', colorway=["DarkSlateBlue", "Salmon"])
fig.update_xaxes( title_text = "Tempo", row = 1, col = 1, showgrid=True, gridwidth=1, gridcolor='lightgray',showline=True, linewidth=1, linecolor='darkgrey')
fig.update_xaxes( title_text = "Tempo", row = 2, col = 1, showgrid=True, gridwidth=1, gridcolor='lightgray',showline=True, linewidth=1, linecolor='darkgrey')
fig.update_yaxes( title_text = "Erros", row = 1, col = 1, showgrid=True, gridwidth=1, gridcolor='lightgray',showline=True, linewidth=1, linecolor='darkgrey')
fig.update_yaxes( title_text = "Falhas em Componentes", row = 2, col = 1, showgrid=True, gridwidth=1, gridcolor='lightgray',showline=True, linewidth=1, linecolor='darkgrey')
fig.show()

# dfComErro é o data frame com as variáveis associadas aos erros e falhas
dfComErro = df
dfComErro = dfComErro.dropna(thresh=5)
filtro = (df['tipo_erro'] != 'error1') & (df['tipo_erro'] != 'error3') & (df['tipo_erro'] != 'error4') & (df['falha'] != 'comp1') & (df['falha'] != 'comp3')
# dfSemErro é o dataframe com as variáveis associadas a casos sem erros ou falhas
dfSemErro = df[filtro]
dfSemErro = dfSemErro.drop(columns=['comp_subst', 'tipo_erro', 'falha'])
dfSemErro = dfSemErro.dropna(axis = 0, how = 'any')
#display(dfComErro)

# R -> Rotação
# P -> Pressão
# V -> Vibração

# MÉDIA DAS VARIÁVEIS
MediaRSemErro = statistics.mean(dfSemErro['rotacao'])
MediaRComErro = statistics.mean(dfComErro['rotacao'])
MediaPSemErro = statistics.mean(dfSemErro['pressao'])
MediaPComErro = statistics.mean(dfComErro['pressao'])
MediaVSemErro = statistics.mean(dfSemErro['vibracao'])
MediaVComErro = statistics.mean(dfComErro['vibracao'])

# MEDIANA DAS VARIÁVEIS
MedianaRSemErro = statistics.median(dfSemErro['rotacao'])
MedianaRComErro = statistics.median(dfComErro['rotacao'])
MedianaPSemErro = statistics.median(dfSemErro['pressao'])
MedianaPComErro = statistics.median(dfComErro['pressao'])
MedianaVSemErro = statistics.median(dfSemErro['vibracao'])
MedianaVComErro = statistics.median(dfComErro['vibracao'])

# DESVIO DAS VARIÁVEIS
DesvioRSemErro = statistics.stdev(dfSemErro['rotacao'])
DesvioRComErro = statistics.stdev(dfComErro['rotacao'])
DesvioPSemErro = statistics.stdev(dfSemErro['pressao'])
DesvioPComErro = statistics.stdev(dfComErro['pressao'])
DesvioVSemErro = statistics.stdev(dfSemErro['vibracao'])
DesvioVComErro = statistics.stdev(dfComErro['vibracao'])

# 1º QUARTIL DAS VARIÁVEIS
Qua1RSemErro = np.percentile(dfSemErro['rotacao'], 25)
Qua1RComErro = np.percentile(dfComErro['rotacao'], 25)
Qua1PSemErro = np.percentile(dfSemErro['pressao'], 25)
Qua1PComErro = np.percentile(dfComErro['pressao'], 25)
Qua1VSemErro = np.percentile(dfSemErro['vibracao'], 25)
Qua1VComErro = np.percentile(dfComErro['vibracao'], 25)

# 3º QUARTIL DAS VARIÁVEIS
Qua3RSemErro = np.percentile(dfSemErro['rotacao'], 75)
Qua3RComErro = np.percentile(dfComErro['rotacao'], 75)
Qua3PSemErro = np.percentile(dfSemErro['pressao'], 75)
Qua3PComErro = np.percentile(dfComErro['pressao'], 75)
Qua3VSemErro = np.percentile(dfSemErro['vibracao'], 75)
Qua3VComErro = np.percentile(dfComErro['vibracao'], 75)

# MÁXIMO DAS VARIÁVEIS
MaxRSemErro = dfSemErro['rotacao'].max()
MaxRComErro = dfComErro['rotacao'].max()
MaxPSemErro = dfSemErro['pressao'].max()
MaxPComErro = dfComErro['pressao'].max()
MaxVSemErro = dfSemErro['vibracao'].max()
MaxVComErro = dfComErro['vibracao'].max()

# MÍNIMO DAS VARIÁVEIS
MinRSemErro = dfSemErro['rotacao'].min()
MinRComErro = dfComErro['rotacao'].min()
MinPSemErro = dfSemErro['pressao'].min()
MinPComErro = dfComErro['pressao'].min()
MinVSemErro = dfSemErro['vibracao'].min()
MinVComErro = dfComErro['vibracao'].min()



# Padrão de cores
headerColor = 'MintCream'
rowEvenColor = 'Cornsilk'
rowOddColor = 'PeachPuff'


# TABELA DA MÉDIA
meanTabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[MediaRSemErro, MediaRComErro],[MediaPSemErro, MediaPComErro ],[ MediaVSemErro, MediaVComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
meanTabel.update_layout(title='Médias das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
meanTabel.show()

# TABELA DA MEDIANA
medianaTabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[MedianaRSemErro, MedianaRComErro],[MedianaPSemErro, MedianaPComErro ],[ MedianaVSemErro, MedianaVComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
medianaTabel.update_layout(title='Medianas das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
medianaTabel.show()

# TABELA DESVIO PADRÃO
desvioTabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[DesvioRSemErro, DesvioRComErro],[DesvioPSemErro, DesvioPComErro ],[DesvioVSemErro, DesvioVComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
desvioTabel.update_layout(title='Desvios das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
desvioTabel.show()

# TABELA 1º QUARTIL
qua1Tabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[Qua1RSemErro, Qua1RComErro],[Qua1PSemErro, Qua1PComErro ],[Qua1VSemErro, Qua1VComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
qua1Tabel.update_layout(title='1º Quartil das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
qua1Tabel.show()

# TABELA 3º QUARTIL
qua3Tabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[Qua3RSemErro, Qua3RComErro],[Qua3PSemErro, Qua3PComErro ],[Qua3VSemErro, Qua3VComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
qua3Tabel.update_layout(title='3º Quartil das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
qua3Tabel.show()

# TABELA MÁXIMO
maxTabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[MaxRSemErro, MaxRComErro],[MaxPSemErro, MaxPComErro ],[MaxVSemErro, MaxVComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
maxTabel.update_layout(title='Máximo das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
maxTabel.show()

# TABELA MÍNIMO
minTabel = go.Figure(data=[go.Table(header=dict(values=['<b>TIPO</b>','<b>ROTAÇÃO</b>','<b>PRESSÃO</b>','<b>VIBRAÇÃO</b>'],line_color='darkslategray',fill_color=headerColor,align=['left','center'],font=dict(color='DarkSlateGray', size=14)),cells=dict(values=[['<b>SEM ERRO<b>', '<b>COM ERRO<b>'],[MinRSemErro, MinRComErro],[MinPSemErro, MinPComErro ],[MinVSemErro, MinVComErro ]],line_color='darkslategray',fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],align = ['left', 'center'],font = dict(color = 'black', size = 12)))])
minTabel.update_layout(title='Mínimo das variáveis para casos com erro e sem erro', font = {'family': 'Arial','size': 14,'color': 'black'}, width=1000, height=300)
minTabel.show()

# Gráfico BoxPlot para Pressão em casos Sem Erro e Com Erro
layout = go.Layout(title = '<b>Pressão Sem e Com Erro</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Pressão</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
pressBox = go.Figure(layout = layout)
pressBox.add_trace(go.Box(y = dfSemErro['pressao'], name = 'Sem Erro'))
pressBox.add_trace(go.Box(y = dfComErro['pressao'], name = 'Com Erro'))

# Gráfico BoxPlot para Rotação em casos Sem Erro e Com Erro
layout = go.Layout(title = '<b>Rotação Sem e Com Erro</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Rotação</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
rotacBox = go.Figure(layout = layout)
rotacBox.add_trace(go.Box(y = dfSemErro['rotacao'], name = 'Sem Erro'))
rotacBox.add_trace(go.Box(y = dfComErro['rotacao'], name = 'Com Erro'))

# Gráfico BoxPlot para Vibração em casos Sem Erro e Com Erro
layout = go.Layout(title = '<b>Vibração Sem e Com Erro</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Vibração</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
vibraBox = go.Figure(layout= layout)
vibraBox.add_trace(go.Box(y = dfSemErro['vibracao'], name = 'Sem Erro'))
vibraBox.add_trace(go.Box(y = dfComErro['vibracao'], name = 'Com Erro'))

# # Gráfico BoxPlot para Pressão, Rotação e Vibração em casos Sem Erro e Com Erro
layout = go.Layout(title = '<b>Pressão, Rotação e Vibração Sem e Com Erro</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Intervalo das medidas</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
geralBox = go.Figure(layout = layout)
geralBox.add_trace(go.Box(x = dfSemErro['pressao'], name = 'Sem Erro'))
geralBox.add_trace(go.Box(x = dfComErro['pressao'], name = 'Com Erro'))
geralBox.add_trace(go.Box(x = dfSemErro['rotacao'], name = 'Sem Erro'))
geralBox.add_trace(go.Box(x = dfComErro['rotacao'], name = 'Com Erro'))
geralBox.add_trace(go.Box(x = dfSemErro['vibracao'], name = 'Sem Erro'))
geralBox.add_trace(go.Box(x = dfComErro['vibracao'], name = 'Com Erro'))

# Dataframe contendo a média das variáveis sem associação com erro por hora
dfMediaSE = dfSemErro
dfMediaSE = dfMediaSE.resample('H', on='Tempo').mean()
dfMediaSE = dfMediaSE.dropna(axis=0,how = 'any')

# Dataframe contendo a média das variáveis com associação a erros por hora
dfMediaCE = dfComErro
dfMediaCE = dfMediaCE.dropna(axis = 1, how = 'any')
dfMediaCE = dfMediaCE.resample('H', on = 'Tempo').mean()

# Gráfico de Série Temporal para Pressão Média x Tempo, com erro e sem erro
layout = go.Layout(title = '<b>Pressão média X Tempo</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tempo</b>'}, yaxis = {'title': '<b>Pressão</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
press = go.Figure(layout = layout)
press.add_trace(go.Scatter(x=dfMediaSE.index, y=dfMediaSE['pressao'], mode = 'lines+markers', name = 'Sem Erro'))
press.add_trace(go.Scatter(x=dfMediaCE.index, y=dfMediaCE['pressao'], mode = 'markers', name  = 'Com Erro'))

# Gráfico de Série Temporal para Rotação Média x Tempo, com erro e sem erro
layout = go.Layout(title = '<b>Rotação Média X Tempo</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Rotação</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
rotac = go.Figure(layout = layout)
rotac.add_trace(go.Scatter(x=dfMediaSE.index, y=dfMediaSE['rotacao'], mode = 'lines+markers', name = 'Sem erro'))
rotac.add_trace(go.Scatter(x=dfMediaCE.index, y=dfMediaCE['rotacao'], mode = 'markers', name = 'Com erro'))

# Gráfico de Série Temporal para Vibração Média x Tempo, com erro e sem erro
layout = go.Layout(title = '<b>Vibração Média X Tempo</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Vibração</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
vibra = go.Figure(layout = layout)
vibra.add_trace(go.Scatter(x=dfMediaSE.index, y=dfMediaSE['vibracao'], mode = 'lines+markers', name = 'Sem erro'))
vibra.add_trace(go.Scatter(x=dfMediaCE.index, y=dfMediaCE['vibracao'], mode = 'markers', name = 'Com erro'))

# Gráfico de Série Temporal para Pressão, Rotação e Vibração Média x Tempo, com erro e sem erro
layout = go.Layout(title = '<b>Pressão, Rotação e Vibração Média X Tempo</b>', titlefont = {'family': 'Arial','size': 22, 'color': '#7f7f7f'},xaxis = {'title': '<b>Tipo</b>'}, yaxis = {'title': '<b>Intervalo das Medidas</b>'}, paper_bgcolor = 'rgb(243, 243, 243)', plot_bgcolor = 'rgb(243, 243, 243)')
PRV = go.Figure(layout = layout)
PRV.add_trace(go.Scatter(x=dfMediaSE.index, y=dfMediaSE['pressao'], mode = 'lines+markers', name = 'Pressao sem Erro'))
PRV.add_trace(go.Scatter(x=dfMediaCE.index, y=dfMediaCE['pressao'], mode = 'markers', name = 'Pressao com Erro'))
PRV.add_trace(go.Scatter(x=dfMediaSE.index, y=dfMediaSE['rotacao'], mode = 'lines+markers', name = 'Rotacao sem Erro'))
PRV.add_trace(go.Scatter(x=dfMediaCE.index, y=dfMediaCE['rotacao'], mode = 'markers', name = 'Rotacao com Erro'))
PRV.add_trace(go.Scatter(x=dfMediaSE.index, y=dfMediaSE['vibracao'], mode = 'lines+markers', name = 'Vibracao sem Erro'))
PRV.add_trace(go.Scatter(x=dfMediaCE.index, y=dfMediaCE['vibracao'], mode = 'markers', name = 'Vibracao com Erro'))
