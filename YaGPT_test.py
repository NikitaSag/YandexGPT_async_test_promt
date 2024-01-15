import requests
import json

folder_id = "b1gbj0eger88fsinb75f"
iam_token = "t1.9euelZqOz42VlcyWjJXPi5vJz4mSkO3rnpWal4uKyc3Kx4zKkM-QkZedjcrl8_cBP2xS-e99WTAM_d3z" \
            "90FtaVL5731ZMAz9zef1656VmomczMaZj8qUlZ7Pl4mekJSO7_zF656VmomczMaZj8qUlZ7Pl4mekJSO.0IQHbixv7qv1" \
            "OEJs-9pemtCXrulARbVMPpvW5qNpFuyGvETKO5Rj-YOhnm7V93H72-ApNcg75g_Ub-GjQ2_EDQ"


def send_request(folder_id, iam_token):
    with open("C:\\Users\\Zak\\AppData\\Roaming\\JetBrains\\PyCharm2021.2\\scratches\\prompt.json", encoding="utf8") \
            as json_file:
        data = json.load(json_file)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {iam_token}',
        'x-folder-id': folder_id,
    }

    response = requests.post(
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync",
        headers=headers,
        data=json.dumps(data),
    )

    data_1 = response.json()
    id_res = data_1['id']

    return id_res

