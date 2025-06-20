from string import Template

PROMPT_TEMPLATES = {
    # Prompt version 1 (Portuguese)
    "relatorio_sentenca_v1_pt": Template(
        "Você é um assessor judiciário especializado em análise de autos processuais. "
        "Para elaboração da resposta considere somente o texto incluso no prompt. "
        "A partir dos dados abaixo faça o relatório do ocorrido neste processo para o início de uma sentença.\n\n"
        "${TEXTOS_INFERENCIAS_ANTERIORES_CONCATENADOS}"
    ),
}

