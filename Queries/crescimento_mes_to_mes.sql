with CALCULO_RECEITA_MENSAL AS
    (SELECT strftime('%Y-%m', invoicedate) as mes_ano, sum(total)as receita_mensal from Invoice
  GROUP by strftime('%Y-%m', invoicedate))
  SELECT mes_ano, receita_mensal, 
  LAG(receita_mensal) over (ORDER by mes_ano) as receita_mês_anterior,
  ROUND(receita_mensal - lag(receita_mensal)over (order by mes_ano),2) as diferenca_absoluta,
  ROUND(
  	(((receita_mensal - lag(receita_mensal)over (order by mes_ano)) /
  	NULLIF(LAG(receita_mensal) OVER (ORDER BY mes_ano),0)
    )*100),2) as diferenca_relativa
    from CALCULO_RECEITA_MENSAL
    ORDER by mes_ano