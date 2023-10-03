/*INSERE DADOS NA TABELA DE MEDICOS E ITENS*/
DECLARE
  VCOD_MEDICO NUMBER;
BEGIN
  VCOD_MEDICO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.MEDICOS VALUES(VCOD_MEDICO,    /*CODIGO_MEDICO*/
                             SYSDATE,        /*DATA_MEDICO*/
                             '43201234567',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
END;
--
DECLARE
  VCOD_MEDICO NUMBER;
BEGIN
  VCOD_MEDICO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.MEDICOS VALUES(VCOD_MEDICO,    /*CODIGO_MEDICO*/
                             SYSDATE,        /*DATA_MEDICO*/
                             '01234567891',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             ); 
END;
--
DECLARE
  VCOD_MEDICO NUMBER;
BEGIN
  VCOD_MEDICO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.MEDICOS VALUES(VCOD_MEDICO,    /*CODIGO_MEDICO*/
                             SYSDATE,        /*DATA_MEDICO*/
                             '87654320123',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
  
END;
--
DECLARE
  VCOD_MEDICO NUMBER;
BEGIN
  VCOD_MEDICO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.MEDICOS VALUES(VCOD_MEDICO,    /*CODIGO_MEDICO*/
                             SYSDATE,        /*DATA_MEDICO*/
                             '32012345678',  /*CPF*/
                             '00001234567891'/*CNPJ*/
                             );
END;
--
DECLARE
  VCOD_MEDICO NUMBER;
BEGIN
  VCOD_MEDICO := LABDATABASE.PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.MEDICOS VALUES(VCOD_MEDICO,    /*CODIGO_MEDICO*/
                             SYSDATE,        /*DATA_MEDICO*/
                             '76543201234',  /*CPF*/
                             '00012345678912'/*CNPJ*/
                             );                              
END;