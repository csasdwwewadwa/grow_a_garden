import requests

from data import DISCORD_USERID, DISCORD_PING, DISCORD_WEBHOOK_URL, DETAILED_REPORT


def send_discord_message(content, webhook_url):
    payload = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code != 204 and response.status_code != 200:
        print(f"Failed to send message: {response.status_code} - {response.text}")


def report(msg, is_ping=False):
    content = msg
    if is_ping:
        content += f' {DISCORD_PING}'
    send_discord_message(content, DISCORD_WEBHOOK_URL)


def detailed_report(msg):
    if DETAILED_REPORT:
        report('-# ' + msg)
        