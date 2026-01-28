import random
import time
from flask import jsonify

def chaos_mode():
    if random.choice([True, False]):
        time.sleep(2)
        return jsonify({"error": "Chaos induced failure"}), 500
