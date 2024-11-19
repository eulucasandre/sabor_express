import os

restaurantes = [{'nome': 'Hizaki','categoria':'Japonesa', 'ativo':False}, 
                {'nome': 'Uliveto','categoria':'Italiana', 'ativo': True}, 
                {'nome': 'Marmitex', 'categoria': 'Brasileira', 'ativo': False}]

def exibir_nome_do_programa():
      '''Exibe de maneira estilizada o nome do programa'''
      print('''
      🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​​
            ''')

def exibir_opcoes():
      '''Exibe as opções disponíveis no programa'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do restaurante')
      print('4. Sair\n')

def finalizar_app():
    '''Mostra a mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
      '''Função no qual faz o usuário retornar para o menu principal do app'''
      input('\nDigite uma tecla para voltar ao menu principal ')
      main()

def opcao_invalida():
      print('Opção Inválida!\n')
      input('Digite uma tecla para voltar ao menu principal')
      main()

def exibir_subtitulo(texto):
      os.system('clear')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      ''' Essa função é responsável por cadastrar um novo restaurante 
      Inputs:
      - Nome do restaurante 
      - Categoria
      
      Outputs:
      - Adiciona um novo restaurante a lista de restaurantes'''
      exibir_subtitulo('Cadastrar novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela'''
      exibir_subtitulo('Listando restaurantes')
      
      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      ''' Essa função é responsável por alternar o estado de cada restaurante listado '''
      exibir_subtitulo('Alternando estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
      restaurante_encontrado = False 

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                  print(mensagem)
      if not restaurante_encontrado:
            print('O restaurante não foi encontrado!')


      voltar_ao_menu_principal()


def escolher_opcoes():
      ''' Função responsável pela escolha das opções '''
      try: 
            opcao_escolhida = int(input('Escolha uma opção: '))
            print(f'Você escolheu a opção {opcao_escolhida}')

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      ''' Função principal que inicia o programa '''
      os.system('clear')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcoes()

if __name__ == '__main__':
     main()