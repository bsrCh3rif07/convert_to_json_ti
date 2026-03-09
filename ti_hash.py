import requests
import json

URL = "https://raw.githubusercontent.com/romainmarcoux/malicious-hash/refs/heads/main/full-hash-sha256-aa.txt"
LIMITS = 500

OUTPUT_FILE = "ti_datasets_hash.json"

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to download file")
    exit()

hashes = response.text.splitlines()[:LIMITS]  # take only first 500

results = []

for h in hashes:
    h = h.strip()
    if not h:
        continue

    results.append({
        "type": "hash",
        "value": h
        #,"Threat" : call_function_virustotal(h)  # Uncomment if you want to add threat info from VirusTotal
    })

with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=4)

print(f"{len(results)} hashes saved to {OUTPUT_FILE}")