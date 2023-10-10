with sumariza_agendamentos as (
    select cpf
         , count(1) as qtd_agendamentos
      from agendamentos
      group by cpf
)

select e.nome as paciente
     , sp.qtd_agendamentos
     , sum(f.valor_consulta) as CustoConsultas
  from agendamentos p
  inner join sumariza_agendamentos sp
  on p.cpf = sp.cpf
  inner join medicos f
  on p.crm = f.crm
  inner join pacientes e
  on p.cpf = e.cpf
  group by sp.qtd_agendamentos, e.nome
  order by e.nome