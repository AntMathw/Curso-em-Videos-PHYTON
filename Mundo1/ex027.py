#DESAFIO 027 DO CURSO EM VÍDEO

nome = str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer! ')
dividido = nome.split()
print('Seu primeiro nome é: {}'.format(dividido[0]))
print('Seu ultimo nome é: {}'.format(dividido[-1]))
