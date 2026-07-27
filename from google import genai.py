from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="hi how are you?"
)

print(interaction.output_text)
