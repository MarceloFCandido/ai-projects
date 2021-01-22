# Tarefa - Busca A*

**Disciplina**: Laboratório de Inteligência Artificial

**Professor**: Rogério Martins Gomes

**Alunos**:

Marcelo Lopes de Macedo Ferreira Cândido

Milena Delarete D Marques

## Objetivo

Representar o algoritmo da busca A* aplicado ao problema do metrô de Paris.

## Execução do algoritmo

### 1. Configuração:
Na raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:
```
pip3 install -r "./A*/requirements.txt"
```

### 2. Funcionamento:
O comando `python3 A* -h` mostra como usar o pacote, como visto na seguinte saída:
```
A* usage:

python A* -s <souce-station> -d <destiny-station> --heuristics=<heuristics-file> --real_distances=<distances-file>
```
Em que:
- `<source-station>`: estação inicial. Exemplo: `E6`
- `<destiny-station>`: estação de destino. Exemplo: `E13`
- `<heuristics-file>`: arquivo com os dados de distâncias diretas entre as estações de metrô.
- `<distances-file>`: arquivo os dados de distâncias reais entre as estações de metrô.

O caminho e seu custo são retornados pelo comando.

## Exemplo

Para determinar o custo para o seguinte caso:

E<sub>inicial</sub> = estação 6 linha azul

E<sub>final</sub> = estação 13 linha vermelha

use o comando:
```
python3 A* -s E6 -d E13 --heuristics="./A*/data/heuristics.csv" --real_distances="./A*/data/real-distances.csv"
```
O resultado a ser impresso na tela será:
```
E6 -> E5 -> E4 -> E13
Path length: 28.8
```


## Versões do Python recomendadas

Dois computadores foram usados para rodar esse algoritmo e as versão utlizadas foram `3.7.4` e `3.9.1`.
