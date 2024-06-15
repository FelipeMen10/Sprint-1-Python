#### Nomes: Felipe Men dos Santos; Otho Oliveira Candido; Lucas Rodrigues de Queiroz; João Pedro Silva Pinheiro
#### RMs: 557571; 55054; 556323; 557013
<hr>

# Sistema de estatísticas para Corredores da Formula E

## _Objetivo:_
O nosso código pode ser usado pelos fãs e administradores das corridas da Formula E para poder se atualizar e comparar as estatísticas de corredores que foram adicionados pelo nosso sistema.

## _Funcionalidade:_
O código funciona usando funções e um tipo de menu, onde o usuário escolhe entre: 
- Adicionar Piloto
- Remover Piloto
- Listar Pilotos
- Sair
  
Este menu é controlado pela função do **Match Case** muito usada para criar esse tipo de menu. Cada opção do match case chama uma função diferente criada.

### _Adicionando um Piloto:_
Para adicionar um Piloto optamos por fazer um bom uso das listas, onde colocamos o seu nome e suas estatísticas digitadas em uma lista temporária para adiciona-lo então em uma lista final chamada **dados**, transformando-a então em uma matriz.

### _Removendo um Piloto:_
Para remover um Piloto o usuário deve apenas digitar a posição que o piloto se apresenta na lista.

### _Listando os Pilotos:_
Para listar os pilotos utilizamos a estrutura de repetição **for** duas vezes, para poder listar a matriz que contém os pilotos.

### _Dados do Piloto:_
Os dados dos pilotos são armazenados em uma lista de listas chamada de matriz, onde cada sublista contém:
- Nome do Piloto
- Melhor Tempo de Volta
- Número de Corridas Vencidas

## _Conclusão:_
Com o uso do nosso código esperamos conquistar a atenção de mais pessoas para a Formula E utilizando as estatísticas dos corredores para mostrar a habilidade deles nas corridas.

>[!NOTE]
>Se acontecer do usuário tentar usar a opção de **Remover** ou **Listar os corredores** e a lista de corredores estiver vazia, ele receberá uma mensagem de erro dizendo que nenhum corredor foi adicionado ainda.
