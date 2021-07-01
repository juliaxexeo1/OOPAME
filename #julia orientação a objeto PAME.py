#julia orientação a objeto PAME


#base de dados


alunos=[]
professores=[]
materias=[]
turmas=[]

#minhas classes
class Aluno:
    def __init__(self, nome_aluno):
        self.nome_aluno = nome_aluno
    
    def __str__(self) -> str:
        return self.nome_aluno #como ele vai imprimir um objeto da classe alunoc

class Professor:
    def __init__(self, nome_professor):
        self.nome_professor = nome_professor
    
    def __str__(self) -> str:
        return (self.nome_professor)

#MATERIA
class Materia:
    def __init__(self, nome_materia):
        self.nome_materia = nome_materia
    
    def __str__(self) -> str:
        return (self.nome_materia)

class Turma:
    def __init__ (self,nome_turma):
        self.nome_turma=nome_turma
        self._prof=None
        self._mat=None
        self._alunos=[] #usamos lista porque são vários alunos

    def __str__(self) -> str:
        return ("Turma: " + self.nome_turma)

    def imprime(self):
        print(self)
        if self.prof:
            print("Professor(a): "+str(self.prof))

   
    @property
    def prof(self):
        return self._prof
   
    @property
    def mat(self):
        return self._mat
    
    @property #o que recupera
    def alunos(self):
        return self._alunos
   
    @mat.setter #o que salva
    def mat(self, a):
         self._mat = a

    @prof.setter
    def prof(self, a):
         self._prof = a
    
    def incluir_aluno(self,aluno):
        self._alunos.append(aluno)
        




#minhasfunções 
def cadastroaluno():
    nomedonovoaluno=input("nome do aluno a ser adicionado: ")
    novoaluno=Aluno(nomedonovoaluno)
    alunos.append(novoaluno)

def cadastroprofessor():
    nomenovoprof=input("nome do professor a ser adicionado: ")
    novoprof=Professor(nomenovoprof)
    professores.append(novoprof)

def cadastromateria():
    nomenovamat= input("nome da nova materia: ")
    novamateria=Materia(nomenovamat)
    materias.append(novamateria)

def cadastroturma():
    nomenovaturma = input ("nome da nova turma: ")
    novaturma = Turma(nomenovaturma)
    turmas.append(novaturma)


def imprimirtodos(lista):
    if len(lista) == 0:
        print("não há cadastrados")
        return True
    print("MOSTRANDO OS CADASTROS:")
    i = 0
    for item in lista:
        i += 1
        print(i,item)
        

def selecionar_prof(turma):
    if len(professores) == 0:
        print("não exitem professores cadastrados")
        return False
    imprimirtodos(professores)
    profturma = int(input("escolha o número do professor: "))
    print("sair: para sair digite 0")
    if 0<profturma<=len(professores):
        turma.prof = professores[profturma-1]
        return turma
    return False

def selecionar_alunos(turma):
    if len(alunos) == 0:
        print("não exitem alunos cadastrados")
        return False
    imprimirtodos(alunos)
    alunoescolhido = int(input("escolha o número do aluno a ser adicionado: "))
    print("sair: para sair digite 0")
    if 0<alunoescolhido<=len(alunos):
        turma.alunos = alunos[alunoescolhido-1]
        return turma
    return False


def escolher_turma():
    if len(turmas) == 0:
        print("não exitem turmas cadastradas")
        return False
    print("Essas são as turmas cadastradas:")
    imprimirtodos(turmas)
    print("sair: para sair digite 0")
    turma_escolhida = int(input("escolha o número da turma: "))
    if 0<turma_escolhida<=len(turmas):
        return turmas[turma_escolhida -1]
    return False

def designar_professor():
    if t:=escolher_turma():#walrus #assignment que economiza as variáveis intermediarias, escolhemos a turma e ao mesmo tempo guardamos no t
        return selecionar_prof(t) 

def adicionar_alunos(): #melhorar, não esta dando certo
    if t:=escolher_turma():
        return selecionar_alunos(t)

        

