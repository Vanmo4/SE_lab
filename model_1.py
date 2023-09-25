from transformers import pipeline

transl = pipeline("translation", "Helsinki-NLP/opus-mt-ru-en")

transl("Я пробую что-то новое для себя")
