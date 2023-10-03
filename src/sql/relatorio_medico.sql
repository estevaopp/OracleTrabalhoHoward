select p.codigo_medico
     , p.data_medico
     , c.nome as paciente
     , nvl(f.nome_fantasia, f.razao_social) as empresa
     , i.codigo_item_medico as item_medico
     , prd.descricao_produto as produto
     , i.quantidade
     , i.valor_unitario
     , (i.quantidade * i.valor_unitario) as valor_total
  from medicos p
  inner join pacientes c
  on p.cpf = c.cpf
  inner join fornecedores f
  on p.cnpj = f.cnpj
  left join itens_medico i
  on p.codigo_medico = i.codigo_medico
  left join produtos prd
  on i.codigo_produto = prd.codigo_produto
  order by c.nome, i.codigo_item_medico