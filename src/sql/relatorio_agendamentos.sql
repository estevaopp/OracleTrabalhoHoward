select p.codigo_agendamento
     , p.data_agendamento
     , c.nome as paciente
     , f.nome as medico
  from agendamentos p
  inner join pacientes c
  on p.cpf = c.cpf
  inner join medicos f
  on p.crm = f.crm
  order by c.nome