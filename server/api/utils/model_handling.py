from typing import Tuple
from transformers import BlipProcessor, BlipForConditionalGeneration

def load_captioning_model(model_name: str = 'Salesforce/blip-image-captioning-base') -> Tuple[BlipProcessor, BlipForConditionalGeneration]:
    """
    Loads the models used for image captioning.

    Args:
        model_name: name of the model to be loaded.

    Returns:
        Tuple[BlipProcessor, BlipForConditionalGeneration]: loaded processor and model.

    Raises:
        RuntimeError: when an error occurs while loading the model.
    """
    try:
        processor = BlipProcessor.from_pretrained(model_name)
        model = BlipForConditionalGeneration.from_pretrained(model_name)
        return processor, model
    
    except Exception as e:
        raise RuntimeError(f'Error while loading model: {e}')