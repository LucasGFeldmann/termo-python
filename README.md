## README.md

### Termo Game

#### Arquitetura do Sistema

O Termo Game é um jogo de palavras inspirado no jogo [Termo](https://term.ooo/), onde o jogador tenta adivinhar uma palavra aleatória escolhida pelo sistema. O jogo oferece várias modalidades, incluindo o modo simplificado, dueto e quarteto.

#### Estrutura de Arquivos

O projeto é organizado em vários arquivos para facilitar a manutenção e compreensão do código:

- **file_manipulation.py**: Contém funções relacionadas à leitura e manipulação de arquivos, como a leitura de palavras do arquivo 'words_termo.txt' e funções para reiniciar o jogo.

- **game_modes.py**: Implementa as regras específicas para cada modo de jogo, incluindo o modo termo, dueto e quarteto. Também possui a função para limpar o terminal.

- **game_rules.py**: Define regras gerais do jogo, como a validação de palavras e entrada de letras.

- **menu_game.py**: Oferece uma interface de texto simples para que o jogador escolha a modalidade de jogo desejada.

- **verify.py**: Contém funções para verificar e destacar letras corretas na palavra secreta, incluindo aquelas na posição exata (verde) e na posição errada (amarelo).

#### Funcionalidades

1. **Modo Termo**:
   - O jogador tenta adivinhar uma palavra em 5 tentativas.
   - As letras corretas na posição exata são destacadas em verde.
   - As letras corretas, mas na posição errada, são destacadas em amarelo.
   - O jogador vence ao acertar a palavra.

2. **Modo Dueto**:
   - O jogador tenta adivinhar duas palavras simultaneamente em 6 tentativas.
   - A lógica é semelhante ao modo Termo, mas com duas palavras.
   - Se uma palavra é acertada, ela é removida das tentativas subsequentes.
   - O jogador vence ao acertar ambas as palavras.

3. **Modo Quarteto**:
   - O jogador tenta adivinhar quatro palavras simultaneamente em 8 tentativas.
   - A lógica é semelhante aos modos Termo e Dueto, mas com quatro palavras.
   - O jogador vence ao acertar todas as quatro palavras.

4. **Reiniciar o Jogo**:
   - A opção no menu permite reiniciar o jogo, restaurando as palavras para o estado original.

#### Funcionamento do Jogo

O jogo inicia com um menu onde o jogador pode escolher entre os modos disponíveis. Após a escolha, o jogador tenta adivinhar as palavras de acordo com as regras específicas de cada modo. O jogo destaca as letras corretas na posição exata e na posição errada para ajudar o jogador.

Ao vencer ou perder, o jogo oferece a opção de voltar ao menu principal ou reiniciar o jogo.

#### Como Executar

Certifique-se de ter o Python instalado em seu sistema. Execute o script `menu_game.py` para iniciar o jogo. Siga as instruções no terminal para escolher a modalidade e jogar.