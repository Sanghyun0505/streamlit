from openai import OpenAI
import textwrap
# import requests
# from IPython.display import Image, display

def translate_text_for_image(text):
    client = OpenAI(
        api_key = "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",
    )

    user_content = text
    messages = [{"role": "user", "content": user_content}]
    
    response = client.chat.completions.create(
        model = "gpt-4-turbo-2024-04-09",
        messages = messages,
        max_tokens = 1000,
        temperature = 0.8,
        n = 1
    )

    assistant_reply = response.choices[0].message.content

    return assistant_reply

def generate_text_for_image(text):
    client = OpenAI(
        api_key = "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",
    )

    user_content = text

    messages = [{"role": "user", "content": user_content}]

    response = client.chat.completions.create(
        model = "gpt-4-turbo-2024-04-09",
        messages = messages,
        max_tokens = 1000,
        temperature = 0.8,
        n = 1
    )

    assistant_reply = response.choices[0].message.content

    return assistant_reply
    
def generate_image_from_text(text_for_image, image_num = 1, image_size = "512x512"):
    client = OpenAI(
        api_key = "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",
    )

    shorten_text_for_image = textwrap.shorten(text_for_image, 1000)

    response = client.images.generate(prompt = shorten_text_for_image, n = image_num, size = image_size)

    image_urls = []

    for data in response.data:
        image_url = data.url
        image_urls.append(image_url)

    return image_urls
