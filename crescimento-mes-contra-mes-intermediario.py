
import sqlite3
from matplotlib import ticker
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.dates as mdates

# Conecta ao banco de dados
conn = sqlite3.connect("Chinook_Sqlite.sqlite")

#Retorna o caminho do arquivo da pasta do projeto
BASE_DIR = Path(__file__).resolve().parent
#variavel que salva o caminho da consulta
crescimento_mes_to_mes = (BASE_DIR/"Queries"/"crescimento_mes_to_mes.sql").read_text(encoding="utf8")

#carregando dataframe
df_crescimento_mes_to_mes = pd.read_sql_query(crescimento_mes_to_mes,conn)

conn.close()

print(df_crescimento_mes_to_mes)

# Converter datas
df_crescimento_mes_to_mes["mes_ano"] = pd.to_datetime(
    df_crescimento_mes_to_mes["mes_ano"],
    format="%Y-%m"
)

# configura para criar 3 linhas e uma coluna, e em cada linha tem um grafico
fig, ax = plt.subplots(3,1, figsize=(16,14), sharex=True, gridspec_kw={"height_ratios":[1,1,2]})

# Plota na figura 0 no eixo x a data e no primeiro eixo y a receita mensal 
# aqui mostrando receita mensal por mes no primeiro eixo y no primeiro gráfico 
ax[0].plot(
    df_crescimento_mes_to_mes["mes_ano"],
    df_crescimento_mes_to_mes["receita_mensal"],
    color="red",
    label="receita_mensal",
    linewidth=2

)

# # Plota na figura 0 no eixo x a data e no segundo eixo y a receita do mes anterior
# aqui mostrando receita do mes anterior por mes no segundo eixo y no primeiro gráfico 
ax[0].plot(
    df_crescimento_mes_to_mes["mes_ano"],
    df_crescimento_mes_to_mes["receita_mês_anterior"],
    color="blue",
    label="receita_mês_anterior",
    linewidth=2
)

#comnfigura as formatação da data para semestres
ax[0].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

#configura as labels dos gráficos
#ax[0].set_xlabel("data")
ax[0].set_ylabel("valores")
ax[0].legend()

# plota na figura 1 no eixo x a data e no eixp y a diferença absolula, em valores monetários
ax[1].plot(
    df_crescimento_mes_to_mes["mes_ano"],
    df_crescimento_mes_to_mes["diferenca_absoluta"],
    color="blue",
    label="diferenca_absoluta",
    marker='o', #coloca uma boloinha em cada ponto
    linewidth=2
)
#comnfigura as formatação da data para semestres
ax[1].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

#configura as labels dos gráficos
ax[1].set_ylabel("valores - R$")
ax[1].legend()

# loop for para passar por cada valor, usando enumerate para pegar posição e valor da serie
for i, txt in enumerate(df_crescimento_mes_to_mes["diferenca_absoluta"]):

    if pd.notna(txt) and abs(txt) >= 2: #pd.notna verifica se aquela linha tem valor, caso seja nulo ele não entra. Isso é usaso pois como está sendo usado a diferença do mes anterior, a primeira linha é nula

        deslocamento = 12 if txt >= 0 else -15 #para ajustar a posição do rotulo

        ax[1].annotate(
            f"{txt:.2f}%",
            (
                df_crescimento_mes_to_mes["mes_ano"].iloc[i],
                txt
            ),
            textcoords="offset points",
            xytext=(0, deslocamento),
            ha="center",
            va="bottom" if txt >= 0 else "top",
            fontsize=8
        )


ax[2].plot(
    df_crescimento_mes_to_mes["mes_ano"],
    df_crescimento_mes_to_mes["diferenca_relativa"],
    color="blue",
    label="diferenca_relativa",
    linewidth=2,
    marker='o',
    linestyle='-'
)

#comnfigura as formatação da data para semestres
ax[2].xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

ax[2].yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100))

for i, txt in enumerate(df_crescimento_mes_to_mes["diferenca_relativa"]):

    if pd.notna(txt) and abs(txt) >= 2:

        deslocamento = 12 if txt >= 0 else -15

        ax[2].annotate(
            f"{txt:.2f}%",
            (
                df_crescimento_mes_to_mes["mes_ano"].iloc[i],
                txt
            ),
            textcoords="offset points",
            xytext=(0, deslocamento),
            ha="center",
            va="bottom" if txt >= 0 else "top",
            fontsize=8
        )

ax[2].set_ylim(-40, int(df_crescimento_mes_to_mes["diferenca_relativa"].max()*1.1))  # Ajusta o limite do Y para o texto não cortar
ax[2].set_title('')
ax[2].set_title('Crescimento Mensal')
ax[2].set_ylabel('Percentual (%)')

ax[0].set_title("Comparação mês anterior", pad=20)
ax[1].set_title("Evolução em R$", pad=20)
ax[2].set_title("Evolução em Percentual", pad=20)
fig.subplots_adjust(hspace=0.45)

plt.show()
