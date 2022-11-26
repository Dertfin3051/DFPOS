import requests
actual_version = requests.get("https://github.com/Dertfin3051/DFPOS/blob/d27a7e714240f34d07311ed78ec97c39fe146c07/vc.json#L1-L3")
print(actual_version.text)