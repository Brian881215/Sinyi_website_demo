

from pathlib import Path
import os 

BASE_DIR = Path(__file__).resolve().parent.parent
env_file_path = os.path.join(BASE_DIR, '.env')
env_file = Path(env_file_path)

print(BASE_DIR)
print(env_file.exists())
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('STATIC_URL'))



