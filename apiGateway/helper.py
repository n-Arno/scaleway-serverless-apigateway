#!/usr/bin/python3

import sys, os, requests, yaml

def get(endpoint):
    scw_url = "https://api.scaleway.com"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": os.environ.get("SCW_SECRET_KEY"),
    }
    response = requests.get(
        "/".join([scw_url, endpoint]),
        headers=headers,
    )
    if not str(response.status_code).startswith("2"):
        print(f"ERROR {response.status_code}: {response.text} on {endpoint}")
        sys.exit(1)
    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        return response.text

def load(filename):
    with open(filename, 'r') as f:
        return yaml.safe_load(f.read())

def dump(filename, content):
    with open(filename, 'w') as f:
        f.write(yaml.dump(content))

def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <service_name> <path to kong.yml>')
        sys.exit(1)
    r = get(f'functions/v1beta1/regions/fr-par/namespaces?project_id={os.environ.get("SCW_DEFAULT_PROJECT_ID")}&name={sys.argv[1]}')
    namespace_id = r["namespaces"][0]["id"]
    r = get(f'functions/v1beta1/regions/fr-par/namespaces/{namespace_id}/functions')
    fns = [ {"name": fn["name"], "url": f'https://{fn["domain_name"]}'} for fn in r["functions"]]
    k = load(sys.argv[2])
    k['services'] = fns
    dump(sys.argv[2], k)
    print("Done!")
    sys.exit(0)

if __name__ == "__main__":
    main()
