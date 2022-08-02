from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))
# load_dotenv()
print(os.getenv('USER'))
# print(os.path.abspath(__file__))
