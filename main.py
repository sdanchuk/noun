import gradio as gr
import spacy
import re

nlp = spacy.load('uk_core_news_sm')

def extract_nouns(text):
    """
    Функція для виділення іменників з тексту.
    """
    if not re.match("^[а-яА-ЯіІїЇєЄА-ҐҐєє.,!? ]+$", text):
        return [("Помилка: Введено недопустимі символи. Використовуйте лише літери", None)]
    
    if not text.strip():
        return [("Помилка: Текст не може бути порожнім", None)]
    
    doc = nlp(text)
    
    highlighted_text = []
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            highlighted_text.append((token.text, ""))  
        else:
            highlighted_text.append((token.text, None))  
    
    return highlighted_text

def noun_extraction_interface(text):
    """
    Інтерфейс для Gradio. Повертає текст з виділеними іменниками.
    """
    highlighted_text = extract_nouns(text)
    return highlighted_text

demo = gr.Interface(
    fn=noun_extraction_interface,
    inputs=[
        gr.Textbox(
            label="Текст українською",
            info="Введіть текст для виділення іменників",
            lines=3
        )
    ],
    outputs=gr.HighlightedText(
        label="Результат",
        combine_adjacent=False,  
        color_map={"green": "#ADD8E6"}  
    ),
    theme=gr.themes.Base(),
    title="Виділення іменників",
    description="Введіть текст українською мовою, щоб виділити всі іменники.",
    examples=[
        "Кіт гуляє в парку.",
        "Ми поїхали до Києва на канікули.",
        "Ірина купила нову книжку."
    ]
)

if __name__ == "__main__":
    demo.launch(share=True)






