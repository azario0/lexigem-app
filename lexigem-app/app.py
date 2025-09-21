import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv
import markdown

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Gemini API Configuration ---
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring Generative AI: {e}")
    model = None

# --- NEW: Store both English and French prompts ---
prompt_en = """
You are an expert lexicographer and usage editor. Produce a complete dictionary-style entry for the word: "{word}".
Return the following sections, labelled and in the order given:
1. **Word**: The word itself.
2. **Part of speech**: e.g., Noun, Verb, Adjective.
3. **Pronunciation**: IPA format if available (e.g., /həˈloʊ/).
4. **Concise definition**: A single, clear sentence.
5. **Expanded definition**: 2–3 sentences providing more detail and context.
6. **Common synonyms**: 3–6 relevant synonyms.
7. **Common antonyms**: If any exist. If not, state "None."
8. **Example sentences**: 3 sentences in different contexts (each ≤ 20 words).
9. **Typical register**: Formal / Neutral / Informal, plus any domain tags (e.g., Medicine, Computing).
10. **Etymology**: A brief, one-line origin of the word.

Format the entire output in Markdown. Ensure each section title is bold.
If the word is nonsensical or cannot be defined, please respond with a polite message indicating that.
"""

prompt_fr = """
Vous êtes un lexicographe et rédacteur spécialisé dans l’usage des mots. Produisez une entrée complète de style dictionnaire pour le mot : "{word}".
Retournez les sections suivantes, étiquetées et dans l’ordre indiqué :
1. **Mot**: Le mot lui-même.
2. **Partie du discours**: ex: Nom, Verbe, Adjectif.
3. **Prononciation**: API si disponible (ex: /bɔ̃.ʒuʁ/).
4. **Définition concise**: Une seule phrase claire.
5. **Définition développée**: 2–3 phrases donnant plus de détails et de contexte.
6. **Synonymes courants**: 3–6 synonymes pertinents.
7. **Antonymes courants**: S’il y en a. Sinon, indiquez "Aucun".
8. **Phrases d’exemple**: 3 phrases dans des contextes différents (chaque phrase ≤ 20 mots).
9. **Registre typique**: Formel / Neutre / Informel, et domaines d’usage (ex: médecine, droit) si pertinent.
10. **Étymologie**: Une brève origine du mot (une ligne).

Formatez la sortie complète en Markdown. Assurez-vous que chaque titre de section est en gras.
Si le mot est absurde ou ne peut être défini, veuillez répondre avec un message poli l'indiquant.
"""

# --- UPDATED: The function now accepts a language parameter ---
def get_definition(word: str, language: str = 'en') -> str:
    """Generates a dictionary entry for a given word using the Gemini API."""
    if not model:
        return "Error: The AI model is not configured. Please check the API key."

    # Choose the prompt based on the selected language
    if language == 'fr':
        prompt_template = prompt_fr
    else:
        prompt_template = prompt_en
    
    # Format the chosen prompt with the user's word
    prompt = prompt_template.format(word=word)
    
    try:
        response = model.generate_content(prompt)
        # Convert the Markdown response to HTML for rendering
        return markdown.markdown(response.text)
    except Exception as e:
        print(f"An error occurred during API call: {e}")
        return f"<p>Sorry, an error occurred while trying to generate the definition. Please try again later.</p><p><i>Error details: {e}</i></p>"

# --- UPDATED: The route now handles language selection ---
@app.route('/', methods=['GET', 'POST'])
def index():
    result_html = None
    word_of_user = ""
    selected_language = "en" # Default language
    
    if request.method == 'POST':
        word_of_user = request.form.get('word', '').strip()
        selected_language = request.form.get('language', 'en')
        
        if word_of_user:
            result_html = get_definition(word_of_user, selected_language)

    return render_template('index.html', result=result_html, word=word_of_user, selected_language=selected_language)

if __name__ == '__main__':
    app.run(debug=True)