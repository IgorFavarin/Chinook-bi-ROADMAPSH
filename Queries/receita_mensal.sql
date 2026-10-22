  SELECT strftime('%Y-%m', invoicedate) as mes_ano, sum(total) as Total_pedido
    from Invoice
    GROUP by strftime('%Y-%m', invoicedate)
    ORDER by mes_ano    