# Tarefa 6 - Algoritmos Genéticos

**Disciplina**: Laboratório de Inteligência Artificial

**Professor**: Rogério Martins Gomes

**Alunos**:

Marcelo Lopes de Macedo Ferreira Cândido

Milena Delarete Drummond Marques

## Objetivo

O objetivo desta atividade é implementar um algoritmo genético para resolver um problema de minimização da função:
<div style="display: flex; justify-content: center">
  <img src="https://render.githubusercontent.com/render/math?math=f(x%2C%20y)%20%3D%20\sin{(x)}e^{[1%20-%20%20\cos{(y)}]^2}%20%2B%20\cos{(y)}e^{[1%20-%20\sin{(x)}]^2}%20%2B%20(x%20-%20y)^2">
</div>

## Execução do algoritmo

### 1. Configuração:
Na raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:
```
pip3 install -r "./requirements.txt"
```

### 2. Funcionamento:
O comando `python3 algoritmo-genetico -h` mostra como usar o pacote, como visto na seguinte saída:
```bash
Perceptron usage:

python3 algoritmo-genetico -p <pop-size> -m <mutation-rate>
```
Em que:
- `<pop-size>`: tamanho da populacao. Exemplo: `20`
- `<mutation-rate>`: taxa de mutacao. Ideal entre `0.001` e `0.01`

## Exemplo

Para determinar o custo para `<pop-size>` = 20 e `<mutation-rate>` = 0.005, use o comando:
```bash
python3 algoritmo-genetico -p 20 -m 0.005
```

O resultado a ser impresso na tela será:
```
Best: 
 [29.69143182 28.44386681] -100.74544994201688
Geracao:  280
```

**OBS.:** O resultado pode variar pois, ao executar o programa, a populacao é gerada aleatoriamente. 

## Versões do Python recomendadas

Dois computadores foram usados para rodar esse algoritmo e as versão utlizadas foram `3.7.4` e `3.9.1`.

## Análise dos resultados

