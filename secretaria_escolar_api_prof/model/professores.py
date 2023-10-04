from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Professor(Base):
    __tablename__ = 'tbl_professores'

    id = Column("pk_professor", Integer, primary_key = True)
    matricula = Column(String(6), unique = True)
    nome = Column(String(100))
    cpf = Column(String(11))
    telefone = Column(String(11))
    endereco = Column(String(100))
    cidade = Column(String(30))
    cep = Column(String(8))
    disciplina = Column(String(30))
    unidade_escolar = Column(String(20))
    data_insercao = Column(DateTime, default = datetime.now())

    def __init__(self, matricula: str, nome: str, cpf: str, telefone: str, endereco: str,
                 cidade: str, cep: str, disciplina: str, unidade_escolar: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um registro para um professor com os seguintes argumentos:
            matricula: matrícula do professor.
            nome: nome do professor.
            cpf: cpf do professor.
            telefone: telefone do professor.
            endereco: endereço do professor.
            cidade: cidade onde o professor reside.
            cep: cep do endereço do professor.
            disciplina: disciplina que o professor leciona.
            unidade_escolar: unidade escolar onde o professor leciona.
            data_insercao: data na qual o professor foi cadastrado.
        """
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.cep = cep
        self.disciplina = disciplina
        self.unidade_escolar = unidade_escolar

        # se não for informada, será a data do cadastro do professor
        if data_insercao:
            self.data_insercao = data_insercao