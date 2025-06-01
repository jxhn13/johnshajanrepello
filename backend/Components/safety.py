import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")

def is_safe_output(text, threshold=0.6):
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            scores = F.softmax(outputs.logits, dim=1)
            toxicity_score = scores[0][1].item()
        if toxicity_score >= threshold:
            logger.warning(f"Output flagged as unsafe with toxicity score {toxicity_score:.3f}")
        return toxicity_score < threshold
    except Exception as e:
        logger.error(f"Error during toxicity check: {e}")
        return False
