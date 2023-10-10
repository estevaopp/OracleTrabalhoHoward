/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.AGENDAMENTOS DROP CONSTRAINT MEDICOS_AGENDAMENTOS_FK;
ALTER TABLE LABDATABASE.AGENDAMENTOS DROP CONSTRAINT PACIENTES_AGENDAMENTOS_FK;

/*Apaga as tabelas*/
DROP TABLE LABDATABASE.MEDICOS;
DROP TABLE LABDATABASE.PACIENTES;
DROP TABLE LABDATABASE.AGENDAMENTOS;

/*Apaga as sequences*/
DROP SEQUENCE LABDATABASE.AGENDAMENTOS_CODIGO_AGENDAMENTO_SEQ;

/*Cria as tabelas*/
CREATE TABLE LABDATABASE.MEDICOS (
                CRM VARCHAR2(11) NOT NULL,
                NOME VARCHAR2(255) NOT NULL,
                VALOR_CONSULTA NUMBER(9,2) not null,
                CONSTRAINT MEDICOS_PK PRIMARY KEY (CRM)
);

CREATE TABLE LABDATABASE.PACIENTES (
                CPF VARCHAR2(11) NOT NULL,
                TELEFONE VARCHAR(11)
                NOME VARCHAR2(255) NOT NULL,
                CONSTRAINT PACIENTES_PK PRIMARY KEY (CPF)
);

CREATE TABLE LABDATABASE.AGENDAMENTOS (
                CODIGO_AGENDAMENTO NUMBER NOT NULL,
                DATA_AGENDAMENTO DATETIME NOT NULL,
                CPF VARCHAR2(11) NOT NULL,
                CRM VARCHAR2(14) NOT NULL,
                CONSTRAINT AGENDAMENTOS_PK PRIMARY KEY (CODIGO_AGENDAMENTO)
);

/*Cria as sequences*/
CREATE SEQUENCE LABDATABASE.AGENDAMENTOS_CODIGO_AGENDAMENTO_SEQ;

/*Cria os relacionamentos*/
ALTER TABLE LABDATABASE.AGENDAMENTOS ADD CONSTRAINT MEDICOS_AGENDAMENTOS_FK
FOREIGN KEY (CRM)
REFERENCES LABDATABASE.MEDICOS (CRM)
NOT DEFERRABLE;

ALTER TABLE LABDATABASE.AGENDAMENTOS ADD CONSTRAINT PACIENTES_AGENDAMENTOS_FK
FOREIGN KEY (CPF)
REFERENCES LABDATABASE.PACIENTES (CPF)
NOT DEFERRABLE;

/*Garante acesso total as tabelas*/
GRANT ALL ON LABDATABASE.MEDICOS TO LABDATABASE;
GRANT ALL ON LABDATABASE.PACIENTES TO LABDATABASE;
GRANT ALL ON LABDATABASE.AGENDAMENTOS TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;

commit;