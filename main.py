import requests
import json
from YaGPT_test import send_request
import time

folder_id = "b1gbj0eger88fsinb75f"
iam_token = "t1.9euelZqOz42VlcyWjJXPi5vJz4mSkO3rnpWal4uKyc3Kx4zKkM-QkZedjcrl8_cBP2xS-e99WTAM_d3z" \
            "90FtaVL5731ZMAz9zef1656VmomczMaZj8qUlZ7Pl4mekJSO7_zF656VmomczMaZj8qUlZ7Pl4mekJSO.0IQHbixv7qv1" \
            "OEJs-9pemtCXrulARbVMPpvW5qNpFuyGvETKO5Rj-YOhnm7V93H72-ApNcg75g_Ub-GjQ2_EDQ"


def prompt_result(folder_id, iam_token):
    data = send_request(folder_id, iam_token)
    time.sleep(10)
    headers = {
        "Authorization": f"Bearer {iam_token}"
    }

    url = "https://llm.api.cloud.yandex.net/operations/"+str(data)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print('Ошибка:', response.status_code, response.reason)


if __name__ == "__main__":
    prompt_result(folder_id, iam_token)
