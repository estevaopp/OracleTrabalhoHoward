select p.codigo_agendamento
     , p.data_agendamento
     , c.nome as cliente
     , nvl(f.nome_fantasia, f.razao_social) as empresa
     , i.codigo_item_agendamento as item_agendamento
     , prd.descricao_produto as produto
     , i.quantidade
     , i.valor_unitario
     , (i.quantidade * i.valor_unitario) as valor_total
  from agendamentos p
  inner join clientes c
  on p.cpf = c.cpf
  inner join fornecedores f
  on p.cnpj = f.cnpj
  left join itens_agendamento i
  on p.codigo_agendamento = i.codigo_agendamento
  left join produtos prd
  on i.codigo_produto = prd.codigo_produto
  order by c.nome, i.codigo_item_agendamento