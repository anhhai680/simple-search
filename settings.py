import os
import dotenv

dotenv.load_dotenv()

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false").lower() == "true"
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "default-project")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))