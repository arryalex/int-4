import json
import time
from rich.console import Console
console = Console()
import json,glob
from datetime import date
Consol_ =Console(color_system="256", highlight=True) 
with open('Spare(Updated).json', 'r') as f:
    data = json.load(f)

data.reverse()

reversed_data = []

for d in data:
    reversed_data.append(d)
    Consol_.print(d['logId'])
    
with open('reversed_data.json', 'w') as f:
    json.dump(reversed_data, f)

