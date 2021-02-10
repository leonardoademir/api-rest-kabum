### :memo: Sobre a aplicação

O KaBuM necessita realizar cotações de fretes em suas transportadoras parceiras e você, como desenvolvedor back-end, deve desenvolver uma API REST que será utilizada pelo site para a consulta de opções de transportes dos produtos. Fora utilizado o Python para desenvolvê-la, como é bem simples, foi escolhido o framework Flask para tal.

### :bookmark_tabs: **Funcionalidades**

- **Validação de altura máxima e mínima para cada opção de frete
** 
- **Gestão de capturas:** cadastrar, atualizar e listar destinatários cadastrados.
- **Validação de largura máxima e mínima para cada opção de frete**
- **Validação se o peso do produto é maior que 0.**

### :bookmark_tabs: **Rotas**
'/kabum' Passando um json em POST no seguinte formato: </br>

{
    "dimensao": {
                    "altura":100,
                    "largura":40
                },
    "peso":100
}


