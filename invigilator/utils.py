import random
import uuid

def generate_uid():
    return str(uuid.uuid4())[:6]

