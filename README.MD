# Projeto de Desenvolvimento

## Requisitos e Introdução:

- Python

Neste desafio iremos desenvolver uma aplicação para estudo de python e de ferramentas de controle de versão, mais precisamente o github


## Expectativas

- Simplicidade: espera-se da solução um projeto pequeno e de fácil entendimento;
- Elegância: espera-se da solução facilidade de manutenção,uma separação clara das responsabilidades e uma estrutura de código bem organizada.
- Operacional: espera-se da solução a resolução do problema.
- Organização: espera-se da solução esteja bem estruturada e organizada no github

___

## Projeto

Usando a api publica de pokemon disponível em [API](https://pokeapi.co/api/v2/), sua solução deve retornar, para um determinado conjunto de entrada qual a melhor rota baseado na chance de encontro, separadas por região, para encontrar os pokemons para meu time. 
Todas as variaveis, entradas e retornos devem estar em inglês. 


*Este é so um exemplo de entrada e saida, os valores não estão corretos. Apenas para demonstração de estrutura*

### Entrada
```json
{
    "pokémons":["butterfree"],
    "regions":["Jhoto","Kanto"],
}
```

### Retorno

```json
{
    "Butterfree":{
        "Jhoto":["ilex-forest-area"],
        "Kanto":[...] 
    }
}

```

--- 

## Documentação e Links importantes

- VsCode: https://code.visualstudio.com
- Pokemon API: https://pokeapi.co/docs/v2
- Python: https://docs.python.org/3/
- Git: https://rogerdudler.github.io/git-guide/index.pt_BR.html
- Requests: https://docs.python-requests.org/en/master/
- Python Basic: https://www.youtube.com/watch?v=kqtD5dpn9C8 (1hr)
- Font Legal pro VSCoe: https://github.com/tonsky/FiraCode
- Python in vsCode: https://code.visualstudio.com/docs/languages/python
___

## Controle de versão

Crie um repo no github, e trabalhe usando commits granulares e branchs separadas para cada funcionalidade, realizando pull requests quando necessário. Lembre-se de realizar commits com mensagens sucintas e em inglês

Qualquer duvida referente a codigo e/ou syntaxe pesquise no google/stackoverflow.
Duvidas sobre o projeto: robert.cristian@live.com ou no Whatsapp.

___

## Extras
Como opcionais, podemos incrementar o retorno da nossa aplicação, trazendo informações extras:

- menor e maior level de encontro (*)
- status (*)
- tipos (*)
- tamanho (*)
- Lendario/Mitico (**)
- Habitat (**)
- Cadeia evolutiva (***)
- Implementações criativas

### Retorno com + dados
```json
{
    "Butterfree":{
        "Regions":{
            "Jhoto":["ilex-forest-area"],
            "Kanto":[...] 
        },
        "Status":{
            "hp": 20,
            "def": 5,
            ...
        },
        "Types":["grama","lutador"]
    }
}


```