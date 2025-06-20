from string import Template

PROMPT_TEMPLATES = {
    # Prompt version 2 (Portuguese)
    "relatorio_sentenca_v2_pt": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Como resposta, você deverá redigir um relatório de sentença, que é a parte inicial de uma sentença judicial. "
        "Segundo a Lei, o relatório de sentença deve conter os nomes das partes, a identificação do caso, "
        "com a suma do pedido e da contestação, e o registro das principais ocorrências havidas no andamento do processo. "
        "O formato do relatório de sentença deve seguir o modelo do EXEMPLO a seguir. "
        "<EXEMPLO>Trata-se de ação movida por NOME DA PARTE AUTORA OMITIDA contra NOME DA PARTE RÉ OMITIDA. "
        "A parte autora narra que firmou contrato de seguro com NOME DA PESSOA OMITIDA, no qual foram previstas coberturas para incêndio, "
        "explosão e danos elétricos, entre outros. Em 27/11/2021, ocorreram danos em equipamentos (ar condicionado e camara fria) devido a "
        "quedas e oscilações na rede elétrica. Após a regulamentação do sinistro, a autora indenizou o prejuízo decorrente de danos elétricos "
        "no valor de R$5.150,00, descontando o valor da franquia. A seguradora autora postula da concessionária de energia o ressarcimento do valor pago. "
        "Juntou documentos. A parte ré foi citada, apresentando contestação (evento 13, CONT1). Preliminarmente, arguiu cerceamento de defesa. "
        "Afirmou que não foi oportunizado à companhia vistoriar os equipamentos. "
        "Teceu comentários sobre a natureza da responsabilidade e sobre a falta de comprovação de danos materiais, tornando-os inexistentes. "
        "Postulou a improcedência da ação. Juntou documentos. Houve réplica (evento 16, RÉPLICA1). "
        "As partes não pediram a produção de outras provas.</EXEMPLO> "
        "Escreva o relatório de sentença considerando o texto abaixo que descreve o resumo do processo.\n\n"
        "${TEXTOS_INFERENCIAS_ANTERIORES_CONCATENADOS}"
    ),
}

