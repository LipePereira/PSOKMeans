# Otimização por Enxame de Partículas como Mecanismo de Inicialização do Método de Agrupamento K-Médias

Trabalho final de graduação do curso de Sistemas de Informação pela Universidade Federal de Itajubá.

Desenvolvido por Felipe Israel Camargo Pereira, sob orientação da Prof.ª Dr.ª Isabela Drummond.

Requisitos para execução:
- NumPy
- SciPy
- PySwarm
- MatPlotLib

A escolha da base de dados a ser analisada é feita no código dentro do arquivo kmeans.py, na função __init, na inicialização do DataReader
Os parâmetros são: DataReader("NomeDoArquivo", IgnoreStart, IgnoreEnd, "Separator"), onde:

- NomeDoArquivo é o nome do arquivo que contém os dados
- IgnoreStart é o número de colunas a serem ignoradas no inicio de cada linha (geralmente 1 que é o identificador da instância)
- IgnoreEnd é o número de colunas a serem ignoradas no fim de cada linha (geralmente 1 que é a classe da instância)
- Separator é a cadeia de caracteres que separa cada coluna de cada linha (geralmente " " ou ",")
