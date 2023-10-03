Feature: Realizar uma busca no site blogdoagi.com.br
    

  Scenario Outline: Realizar uma busca válida com resultados
    Given que estou na página inicial "https://blogdoagi.com.br/"
    When eu busco por "<query>"
    Then aparece escrito "<query>" em Resultados da busca por:
    And eu encontro "<query>" no titulo, no sub-titulo ou na noticia

    Examples:
      | query                          |
      | chatbot                        |
      | 2023                           |
      | a.base@agi.com.br              |
      | de Sean Ellis e Morgan Brown   |

  Scenario Outline: Realizar uma busca válida sem resultados
    Given que estou na página inicial "https://blogdoagi.com.br/"
    When eu busco por "<query>"
    Then aparece escrito "Nenhum resultado" no header:
    And aparece a mensagem: "Não encontramos nada para estes termos de busca. Tente novamente com palavras-chave diferentes."

    Examples:
      | query          |
      | banana         |
