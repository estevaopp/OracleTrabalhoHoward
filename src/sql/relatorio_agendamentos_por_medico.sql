with sumariza_agendamentos as (
    select cnpj
         , count(1) as qtd_agendamentos
      from agendamentos
      group by cnpj
)

select nvl(f.nome_fantasia, f.razao_social) as empresa
     , sp.qtd_agendamentos
     , sum(i.quantidade * i.valor_unitario) as valor_total
  from agendamentos p
  inner join sumariza_agendamentos sp
  on p.cnpj = sp.cnpj
  inner join medicos f
  on p.cnpj = f.cnpj
  inner join itens_agendamento i
  on p.codigo_agendamento = i.codigo_agendamento
  group by sp.qtd_agendamentos, nvl(f.nome_fantasia, f.razao_social)
  order by nvl(f.nome_fantasia, f.razao_social)