import requests

def getRepositories(url):
    r = requests.get(url)
    print("Kod stanu:", r.status_code)
    response_dict = r.json()
    print(response_dict.keys())
    print("Całkowita liczba repozytoriów: ", response_dict['total_count'])
    return response_dict


def showKeys(repo_dicts):
    repo_dict_1 = repo_dicts[0]
    print("\nKlucze: ", len(repo_dict_1))
    for key in sorted(repo_dict_1.keys()):
        print(key)
