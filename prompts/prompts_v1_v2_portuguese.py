from string import Template

PROMPT_TEMPLATES = {
    # Prompts common to version 1 and version 2 (Portuguese)
    "peticao_inicial": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "A partir da petição inicial abaixo indique os autores e réus da ação proposta. "
        "Faça um resumo destacando os fatos ocorridos, as razões jurídicas e os pedidos dos autores.\n\n"
        "${TEXTO_DOC}"
    ),
    "despacho_decisao": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo da decisão proferida abaixo pelo juiz. "
        "Utilize o tempo verbal no pretérito pois já houve cumprimento.\n\n"
        "${TEXTO_DOC}"
    ),
    "contestacao": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo do documento de contestação abaixo destacando as razões jurídicas e os pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "replica": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo do documento de réplica abaixo destacando as razões jurídicas e os pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "resposta": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo do documento abaixo destacando as razões jurídicas e os pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "termo_audiencia": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo do termo de audiência abaixo. Indique o nome das testemunhas ouvidas.\n\n"
        "${TEXTO_DOC}"
    ),
    "memoriais": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo do documento abaixo destacando as razões jurídicas e os pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "denuncia": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "A partir da denúncia abaixo indique os réus, as vítimas e a data do fato típico. "
        "Faça um resumo destacando os fatos, as razões jurídicas e os pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "defesa_previa": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo da defesa do réu descrita no documento abaixo, destacando as razões jurídicas e os pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "alegacoes_finais": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "A partir das alegações finais abaixo faça um resumo das razões jurídicas. "
        "Faça também um resumo dos pedidos.\n\n"
        "${TEXTO_DOC}"
    ),
    "outros_documentos": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "Faça um resumo do documento abaixo.\n\n"
        "${TEXTO_DOC}"
    ),
}
