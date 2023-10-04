from pydantic import BaseModel
from typing import Optional, List
from model.professores import Professor



class ProfessorSchema(BaseModel):
    """ Define como deve ser representado um professor que será cadastrado.
    """
    matricula: str = "MAT001"
    nome: str = "Alexandre"
    cpf: str = "12345678900"
    telefone: str = "21999999999"
    endereco: str = "Av Pres Vargas, 42 - Centro"
    cidade: str = "Cordeiro"
    cep: str = "28540000"
    disciplina: str = "Matemática"
    unidade_escolar: str = "Cordeiro"


class BuscaProfessorSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca, que será
        feita apenas com base na matrícula do professor.
    """
    matricula: str = "MAT001"


class ListagemProfessoresSchema(BaseModel):
    """ Define como uma listagem de professores cadastrados será retornada.
    """
    list_professores:List[ProfessorSchema]


def exibe_professores(professores: List[Professor]):
    """ Retorna uma representação da listagem de professores cadastrados seguindo o schema definido em
        ProfessorViewSchema.
    """
    result = []
    for professor in professores:
        result.append({
            "matricula": professor.matricula,
            "nome": professor.nome,
            "cpf": professor.cpf,
            "telefone": professor.telefone,
            "endereco": professor.endereco,
            "cidade": professor.cidade,
            "cep": professor.cep,
            "disciplina": professor.disciplina,
            "unidade_escolar": professor.unidade_escolar
        })

    return {"professores": result}


class ProfessorViewSchema(BaseModel):
    """ Define como um professor cadastrado será retornado.
    """
    id: int = 1
    matricula: str = "MAT001"
    nome: str = "Alexandre"
    cpf: str = "12345678900"
    telefone: str = "21999999999"
    endereco: str = "Av Pres Vargas, 42 - Centro"
    cidade: str = "Cordeiro"
    cep: str = "28540000"
    disciplina: str = "Matemática"
    unidade_escolar: str = "Cordeiro"


class RemoveProfessorSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção de um professor.
    """
    mensagem_remove_professor: str
    nome_remove_professor: str


def exibe_professor(professor: Professor):
    """ Retorna uma representação do professor seguindo o schema definido em
        ProfessorViewSchema.
    """
    return {
        "matricula": professor.matricula,
        "nome": professor.nome,
        "cpf": professor.cpf,
        "telefone": professor.telefone,
        "endereco": professor.endereco,
        "cidade": professor.cidade,
        "cep": professor.cep,
        "disciplina": professor.disciplina,
        "unidade_escolar": professor.unidade_escolar
    }
