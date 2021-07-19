motorista = int(input('Digite velocidade do veiculo: '))
placa_veiculo = 'CMG-3164'

infra_media = float(130.16)
infra_grave = float(195.23)
infra_gravissima = float(880.41)

if motorista > 40 and motorista < 60:
    print('Limite da via e: 40km > Placa CMG-3164 ultrapassou o limite de velocidade multa media: {0}'.format(infra_media))
elif motorista > 60 and motorista < 90:
    print('Limite da via e: 60km >  Placa CMG-3164 ultrapassou o limite de velocidade multa grave: {0}'.format(infra_grave))
elif motorista > 90:
    print('Limite da via e: 90km > Placa CMG-3164 ultrapassou o limite de velocidade multa gravissima: {0}'.format(infra_gravissima))
else:
    print('Limite aceito, multa nao registrada')


