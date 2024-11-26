# sabor_express
Projeto elaborado durante o curso de ''Python: crie sua primeira aplicação'' da Alura, utilizando conceitos básicos da linguagem de programação.

**1. Estrutura do Programa**
Arquitetura Modular
O código utiliza funções para encapsular comportamentos específicos, como exibir menus, cadastrar restaurantes ou alternar estados. Isso promove organização e reusabilidade.

Execução Condicional
A linha if __name__ == '__main__': define o ponto de entrada do programa, garantindo que a função main() seja executada apenas quando o arquivo for executado diretamente, e não quando importado como módulo.

**2. Manipulação de Dados**
Lista de Dicionários
Os restaurantes são armazenados como uma lista de dicionários, onde cada dicionário contém as informações de um restaurante:

restaurantes = [{'nome': 'Hizaki','categoria':'Japonesa', 'ativo':False}, ...]
Isso facilita a organização e o acesso aos dados usando chaves, como restaurante['nome'].

Métodos de Lista
append: Adiciona um novo restaurante à lista.
Iteração com for: Usada para percorrer os elementos da lista e processá-los.

**3. Estruturas de Controle**
Condições e Loops
Condicionais if-elif-else são usadas para determinar a ação baseada na opção escolhida pelo usuário.
for é usado para iterar pelos elementos da lista e verificar ou alterar estados.
Tratamento de Exceções
A função escolher_opcoes() utiliza um bloco try-except para capturar erros, como entrada de valores inválidos, evitando que o programa seja encerrado abruptamente.

**4. Interação com o Usuário**
Entrada e Saída de Dados
Funções como input permitem que o usuário insira informações.
print exibe mensagens, menus e resultados no console.
Interface Simples
O programa exibe menus com opções numeradas e solicita ações ao usuário, facilitando a navegação.

**5. Organização do Código**
Docstrings
As funções possuem docstrings (comentários de documentação), explicando seus propósitos, entradas e saídas. Por exemplo:

'''Exibe as opções disponíveis no programa'''
Funções Utilitárias
Algumas funções, como exibir_subtitulo, melhoram a organização e a estética do programa, tornando o código mais legível e o menu mais amigável.

**6. Sistema Operacional**
Uso do Módulo os
O programa usa os.system('clear') para limpar a tela, criando uma experiência mais fluida ao usuário. Este comando é específico para sistemas baseados em UNIX (Linux/MacOS) e pode precisar de ajustes para Windows (ex.: os.system('cls')).

**7. Boas Práticas no Código**
Clareza
Os nomes das funções são descritivos e autoexplicativos, facilitando a leitura e manutenção.

Modularidade
Cada funcionalidade é isolada em sua própria função, o que torna o código mais fácil de depurar e expandir.

**8. Pontos de Melhoria**
Validação de Entradas: Adicionar verificações para garantir que o usuário insira dados válidos.
Persistência de Dados: Incorporar um sistema de armazenamento (ex.: arquivo ou banco de dados) para salvar os restaurantes entre execuções.
Compatibilidade de Sistema: Substituir os.system('clear') por uma solução multiplataforma.

**Como Executar?**
Certifique-se de ter o Python instalado.
- Execute o programa no terminal: python nome_do_arquivo.py
- Siga as instruções exibidas no menu interativo.
