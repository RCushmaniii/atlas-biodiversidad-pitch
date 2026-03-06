"""
BioJalisco Species Identifier
Uses GPT-4o vision to identify species from photos.
"""
import os
import base64
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

app = Flask(__name__, static_folder='static')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a world-class field biologist and taxonomist working for BioJalisco, 
a biodiversity atlas project in Jalisco, Mexico. When shown a photo, identify the species with 
scientific precision but communicate in an engaging, accessible way.

You identify ALL living organisms — wild and domestic. For domestic animals like dogs, identify 
the specific breed (or mix). For cats, identify the breed. For garden plants, houseplants, 
livestock, pet birds, aquarium fish — identify them all with the same enthusiasm and detail. 
Every species has a story worth telling, whether it's a wild jaguar or a beloved family pet.

For dogs, always include breed-specific traits, temperament, and origin history in the description.
For mixed breeds, describe the likely mix and characteristics of each contributing breed.

Respond in this exact JSON format:
{
  "common_name": "Common name or breed (English)",
  "nombre_comun": "Nombre común o raza (Spanish)",
  "scientific_name": "Genus species (or subspecies/breed for domestics, e.g. Canis lupus familiaris)",
  "family": "Family name",
  "breed": "Specific breed name if domestic animal, otherwise null",
  "confidence": "high|medium|low",
  "description": "2-3 sentence description — for domestic animals include breed traits, temperament, origin.",
  "descripcion": "Same description in Spanish.",
  "conservation_status": "IUCN status if known. For domestic breeds, use 'Domesticated' or note if rare breed.",
  "found_in_jalisco": true/false or "unknown",
  "fun_fact": "One surprising or delightful fact about this species or breed."
}

If the image doesn't contain a clearly identifiable organism, respond with:
{
  "error": "Brief explanation of why identification isn't possible.",
  "suggestion": "Tip for getting a better photo."
}

Always respond with valid JSON only, no markdown formatting."""


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/identify', methods=['POST'])
def identify():
    if 'image' not in request.files and 'image_data' not in request.json if request.is_json else True:
        return jsonify({"error": "No image provided"}), 400

    # Handle base64 image from camera capture
    if request.is_json and 'image_data' in request.json:
        image_data = request.json['image_data']
        # Strip data URI prefix if present
        if ',' in image_data:
            image_data = image_data.split(',', 1)[1]
        image_b64 = image_data
        media_type = "image/jpeg"
    else:
        # Handle file upload
        file = request.files['image']
        image_bytes = file.read()
        image_b64 = base64.b64encode(image_bytes).decode('utf-8')
        media_type = file.content_type or "image/jpeg"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Identify the species in this photo."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{media_type};base64,{image_b64}",
                                "detail": "high"
                            }
                        }
                    ]
                }
            ],
            max_tokens=800,
            temperature=0.3
        )

        result_text = response.choices[0].message.content.strip()
        # Clean up potential markdown code fences
        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1] if '\n' in result_text else result_text[3:]
            if result_text.endswith('```'):
                result_text = result_text[:-3]
            result_text = result_text.strip()

        import json
        result = json.loads(result_text)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('SPECIES_ID_PORT', 5050))
    print(f"\n  🔬 BioJalisco Species Identifier running at http://localhost:{port}\n")
    app.run(host='0.0.0.0', port=port, debug=True)
