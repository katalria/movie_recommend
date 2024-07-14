from dotenv import find_dotenv, load_dotenv
import os


load_dotenv(find_dotenv())

def get_env_variable(var_name: str) -> str:
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' not found.")
    return value

OPENAI_API_KEY = get_env_variable("OPENAI_API_KEY")
