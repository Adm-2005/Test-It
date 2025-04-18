# external imports
import torch
import requests
from PIL import Image
from typing import Tuple, List
from transformers import BlipProcessor, BlipForConditionalGeneration

def request_groq(prompt: str, groq_api_key: str) -> str:
    """
    Sends a request to groq api with the given prompt.

    Args:
        prompt: prompt to be given to the model.
        groq_api_key: groq api key.

    Returns:
        str: generated response.
    """
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a professional QA Engineer."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1024
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )
    return response.json()["choices"][0]["message"]["content"]

def gen_response_for_img(
    image_paths: List[str], 
    name: str, 
    scope: str,
    processor: BlipProcessor,
    model: BlipForConditionalGeneration,
    hf_token: str,
    groq_api_key: str,
) -> str:
    """
    Captions the images, embeds them in the prompt and passes prompt to the LLM for generating response.

    Args:
        image_paths: list of image paths.
        name: name of the component to be tested.
        scope: scope of the component to be tested.
        processor: blip processor.
        model: blip model.
        hf_token: Huggingface token.
        groq_api_key: API key for Groq.

    Returns:
        str: generated response from the model.
    """
    captions = []
    for img_path in image_paths:
        text = 'photograph of a software component'
        raw_img = Image.open(img_path, 'r')

        inputs = processor(raw_img, text, return_tensors='pt') 
        output = model.generate(**inputs)

        generated_caption = processor.decode(output[0], skip_special_tokens=True)
        captions.append(generated_caption)

    prompt = f"""
    Your task is to generate detailed testing instructions for a software component based on its visual layout and purpose.

    Component Name: {name}
    Scope of Testing: {scope}

    Here are the image captions generated using a visual model that describe different aspects of this component:

    {chr(10).join([f"- {cap}" for cap in captions])}

    Based on the above, write a step-by-step list of QA testing instructions, covering UI, UX, and any visible functionalities. The instructions should be structured, specific, and relevant to the described interface. Consider usability, responsiveness, accessibility, and error handling.
    """
    response = request_groq(prompt, groq_api_key)
    return response
    
def gen_response_for_code(
    code: str, 
    name: str, 
    scope: str,
    groq_api_key: str
) -> str:
    """
    Embeds the provided information in the prompt and passes it to the LLM for generating response.
    
    Args:
        code: code to generate test cases for.
        name: name of the component to be tested.
        scope: scope of the component to be tested.
        groq_api_key: groq api key.

    Returns:
        str: generated response from the model.
    """
    prompt = f"""
    Based on the following component code, generate detailed and well-structured test cases.

    Component Name: {name}
    Scope of Testing: {scope}

    Code:
    ```python
    {code}
    """
    response = request_groq(prompt, groq_api_key)
    return response