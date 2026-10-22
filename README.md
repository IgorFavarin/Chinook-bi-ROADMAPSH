# RoadmadSH-Chinook-database

Projeto duplicado do projeto base no ```https://github.com/IgorFavarin/RoadmadSH-Chinook-database```.

O intuito deste, é criar um projeto novo, usando a mesma base de dados e desenvolver novas análises e dashboards a fim de aprimorar as habilidades técnicas.

### Trabalho base da roadmap.sh abaixo
Trabalho colaborativo roadmap.sh py, sqllite
URL do projeto 
```https://roadmap.sh/projects/querying-sql-python```



## 📊 Progresso dos Desafios — Chinook BI

Este projeto tem como objetivo desenvolver habilidades em SQL, Python, Pandas e Matplotlib por meio de análises de dados e indicadores de negócio.

### 🚀 Checklist de Desenvolvimento

- [x] **01.** Faturamento mensal
- [ ] **02.** Crescimento mensal (MoM)
- [ ] **03.** Ticket médio por país
- [ ] **04.** Clientes mais valiosos
- [ ] **05.** Segmentação RFM
- [ ] **06.** Taxa de recompra
- [ ] **07.** Receita por gênero musical
- [ ] **08.** Músicas com baixa performance
- [ ] **09.** Curva ABC
- [ ] **10.** Desempenho dos representantes por período
- [ ] **11.** Concentração de receita por cliente
- [ ] **12.** Análise de coorte
- [ ] **13.** Análise de cesta de compras

### 📈 Progresso Geral

**Desafios concluídos:**  de 13

![Progresso](https://geps.dev/progress/0)


## Atividades a serem desenvolvidas

### Módulo 1 — Análise financeira

01. Evolução do faturamento mensal Básico
Solicitação do gestor: precisamos identificar os meses de maior e menor faturamento e avaliar se a receita está crescendo.
Entregáveis: receita mensal, quantidade de pedidos por mês, ticket médio mensal e gráfico de linhas.
SQL: strftime(), SUM(), COUNT(), GROUP BY.

02. Crescimento mês contra mês (MoM) Intermediário
Solicitação do gestor: quanto o faturamento cresceu ou caiu em relação ao mês anterior?
Entregáveis: receita do mês, receita anterior, diferença absoluta e variação percentual. Gráfico de linhas com os percentuais.
SQL: CTE, LAG(), NULLIF() e operações matemáticas.

03. Ticket médio por país Básico
Solicitação do gestor: países que geram mais receita também possuem compras de maior valor?
Entregáveis: faturamento, número de pedidos e ticket médio por país. Gráfico de barras com os dez maiores tickets médios.
SQL: SUM(), COUNT(), GROUP BY, HAVING.

### Módulo 2 — Clientes e comportamento de compra

04. Clientes mais valiosos Básico
Solicitação do CRM: identifique os dez clientes que mais contribuíram para o faturamento.
Entregáveis: nome, país, número de pedidos, valor total gasto e ticket médio. Gráfico de barras horizontais.
SQL: JOIN, SUM(), COUNT(), GROUP BY.

05. Segmentação RFM Avançado
Solicitação do marketing: precisamos identificar clientes recorrentes, de alto valor e clientes que não compram há muito tempo.
Calcule:
- Recency: tempo desde a última compra.
- Frequency: número de compras.
- Monetary: valor total gasto.
Entregáveis: classificação de clientes e gráfico de dispersão ou barras por segmento.
SQL: CTE, datas, MAX(), COUNT(), SUM() e CASE.

06. Taxa de recompra Intermediário
Solicitação do marketing: qual percentual dos clientes realizou mais de uma compra?
Entregáveis: quantidade de clientes com uma compra, clientes com duas ou mais compras e taxa de recompra. Indicador KPI e gráfico de barras.
SQL: subconsultas ou CTE, COUNT() e HAVING.

### Módulo 3 — Produtos, músicas e catálogo

07. Participação de receita por gênero musical Intermediário
Solicitação do gerente de produtos: quais gêneros representam a maior parte da receita?
Entregáveis: faturamento por gênero, percentual de participação no total e gráfico de barras ou pizza.
SQL: InvoiceLine, Track, Genre, SUM() e JOIN.

08. Produtos com baixa performance Intermediário
Solicitação do gerente de catálogo: quais músicas nunca foram vendidas? E quais tiveram apenas uma unidade vendida?
Entregáveis: total de músicas sem vendas, músicas com uma venda e distribuição da quantidade vendida por faixa.
SQL: LEFT JOIN, COALESCE(), COUNT() e HAVING.

09. Concentração de receita — Curva ABC Avançado
Solicitação da diretoria: queremos saber se uma pequena parcela dos artistas é responsável pela maior parte do faturamento.
Entregáveis: receita por artista, percentual acumulado da receita, classificação ABC e gráfico de Pareto.
SQL: CTE, SUM() OVER(), ORDER BY e CASE.

### Módulo 4 — Análise comercial

10. Desempenho dos representantes por período Intermediário
Solicitação do gerente comercial: como evoluiu o faturamento da carteira de clientes de cada representante?
Entregáveis: receita mensal por representante, média mensal e gráfico de linhas com uma série por funcionário.
SQL: Employee, Customer, Invoice, agrupamento por funcionário e mês.

11. Dependência de grandes clientes Intermediário
Solicitação da diretoria: qual percentual da receita de cada representante vem de seus três maiores clientes?
Entregáveis: receita total da carteira, receita dos três maiores clientes e percentual de concentração.
SQL: CTE, ROW_NUMBER() ou DENSE_RANK() e agregações.

### Módulo 5 — Desafios de análise avançada

12. Análise de coorte de clientes Avançado
Solicitação do marketing: clientes que realizaram a primeira compra em determinado mês continuam comprando nos meses seguintes?
Entregáveis: mês da primeira compra, meses decorridos e percentual de clientes que voltaram a comprar. Visualização em mapa de calor.
SQL: CTE, MIN(), datas, COUNT(DISTINCT ...). Python: pandas e Matplotlib.

13. Análise de cesta de compras Avançado
Solicitação do gerente de produtos: quais gêneros musicais aparecem juntos com mais frequência em uma mesma compra?
Entregáveis: pares de gêneros, quantidade de pedidos compartilhados e ranking das combinações mais comuns.
SQL: self-join, DISTINCT, agrupamento e contagens.


### 🛠️ Tecnologias utilizadas

- SQLite — Consultas e manipulação de dados
- Python — Processamento e automação
- Pandas — Análise e tratamento de dados
- Matplotlib — Visualização de dados
