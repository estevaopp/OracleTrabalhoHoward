with sumariza_agendamentos as (
    select crm
         , count(1) as qtd_agendamentos
      from agendamentos
      group by crm
)

select nvl(f.nome) as medico
     , sp.qtd_agendamentos
  from agendamentos p
  inner join sumariza_agendamentos sp
  on p.crm = sp.crm
  inner join medicos f
  on p.crm = f.crm
  group by sp.qtd_agendamentos, nvl(f.nome)
  order by nvl(f.nome)