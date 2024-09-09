from PIL import Image
from app import processor, model

def generate_instructions(image_paths, context):
    prompt = f"You are a helpful assistant to a Quality Assurance Engineer, use the given images of the software and context:{context} to generate instructions to test the software that should include following details: 1.Description of the test case 2.Preconditions 3.Step-by-step instructions 4.Expected result"

    images = [Image.open(img_path) for img_path in image_paths]

    inputs = processor(images=images, text=prompt, return_tensor="pt")
    # inputs = {k: v.to(device) for k, v in inputs.items()}

    generated_ids = model.generate(pixel_values=inputs['pixel_values'], max_new_tokens=150)

    instructions = processor.decode(generated_ids[0], skip_special_tokens=True)

    return instructions


