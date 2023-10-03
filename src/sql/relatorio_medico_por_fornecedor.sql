with sumariza_medicos as (
    select cnpj
         , count(1) as qtd_medicos
      from medicos
      group by cnpj
)

select nvl(f.nome_fantasia, f.razao_social) as empresa
     , sp.qtd_medicos
     , sum(i.quantidade * i.valor_unitario) as valor_total
  from medicos p
  inner join sumariza_medicos sp
  on p.cnpj = sp.cnpj
  inner join fornecedores f
  on p.cnpj = f.cnpj
  inner join itens_medico i
  on p.codigo_medico = i.codigo_medico
  group by sp.qtd_medicos, nvl(f.nome_fantasia, f.razao_social)
  order by nvl(f.nome_fantasia, f.razao_social)