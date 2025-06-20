from string import Template

PROMPT_TEMPLATES = {
    # Prompts common to version 1 and version 2 (English)
    "initial_petition": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "From the initial petition below, indicate the plaintiffs and defendants of the proposed action. "
        "Write a summary highlighting the facts that occurred, the legal reasons and the plaintiffs' requests.\n\n"
        "${TEXT_DOC}"
    ),
    "order_decision": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Write a summary of the decision handed down below by the judge. "
        "Use the past tense because it has already been complied with.\n\n"
        "${TEXT_DOC}"
    ),
    "contestation": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Summarize the response document below, highlighting the legal reasons and requests.\n\n"
        "${TEXT_DOC}"
    ),
    "reply": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Summarize the response document below, highlighting the legal reasons and requests.\n\n"
        "${TEXT_DOC}"
    ),
    "response": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Summarize the document below, highlighting the legal reasons and requests.\n\n"
        "${TEXT_DOC}"
    ),
    "hearing_instrument": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Summarize the hearing terms below. Indicate the names of the witnesses heard.\n\n"
        "${TEXT_DOC}"
    ),
    "memorials": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Summarize the document below, highlighting the legal reasons and requests.\n\n"
        "${TEXT_DOC}"
    ),
    "complaint": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "From the complaint below, indicate the defendants, the victims, and the date of the typical event. "
        "Make a summary highlighting the facts, the legal reasons, and the requests.\n\n"
        "${TEXT_DOC}"
    ),
    "preliminary_defense": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Make a summary of the defendant's defense described in the document below, highlighting the legal reasons and the requests.\n\n"
        "${TEXT_DOC}"
    ),
    "final_arguments": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "From the final allegations below, make a summary of the legal reasons. "
        "Also make a summary of the requests.\n\n"
        "${TEXT_DOC}"
    ),
    "other_documents": Template(
        "You are a judicial advisor specialized in analyzing procedural records. "
        "To prepare the response, consider only the text included in the prompt. "
        "Make a summary of the document below.\n\n"
        "${TEXT_DOC}"
    ),
}
