from tqdm import tqdm
import time

print('Curso de Python SENAI!\n')
print('O programa a seguir irá cadastrar as notas dos 30 discentes do curso de Python. Para isso, você deve informar o nome do aluno e em seguida colocar as 5 notas de cada disciplina, lembrando que as notas são de 0 a 10. Ao final do programa, você poderá ter a listagem dos aprovados e dos reprovados.\n')

# Listas de alunos e de notas
alunos = []
notas = []

# Receber os dados dos alunos
for i in range(30):
    nome = input(f"Digite o nome do discente {i+1}: ")
    alunos.append(nome)

    notas_aluno = []
    for j in range(5):
        while True:
            try:
                nota = float(input(f"Digite a nota {j+1} do discente {nome} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas_aluno.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Por Favor, digite um entrada válida e tente novamente.")
    print('Inserindo as notas...')
    notas.append(notas_aluno)
    for i in tqdm(range(100)):
        time.sleep(0.05)

# Calcular a média e verifica aprovação
aprovados = []
reprovados = []
for i in range(30):
    media = sum(notas[i]) / 5
    if media >= 7:
        aprovados.append(alunos[i])
    else:
        reprovados.append(alunos[i])

while True:
    print("\nOpções:")
    print("1. Lista de aprovados")
    print("2. Lista de reprovados")
    print("3. Encerrar programa")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nLista de discentes aprovados:")
        for i in tqdm(range(100)):
            time.sleep(0.05)
        for aprovado in aprovados:
            print(aprovado)
    elif opcao == '2':
        print("\nLista de discentes reprovados:")
        for i in tqdm(range(100)):
            time.sleep(0.05)
        for reprovado in reprovados:
            print(reprovado)
    elif opcao == '3':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")