from functions import *

# Programa de um jogo de azar
# Não é o jogo do tigrinho

# 0. Apresentado uma introdução no terminal CHECK
# 1. Registrar o nome do jogador CHECK
# 2. Apresentar as regras do jogo CHECK
# 3. Jogar
# 3.1. Implementar função dado CHECK
# 4. Apresentar resultados
# 5. Registrar o resultado em um registro fixo (.txt)
# 6. Abre um menu para perguntar se quer tentar de novo

# Elementos conceituais a serem trabalhados nesse projeto
# - Identação
# - Variáveis
# - Operações matemáticas
# - Criação de módulos
# - Importação de bibliotecas
# - Funções, Rotinas e Métodos
# - Interface com usuário
# - Encapsulamento
# - Divisão de responsabilidades
# - Documentação
# - Erros
# - Arquitetura de Software
# - Manipulação de Dados
# - Operações lógicas

# - Estruturas condicionais
# - Estruturas de repetição
# - Manipulação de arquivos
# - etc.

# Conceitos avançados
# - Programação Orientada a Objetos (POO)



def intro():
    """Essa função introduz o jogador ao jogo.""" # DocString: descrição da função
    print("Olá, jogador.")
    nomeJogador = input("Qual é o seu nome, jogador? ")
    print(f'Seja bem vindo, {nomeJogador}') # F-String

def apresentaRegra():
    """Essa função apresenta as regras do jogo para o jogador.""" # DocString: descrição da função
    print("As regras do jogo são essas:")
    print("1. Escolher um número de 1 a 100.")
    print("2. Escolhe quantos dados de 6 lados você quer lançar nesta rodada.")
    print("3. Lança e verifica o quão próximo está do valor escolhido.")
    print("4. Se estiver no terceiro turno, o jogo acaba. Se não, continua.")
    print("5. O jogador pode lançar uma quantidade de dados para tentar alcançar o valor escolhido ou parar de arriscar e ficar com o valor de soma acumalado dos dados. Se escolher jogar de novo, volta ao passo 2.")
    print("6. Depois que os turnos acabarem ou o jogador parar de jogar os dados, os pontos são calculados em função da proximidade entre a soma de todos os dados jogados e o valor escolhido inicialmente.")
    print("7. A pontuação também sofrerá uma correção proporcional ao número de dados rolados e inversamente proporcional ao número de turnos jogados.")

def inicioJogo():
    pass
def registroPontos():
    pass
def sairTela():
    pass
    

# Estrutura padrão em programas principais
if __name__=="__main__":
    intro()
    apresentaRegra()
    inicioJogo()
    registroPontos()
    sairTela()