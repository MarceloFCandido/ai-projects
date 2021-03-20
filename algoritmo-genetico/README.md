# Tarefa 6 - Algoritmos Genéticos

**Disciplina**: Laboratório de Inteligência Artificial

**Professor**: Rogério Martins Gomes

**Alunos**:

Marcelo Lopes de Macedo Ferreira Cândido

Milena Delarete Drummond Marques

## Objetivo

O objetivo desta atividade é implementar um algoritmo genético para resolver um problema de minimização de função com as seguintes características:

```
𝑓(𝑥,𝑦) = sin(𝑥)𝑒^((1−cos(𝑦))^2) + 𝑐𝑜𝑠(𝑦)𝑒^((1−sin(𝑥))^2) + (𝑥−𝑦)^2
```

## Execução do algoritmo

### 1. Configuração:
Na raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:
```
pip3 install -r "./requirements.txt"
```

### 2. Funcionamento:
O comando `python3 perceptron -h` mostra como usar o pacote, como visto na seguinte saída:
```
Perceptron usage:

python algoritmo-genetico -p <popsize> -m <mutation-rate>
```
Em que:
- `<popsize>`: tamanho da populacao. Exemplo: `20`
- `<mutation-rate>`: taxa de mutacao. Ideal entre `0.001` e `0.01`

## Exemplo

Para determinar o custo para o seguinte caso:

`<learning-rate>` = 20

`<max-iterations>` = 0.005

use o comando:
```
python3 algoritmo-genetico -p 20 -m 0.005
```

O resultado a ser impresso na tela será:
```
Best: 
 [29.69143182 28.44386681] -100.74544994201688
Geracao:  280
```

**OBS.:** O resultado pode variar pois, ao executar o programa, a populacao é gerada aleatóriamente aleatóriamente. 

## Versões do Python recomendadas

Dois computadores foram usados para rodar esse algoritmo e as versão utlizadas foram `3.7.4` e `3.9.1`.

## Análise dos resultados

