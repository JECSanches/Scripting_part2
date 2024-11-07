import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

# Main function
def plot_pivot_table(data, value, index, function, option='default', ylabel=None, xlabel=None):
    if option == 'default':
        pd.pivot_table(data, values=value, index=index, aggfunc=function).plot(figsize=[13,5])
    elif option == 'unstack':
        pd.pivot_table(data, values=value, index=index, aggfunc=function).unstack().plot(figsize=[13,5])
    elif option == 'sort':
        pd.pivot_table(data, values=value, index=index, aggfunc=function).sort_values(value).plot(figsize=[13,5])

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    return None

print('O nome do nosso script é: ', sys.argv[0])


for mes in sys.argv[1:]:

    print('Mês de referência é: ', mes)

    # Dataset
    df = pd.read_csv('SINASC_RO_2019_'+mes+'.csv')

    max_data = df.DTNASC.max()[:7]
    print(max_data)

    # Construção da pasta
    os.makedirs('./figs/'+max_data, exist_ok=True)

    # Plots
    plot_pivot_table(df, 'IDADEMAE', 'DTNASC', 'mean', ylabel='média idade mãe', xlabel='data nascimento')
    plt.savefig('./figs/'+max_data+'/media_idade_mae.png', dpi=200)

    plot_pivot_table(df, 'IDADEMAE', ['DTNASC', 'SEXO'], function='mean',
                    ylabel='média idade mãe', xlabel='data nascimento', option='unstack')
    plt.savefig('./figs/'+max_data+'/idade_mae_sexo_bebe.png', dpi=200)

    plot_pivot_table(df, 'PESO', ['DTNASC', 'SEXO'], function='mean',
                    ylabel='média peso bebê', xlabel='data nascimento', option='unstack')
    plt.savefig('./figs/'+max_data+'/media_peso_bebe_por_sexo.png', dpi=200)

    plot_pivot_table(df, 'PESO', 'ESCMAE', function='median',
                    ylabel='peso mediano', xlabel='escolaridade mãe', option='sort')
    plt.savefig('./figs/'+max_data+'/peso_mediano_por_escolaridade_mae.png', dpi=200)

    plot_pivot_table(df, 'APGAR1', 'GESTACAO', function='mean',
                    ylabel='apgar1 médio', xlabel='gestação', option='sort')
    plt.savefig('./figs/'+max_data+'/media_apigar1_por_gestacao.png', dpi=200)

    print('Rotina finalizada para: {}.'.format(mes))
    print('----------------------------------')