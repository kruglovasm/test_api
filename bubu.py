import json
import csv
import requests
import argparse

def send_request(text_request, access_token, catalog_id, output_file):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    payload = {
        "modelUri": f"gpt://{catalog_id}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Заполни таблицу с указанными названиями строк или столбцов на основе текста."
            },
            {
                "role": "user",
                "text": text_request
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        res = response.json()
        print("ответ API:", json.dumps(res, indent=2, ensure_ascii=False))

        if 'result' in res and 'alternatives' in res['result'] and len(res['result']['alternatives']) > 0:
            response_text = res['result']['alternatives'][0]['message']['text']
            save_to_csv(response_text, output_file)
        else:
            print("ошибка в структуре",
                  json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("ошибка запроса")


def save_to_csv(response_text, output_file):
    rows = response_text.strip().split("\n")
    data = [row.split("|")[1:-1] for row in rows[2:] if row.strip()]

    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    print(f"Результаты сохранены {output_file}")

