print('\033[34mOlá, sejá bem- vindo ao Chat Bot Dúvidas Frequentes.\033[m')
nome = str(input('Me diga primeiramente qual o seu nome ou apelido: '))
email = input(f'Qual o seu email, {nome}? ')
felizoutriste = input('Você está feliz ou triste hoje? ').upper()
if felizoutriste in 'FELIZ':
    print('A vida é boa mesmo, continue assim, se sentir feliz é tudo de bom!!!')
elif felizoutriste in 'TRISTE':
    print('''Não há por que estar triste, a vida é boa demais pra ficar assim, se está triste por algo
faça outra coisa que te deixa feliz, leia um livro, vejá um video de gatinho sorrindo.''')
print('''Aqui temos algumas opções de perguntas para você:
  1 - O que é o mundo?
  2 - Por que nascemos?
  3 - O que é bom ouvir?
  4 - Que estilo de vida é saúdavel? ''')

while True:
    opcão = input(f'Qual a sua opção {nome}? '
                  f'')
    if opcão == '1':
        print(f'''
O mundo {nome}, é tudo aquilo que constituiu a realidade.
É o conjunto de tudo que existe, Totalidade dos Astros e Planetas; Universo.
Embora esclarecer o conceito de mundo tenha sempre sido considerada
uma das tarefas básicas da filosofia Ocidental, este tema parece ter sido levantado explicitamente
no início do Século XX.''')
    elif opcão == '2':
        print(f'''
{nome}, não poderíamos morrer pra depois nascer.
Não poderíamos morrer sem termos nascido.
Logo, nascemos para aprender, experimentar, saborear, compreender a vida e depois, sem nos despedirmos, morrer. ''')
    elif opcão == '3':
        print(f'''
{nome}, Os benefícios da música vão desde o alívio de dores, a melhora da memória e até mesmo um estímulo 
para a prática de atividade física
Ouvir música libera dopamina e causa uma sensação de bem-estar e, por isso, tem sido usada por médicos, terapeutas
e preparadores físicos para o tratamento de diversos problemas.''')
    elif opcão == '4':
        print(f'''
{nome}, um estilo de vida saudável inclui a saúde preventiva, boa nutrição e controle do peso, recreação, 
exercícios regulares, e evitar substâncias nocivas ao organismo. Mas acima de tudo, uma vida saúdavel é aquela
que você se sente bem e é feliz com o que faz. ''')
    else:
        print('Desculpe, opção inválida! Tente selecionar algumas das opções indicadas. ')
