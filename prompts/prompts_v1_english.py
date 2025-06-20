from string import Template

PROMPT_TEMPLATES = {
    # Prompt version 1 (English)
    "judgment_report_v1_en": Template(
        "You are a judicial advisor specialized in analyzing court records. "
        "To prepare your answer, consider only the text included in the prompt. "
        "Using the data below, write a report of what happened in this case to begin a judgment.\n\n"
        "${TEXTS_PREVIOUS_INFERENCES_CONCATENATED}"
    ),
}

