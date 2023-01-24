import re

num_dict = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'zero': 0,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60, 
    'setenta': 70, 
    'oitenta': 80, 
    'noventa': 90, 
    'cem': 100,
    'cento': 100,
    'duzentos': 200,
    'trezentos': 300,
    'quatrocentos': 400,
    'quinhentos': 500,
    'seissentos': 600,
    'setessentos': 700,
    'oitossentos': 800,
    'novessentos': 900,
    'mil': 1000,
    'milhão': 1000000,
    'milhões': 1000000,
    'bilhão': 1000000000,
    'bilhões': 1000000000,
    'trilhão': 1000000000000,
    'trilhões': 1000000000000,
}

def brw2n(brword):    
    default_patterns = [
        'trilhões'
        'trilhão'
        'bilhões',
        'bilhão',
        'milhões',
        'milhão',
        'mil',
    ] 
    for dp in default_patterns:
        pattern = r'([A-Za-z0-9]+) e ([A-Za-z0-9]+) {}'.format(dp)
        result = re.search(pattern, brword)
        if not result:
            pattern = r'([A-Za-z0-9]+) {}'.format(dp)
            result = re.search(pattern, brword)
        if result:
            number = (str(dp) + " ") * num_dict[result.group(1)]
            brword = brword.replace(result.group(1) + " "+dp, number)
    
    words = brword.split(' ')
    number = 0
    for word in words:
        if word in num_dict.keys():
            number += int(num_dict[word])

    return number

print (brw2n("vinte e um"))