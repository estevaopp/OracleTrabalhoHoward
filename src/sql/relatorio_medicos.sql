select f.cnpj
       , f.razao_social
       , f.nome_fantasia
  from medicos f
 order by f.nome_fantasia