from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


def get_hf_key():
    HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

    if not HF_TOKEN:
        raise ValueError(
            "HUGGINGFACE_API_KEY not found.\n"
            "→ Copy .env.example to .env\n"
            "→ Add your HuggingFace API key"
        )

    return HF_TOKEN

if __name__ == "__main__":
    print(get_hf_key())