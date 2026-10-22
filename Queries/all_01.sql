  SELECT strftime('%Y-%m', invoicedate) as mes_ano, sum(total) as Total_pedido, count(*) as qtd_pedido,  (sum(total)/ count(*)) as ticket_medio
    from Invoice
    GROUP by strftime('%Y-%m', invoicedate)
    ORDER by mes_ano    