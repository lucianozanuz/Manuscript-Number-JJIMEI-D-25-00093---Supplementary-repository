from string import Template

PROMPT_TEMPLATES = {
    # Prompt LLM-as-a-Judge (Portuguese)
    "llm_as_judge_pt": Template(
        "Utilizando como base o MQM Framework, avalie os textos abaixo, comparando os textos contidos nas tags <TEXTO_ALVO> com o <TEXTO_REFERENCIA>. "
        "Considere os seguintes critérios de avaliação baseados no MQM Framework. "
        "Acurácia: Problemas relacionados a quão bem o conteúdo do TEXTO_ALVO representa o conteúdo do TEXTO_REFERENCIA, considerando a terminologia (se o TEXTO_ALVO contém termos legais obrigatórios), a omissão e a inclusão de termos importantes ou obrigatórios. "
        "Verdade: Problemas relacionados a se o TEXTO_ALVO contém requisitos do Código do Processo Civil (o TEXTO_ALVO deverá conter os nomes das partes, a identificação do caso, com a suma do pedido e da contestação e o registro das principais ocorrências havidas no andamento do processo; o TEXTO_ALVO precisa conter o nomes das partes, o tipo de ação, os pedidos da inicial, os pedidos da contestação e sobre as principais ocorrências; por exemplo, no Procedimento Comum Civil deve conter as audiências e os laudos periciais). "
        "Fluência: Problemas ao estilo (o TEXTO_ALVO é formal, mas segue os princípios da linguagem simples), ortografia (o TEXTO_ALVO possui ortografia correta), gramática (o TEXTO_ALVO possui gramática correta), violações locais (o formato de datas, valores, números, telefones e endereços do TEXTO_ALVO segue o padrão local do Brasil). "
        "Retorne apenas o resumo da análise da seguinte forma, em formato JSON. "
        "Acurácia: 5 se contém problemas graves de Acurácia (Exemplo: TEXTO_ALVO não se refere ao mesmo processo judicial relatado no TEXTO_REFERENCIA); 3 se contém problemas leves de Acurácia (Exemplo: TEXTO_ALVO se refere ao mesmo processo judicial relatado no TEXTO_REFERENCIA, mas, omite termos legais obrigatórios ou inclui termos inadequados para um relatório de sentença); 0 se não contém problemas de Acurácia (Exemplo: TEXTO_ALVO se refere ao mesmo processo judicial relatado no TEXTO_REFERENCIA, não omite termos legais obrigatórios e não inclui termos inadequados para um relatório de sentença). "
        "Verdade: 5 se contém problemas graves de Verdade (Exemplo: TEXTO_ALVO não contém o nomes das partes, o tipo de ação e os pedidos da inicial e da contestação); 3 se contém problemas leves de Verdade (Exemplo: TEXTO_ALVO contém o nomes das partes, o tipo de ação e os pedidos da inicial, mas não descreve adequadamente as principais ocorrências como audiências e laudos periciais, se existirem no TEXTO_REFERENCIA); 0 se não contém problemas de Verdade (Exemplo: TEXTO_ALVO contém o nomes das partes, o tipo de ação e os pedidos da inicial, e descreve adequadamente as principais ocorrências como audiências e laudos periciais, se existirem no  TEXTO_REFERENCIA). "
        "Fluência: 5 se contém problemas graves de Fluência (Exemplo: TEXTO_ALVO contém interrupções, como divisão em seções ou subtítulos); 3 se contém problemas leves de Fluência (Exemplo: TEXTO_ALVO não contém interrupções, como divisão em seções ou subtítulos, mas não segue os princípios da linguagem simples ou possui erros de ortografia ou gramática ou o formato de datas, valores, números, telefones e endereços não segue o padrão local do Brasil); 0 se não contém problemas de Fluência (Exemplo: TEXTO_ALVO não contém interrupções, como divisão em seções ou subtítulos, segue os princípios da linguagem simples e não possui erros de ortografia e gramática e o formato de datas, valores, números, telefones e endereços segue o padrão local do Brasil).\n"
        "<TEXTO_REFERENCIA>${TEXTO_REFERENCIA}<\TEXTO_REFERENCIA>\n"
        "<TEXTO_ALVO>${TEXTO_ALVO}<\TEXTO_ALVO>"
    ),
}

