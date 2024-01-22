import subprocess
import requests
import json

def get_network_status():
    try:
        subprocess.check_output(["ping", "-c", "1", "www.baidu.com"])
        return True
    except subprocess.CalledProcessError:
        return False

def get_network_info():
    try:
        output = subprocess.check_output(["iwgetid", "-r"]).decode("utf-8").strip()
        return output
    except subprocess.CalledProcessError:
        return None

def get_ip_address():
    try:
        output = subprocess.check_output(["hostname", "-I"]).decode("utf-8").strip()
        return output
    except subprocess.CalledProcessError:
        return None

def send_message(message):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e7ede143-7d1c-4308-9af7-c8e6f7e1765e" # 王者风范-食堂阿姨
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print("消息发送失败")

network_status = get_network_status()
if network_status:
    network_info = get_network_info()
    ip_address = get_ip_address()
    message = f"已联网\n网络名称：{network_info}\nIP地址：{ip_address}"
else:
    message = "未联网"

send_message(message)
