

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.dates as mdates

# Conecta ao banco de dados
conn = sqlite3.connect("Chinook_Sqlite.sqlite")

#Retorna o caminho do arquivo da pasta do projeto
BASE_DIR = Path(__file__).resolve().parent

# # Receita mensal
# receita_mensal = (BASE_DIR /"Queries"/"receita_mensal.sql").read_text(encoding="utf-8")

# #Quantidade de pedido
# qtd_pedido = (BASE_DIR/"Queries"/"quantidade_pedidos.sql").read_text(encoding="utf-8")

# #ticket medio
# ticket_medio = (BASE_DIR/"Queries"/"ticket_medio.sql").read_text(encoding="utf-8")

#Consulta unificada - Evolução do faturamento mensal Básico
faturamento_mensal_basico = (BASE_DIR/"Queries"/"all_01.sql").read_text(encoding="utf8")

# df_receita_mensal = pd.read_sql_query(receita_mensal, conn)
# df_qtd_pedido = pd.read_sql_query(qtd_pedido, conn)
# df_ticket_medio = pd.read_sql_query(ticket_medio,conn)
df_faturamento_mensal = pd.read_sql_query(faturamento_mensal_basico,conn)

conn.close()

# print(df_receita_mensal)
# print(df_qtd_pedido)
# print(df_ticket_medio)
print(df_faturamento_mensal)

df_faturamento_mensal["mes_ano"] = pd.to_datetime(
    df_faturamento_mensal["mes_ano"],
    format="%Y-%m"
)
fig, ax = plt.subplots(2,1)

ax[0].plot(df_faturamento_mensal["mes_ano"], df_faturamento_mensal["Total_pedido"])
ax[0].plot(
    df_faturamento_mensal["mes_ano"],
    df_faturamento_mensal["Total_pedido"],
    color="red",
    label="Total_pedido",
    linewidth=2

)

#ax.plot(df_faturamento_mensal["mes_ano"], df_faturamento_mensal["qtd_pedido"])
ax[0].plot(df_faturamento_mensal["mes_ano"], df_faturamento_mensal["ticket_medio"])
ax[0].plot(
    df_faturamento_mensal["mes_ano"],
    df_faturamento_mensal["ticket_medio"],
    color="blue",
    label="ticket_medio",
    linewidth=2
)
ax[0].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

ax[0].set_xlabel("data")
ax[0].set_ylabel("valores")
ax[0].legend()

#####
ax[1].plot(df_faturamento_mensal["mes_ano"], df_faturamento_mensal["qtd_pedido"])
ax[1].plot(
    df_faturamento_mensal["mes_ano"],
    df_faturamento_mensal["qtd_pedido"],
    color="red",
    label="quantidade_pedido",
    linewidth=2,
)
ax[1].set_ylim(0,max(df_faturamento_mensal["qtd_pedido"])+1)
ax[1].set_xlabel("data")
ax[1].set_ylabel("valores")
ax[1].legend()

plt.show()


# top10 = df_musicas.plot(x="Name", y="coun", kind="bar", title="Top 10 musicas", legend= False)

# top10.bar_label(
#     top10.containers[0],
#     fmt="%.2f",
#     padding=3
# )

# pais, Total = df_pais.loc[0,["pais", "Total"]]

# fig, ax = plt.subplots(figsize=(5, 2))

# ax.text(
#     0.5, 0.7,
#     f"País com maior faturamento: {pais}",
#     ha="center",
#     fontsize=13,
#     transform=ax.transAxes
# )

# ax.text(
#     0.5, 0.35,
#     f"${Total:.2f}",
#     ha="center",
#     fontsize=26,
#     fontweight="bold",
#     transform=ax.transAxes
# )
# ###########33
# # ax[1].text(
# #     0.7, 1,
# #     f"País com maior faturamento: {pais}",
# #     ha="center",
# #     color="red",
# #     fontsize=15,
# #     transform=ax[1].transAxes
# # )

# # ax[1].text(
# #     0.5, 0.35,
# #     f"${Total:.3f}",
# #     ha="center",
# #     fontsize=26,
# #     fontweight="bold",
# #     transform=ax[1].transAxes
# # )
# # ax[1].axis("off")
# ax.axis("off")


# top_vendedor = df_vendedor.plot(y="Total", kind="pie", title="Top Vendedor", labels=df_vendedor["FirstName"], legend=False)

# legendas = [
#     f"{nome}: €{valor: .2f}"
#     for nome, valor in zip(df_vendedor["FirstName"],df_vendedor["Total"])
# ]
# top_vendedor.legend(
#     legendas,
#     loc="upper right",
#     bbox_to_anchor=(1.5, 1)

# )

# plt.show()