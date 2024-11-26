# **Sabor Express 🍴**

Este é um programa interativo em Python para gerenciar uma lista de restaurantes. Ele permite cadastrar, listar e alterar o estado de restaurantes de forma simples, utilizando o terminal.

---

## **📋 Funcionalidades**
- Exibir o nome estilizado do programa.
- Menu interativo com opções de:
  - **Cadastrar Restaurante**: Adicionar novos restaurantes à lista.
  - **Listar Restaurantes**: Veja os restaurantes cadastrados com nome, categoria e status.
  - **Alternar Estado**: Ativar ou desativar um restaurante.
  - **Sair**: Finalizar o programa.

---

## **📂 Estrutura do Código**

### **1. Organização Modular**
O programa é dividido em funções específicas, como:
- `cadastrar_novo_restaurante()`: Adiciona um novo restaurante.
- `listar_restaurantes()`: Exibe os restaurantes cadastrados.
- `alternar_estado_restaurante()`: Alterna o estado de ativação dos restaurantes.
- `main()`: Função principal que inicializa o programa.

### **2. Lista de Dicionários**
Os restaurantes são armazenados como uma lista de dicionários:
```python
restaurantes = [{'nome': 'Hizaki','categoria':'Japonesa', 'ativo':False}, ...]
```

### **3. Funcionalidades Adicionais**
- Uso do módulo `os` para limpar a tela com `os.system('clear')`.
- Tratamento de exceções para entradas inválidas com `try-except`.

---

## **🛠️ Tecnologias Utilizadas**
- **Python 3.9+**
  - Manipulação de listas e dicionários.
  - Entrada/saída via terminal.
  - Módulo `os` para interação com o sistema operacional.

---

## **📖 Documentação das Funções**

### `exibir_nome_do_programa()`
Exibe o nome do programa de forma estilizada no terminal.

### `exibir_opcoes()`
Mostra as opções do menu interativo.

### `cadastrar_novo_restaurante()`
- **Entrada:** Nome e categoria do restaurante.
- **Saída:** Adiciona um novo restaurante à lista e exibe uma mensagem de sucesso.

### `listar_restaurantes()`
- **Saída:** Exibe os restaurantes cadastrados com nome, categoria e estado (ativado/desativado).

### `alternar_estado_restaurante()`
- **Entrada:** Nome do restaurante.
- **Saída:** Alterna o estado (ativado/desativado) do restaurante correspondente.

### `escolher_opcoes()`
Gerencia a escolha de opções pelo usuário e redireciona para as funções correspondentes.

### `voltar_ao_menu_principal()`
Retorna ao menu principal após a execução de uma funcionalidade.

---

## **💡 Pontos de Melhoria**
- **Persistência de Dados:** Usar arquivos (ex.: JSON) ou banco de dados para salvar os restaurantes.
- **Compatibilidade:** Substituir `os.system('clear')` por uma solução multiplataforma (visto que o sistema utilizado para a elaboração deste projeto foi o Linux Ubuntu).
- **Validação de Entradas:** Garantir que nomes e categorias não sejam deixados em branco.

---

## **🚀 Como Executar**
1. Certifique-se de ter o Python 3.9 ou superior instalado.
2. Clone ou baixe o repositório.
3. Execute o programa no terminal:
   ```bash
   python nome_do_arquivo.py
   ```
4. Siga as instruções no menu interativo.

---

## **🔧 Exemplos de Uso**

### **Cadastrar Restaurante**
```
Escolha uma opção: 1
Digite o nome do restaurante que deseja cadastrar: Marmitex da Maria
Digite o nome da categoria do restaurante Marmitex da Maria: Brasileira
O restaurante Marmitex da Maria foi cadastrado com sucesso!
```

### **Listar Restaurantes**
```
Escolha uma opção: 2
Nome do restaurante       | Categoria           | Status
- Hizaki                  | Japonesa           | desativado
- Uliveto                 | Italiana           | ativado
```

### **Alternar Estado**
```
Escolha uma opção: 3
Digite o nome do restaurante que deseja alternar o estado: Uliveto
O restaurante Uliveto foi desativado com sucesso!
```

---

## **📄 Licença**
Este projeto é livre para uso e modificação. Sinta-se à vontade para contribuir! 😊

---
