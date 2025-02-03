from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()  # Получение JSON данных
    print("Полученные данные: ", data)  # Вывод для отладки

    contact_by = data.get("object", {}).get("metadata", {}).get("contact_by")
    search = data.get("object", {}).get("metadata", {}).get("search")

    if contact_by and search:
        payload = {
            "contact_by": contact_by,
            "search": search,
            "variables": {
                "name": "Иванов Иван Иванович"
            }
        }
        leadteh_webhook_url = "https://rb633508.leadteh.ru/inner_webhook/5a16a581-4450-48a6-b3a0-3297001a8bb7"
        response = requests.post(leadteh_webhook_url, json=payload)

        return jsonify({"status": "success", "response_code": response.status_code})

    return jsonify({"status": "error", "message": "Required metadata missing"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
