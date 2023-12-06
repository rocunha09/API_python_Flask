import random

'''
cria aleatoriamente um grupo de 10 pacientes e
a cada vez que for invocado quando a aplicação iniciar
criará outro grupo.
'''

grupos = ['joelho', 'coluna', 'quadril']
Pacientes = []

for i in range(1, 11):
    paciente = {
        'id': i,
        'prontuario': random.randint(100000, 999999),
        'idade': random.randint(20, 60),
        'grupo': random.choice(grupos)
    }
    Pacientes.append(paciente)
