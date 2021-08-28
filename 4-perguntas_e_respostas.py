perguntas = {
    'Pergunta Atividades - 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': 'Atividades - 1',
            'b': '4',
            'c': '8'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {
            'a': '8',
            'b': '12',
            'c': '6'
        },
        'resposta_certa': 'c',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha a opção correta abaixo.')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario.lower() == pv['resposta_certa']:
        print(f'EHHHHHHH! Você acerto')
        respostas_certas += 1
    else:
        print('IXIIIIIII! Você errou!')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} pergunta.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%')