#SEGUNDO MENU:
def menusecundario():
    print("MENU TURMAS") 
    print(" Escolha uma opção:\n\n -Para cadastrar uma nova turma digite 1 ")
    print(" -Para designar um professor para uma turma digite 2 \n -Para adicionar alunos em uma turma digite 3")
    print(" -Para remover alunos de uma turma digite 4 \n -Para dar a nota final a todos alunos de uma turma digite 5")
    print(" -Para mostrar todos os alunos de uma turma digite 6 \n -Para mostrar todas as turmas cadastradas digite 7")
    print(" -caso deseje voltar ao menu principal digite 0")
    escolhamt=input("Por favor escolha ")
   
   #CADASTRO NOVA TURMA

    if escolhamt =='1': 
        print ("CADASTRO DE NOVA TURMA" )
        cadastroturma()
        

    #DESIGNAR PROFESSOR PARA UMA TURMA
    elif escolhamt == '2': 
        print ("DESIGNAR PROFESSOR PARA UMA TURMA" )
        if t:=designar_professor():
            t.imprime()
        else:
            print("professor não designado")



    #ADICIONAR ALUNOS EM UMA TURMA
    elif escolhamt == '3':
        print ("ADICIONAR ALUNOS EM UMA TURMA")
        #FALTA ADICIONAR E MELHORAR A FUNÇAO


    
    #REMOVER ALUNOS DE UMA TURMA
    elif escolhamt == '4':
        print ("REMOVER ALUNOS DE UMA TURMA")
        #FALTA

    
    #DAR NOTA FINAL 
    elif escolhamt == '5':
        print ("DE AS NOTAS FINAIS")
        #FALTA


    #MOSTRANDO TODOS OS ALUNOS DA TURMA
    elif escolhamt == '6':
        print ("MOSTRANDO TODOS OS ALUNOS DA TURMA")
        #FALTA


    #MOSTRANDO TODAS AS TURMAS CADASTRADAS
    elif escolhamt == '7':
        print ("MOSTRANDO TODAS AS TURMAS CADASTRADAS")
        imprimirtodos(turmas)
        #MOSTRANDO MAS SEM A ORDEM

    #VOLTAR AO MENU PRINCIPAL 
    elif escolhamt == '0': 
        print("VOLTAR AO MENU PRINCIPAL")
    
    else: 
        print ("opção desconhecida")


#MENU PRINCIPAL
def menuprincipal():
    print("MENU PRINCIPAL\n Escolha uma opção:\n\n -Para cadastrar uma nova matéria digite 1 ")
    print(" -Para cadastrar um novo professor digite 2 \n -Para cadastrar um novo aluno digite 3")
    print(" -Para mostrar todas as matérias digite 4 \n -Para mostrar todos os professores digite 5")
    print (" -Para mostrar todos os alunos digite 6 \n -Para abrir o menu de turmas digite 7")
    print(" -caso deseje sair digite 0")

    escolha=input("Por favor escolha ")



#CADASTRO DE NOVA MATÉRIA
    if escolha =='1': 
        print ("CADASTRO DE NOVA MATÉRIA" )
        cadastromateria()



#CADASTRO DE NOVO PROFESSOR
    elif escolha == '2': 
        print ("CADASTRO DE NOVO PROFESSOR" )
        cadastroprofessor()

#CADASTRO DE NOVO ALUNO
    elif escolha == '3':
        print ("CADASTRO DE NOVO ALUNO")
        cadastroaluno()
        
        

#MOSTRANDO TODAS AS MATÉRIAS    
    elif escolha == '4':
        imprimirtodos(materias)

#MOSTRANDO TODOS OS PROFESSORES
    elif escolha == '5':
        imprimirtodos(professores)

#MOSTRANDO TODOS OS ALUNOS
    elif escolha == '6':
        imprimirtodos(alunos)
        

#MENU TURMAS
    elif escolha == '7':
        menusecundario()
        
#SAIR
    elif escolha == '0': 
        print("saindo")
        return False

    #CASO TENHA ALGO DIFERENTE
    else: 
        print ("opção desconhecida")
    
    return True



while menuprincipal():
    pass