### Módulo 1 — Análise financeira

01. Evolução do faturamento mensal Básico
Solicitação do gestor: precisamos identificar os meses de maior e menor faturamento e avaliar se a receita está crescendo.
Entregáveis:
    receita mensal: Somatória de todo valor arrecadado pela empresa. Tabela `Invoice` tem os dados de datas de pagamentos no campo `InvoiceDate` e tem o valor total de vendas por cada cliente no campo `Total`. Neste caso é só tratar o campo de data para retornar apenas mês e ano, somar o campo de totais e agrupar por mês.

    ``` sql
        SELECT strftime('%Y-%m', invoicedate) as mes_ano, sum(total)as Total_vendas from Invoice
        GROUP by strftime('%Y-%m', invoicedate)
        ORDER by mes_ano 
    ```
    quantidade de pedidos por mês: Na mesma tabela `Invoice` basta fazer um count e agrupar por mês e ano, com o valor resultante do campo de data.
    ``` sql
        SELECT strftime('%Y-%m', invoicedate) as mes_ano, count(*)as qtd_pedidos
        from Invoice
        GROUP by strftime('%Y-%m', invoicedate)
        ORDER by mes_ano 
    ```
	ticket médio mensal: Aqui basicamente usa os resultados acima, na fóruma Tm = Rm / Qp.
    ``` sql
        SELECT strftime('%Y-%m', invoicedate) as mes_ano, (sum(total)/ count(*)) as ticket_medio
        from Invoice
        GROUP by strftime('%Y-%m', invoicedate)
        ORDER by mes_ano 
    ```
    Aqui, uma versão da consulta retornando todas as informações em uma unica consulta
    ```sql
    SELECT strftime('%Y-%m', invoicedate) as mes_ano, sum(total) as Total_pedido, count(*) as qtd_pedido,  (sum(total)/ count(*)) as ticket_medio
    from Invoice
    GROUP by strftime('%Y-%m', invoicedate)
    ORDER by mes_ano    
    ```
    gráfico de linhas:

SQL: strftime(), SUM(), COUNT(), GROUP BY.