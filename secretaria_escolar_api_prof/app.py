from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect
from urllib.parse import unquote

from model import Session, Professor
from schemas import *


info = Info(title = "API Secretaria Escolar - Cadastro de Professores", version = "1.1.0")
app = OpenAPI(__name__, info = info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
professor_tag = Tag(name="Secretaria Escolar - Professores", description="Adição, visualização e remoção de professores à base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/cadastra_professor', tags=[professor_tag],
          responses={"200": ProfessorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def insere_professor(form: ProfessorSchema):
    """Cadastra um novo professor à base de dados

    Retorna uma representação do professor.
    """
    professor = Professor(
        matricula = form.matricula,
        nome = form.nome,
        cpf = form.cpf,
        telefone = form.telefone,
        endereco = form.endereco,
        cidade = form.cidade,
        cep = form.cep,
        disciplina = form.disciplina,
        unidade_escolar = form.unidade_escolar
        )

    try:
        # criando conexão com a base de dados
        session = Session()
        # adicionando um novo professor à base de dados
        session.add(professor)
        # efetivando o comando de adição de novo professor na tabela
        session.commit()
        return exibe_professor(professor), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Professor com a mesma matrícula existente na base de dados:/"
        return {"mensagem de erro de integridade": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível cadastrar um novo professor :/"
        return {"mensagem de erro": error_msg}, 400


@app.get('/listagem_professores', tags=[professor_tag],
         responses={"200": ListagemProfessoresSchema, "404": ErrorSchema})
def busca_professores():
    """Faz a busca por todos os professores cadastrados na base de dados

    Retorna uma representação da listagem de professores.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    professores = session.query(Professor).all()
    
    if not professores:
        # se não há professores cadastrados
        return {"professores": []}, 200
    else:
        # retorna a representação da listagem de professores
        return exibe_professores(professores), 200


@app.get('/busca_professor', tags=[professor_tag],
         responses={"200": ProfessorViewSchema, "404": ErrorSchema})
def busca_professor(query: BuscaProfessorSchema):
    """Faz a busca por um professor a partir da matrícula do professor.

    Retorna uma representação do professor.
    """
    #matricula_prof = query.matricula
    matricula_prof = query.matricula
    # criando conexão com a base de dados
    session = Session()
    # fazendo a busca
    professor = session.query(Professor).filter(Professor.matricula == matricula_prof).first()
    
    if not professor:
        # se o professor não foi encontrado
        error_msg = "Professor não encontrado na base de dados:/"
        return {"mensagem de erro": error_msg}, 404
    else:
        # retorna a representação de professor
        return exibe_professor(professor), 200


@app.delete('/remove_professor', tags=[professor_tag],
            responses={"200": RemoveProfessorSchema, "404": ErrorSchema})
def remove_professor(query: BuscaProfessorSchema):
    """Remove um professor a partir da matrícula informada

    Retorna uma mensagem de confirmação da remoção do professor.
    """
    
    #matricula_prof = query.matricula
    matricula_prof = query.matricula
    # criando conexão com a base de dados
    session = Session()
    # fazendo a remoção do professor da base de dados
    contador = session.query(Professor).filter(Professor.matricula == matricula_prof).delete()
    session.commit()
    
    if contador:
        # se o professor foi removido da base de dados
        return {"mensagem": "Professor removido", "Matrícula": matricula_prof}
    else:
        # se o professor não foi encontrado na base de dados
        error_msg = "Professor não encontrado na base de dados:/"
        return {"mensagem": error_msg}, 404
