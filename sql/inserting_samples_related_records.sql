/*INSERE DADOS NA TABELA DE PEDIDOS E ITENS*/
DECLARE
  VCOD_PEDIDO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PEDIDOS_CODIGO_PEDIDO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '43201234567',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );

END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PEDIDOS_CODIGO_PEDIDO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '01234567891',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PEDIDOS_CODIGO_PEDIDO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '87654320123',  /*CPF*/
                             '01234567891234'/*CNPJ*/
                             );
  
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PEDIDOS_CODIGO_PEDIDO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '32012345678',  /*CPF*/
                             '00001234567891'/*CNPJ*/
                             );
                                  
END;
--
DECLARE
  VCOD_PEDIDO NUMBER;
  VCOD_ITEM_PEDIDO NUMBER;
  VCOD_PRODUTO NUMBER;
BEGIN
  VCOD_PEDIDO := LABDATABASE.PEDIDOS_CODIGO_PEDIDO_SEQ.NEXTVAL;
  
  INSERT INTO LABDATABASE.PEDIDOS VALUES(VCOD_PEDIDO,    /*CODIGO_PEDIDO*/
                             SYSDATE,        /*DATA_PEDIDO*/
                             '76543201234',  /*CPF*/
                             '00012345678912'/*CNPJ*/
                             );
                                  
END;