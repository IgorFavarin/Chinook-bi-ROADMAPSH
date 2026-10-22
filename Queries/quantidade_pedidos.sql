SELECT strftime('%Y-%m', invoicedate) as mes_ano, count(*) as qtd_pedido
from Invoice
GROUP by strftime('%Y-%m', invoicedate)
ORDER by mes_ano