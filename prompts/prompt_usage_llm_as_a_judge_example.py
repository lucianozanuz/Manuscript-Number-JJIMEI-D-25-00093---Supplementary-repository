reference_text = "Text from a real judgment report, written by a judge..."
target_text = "Text from the judgment report generator..."
prompt = PROMPT_TEMPLATES["llm_as_judge_en"].substitute(REFERENCE_TEXT=reference_text, TARGET_TEXT=target_text)
print(prompt)
