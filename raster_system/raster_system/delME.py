from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

test = environ["TEST_VARI"]

print(test)
