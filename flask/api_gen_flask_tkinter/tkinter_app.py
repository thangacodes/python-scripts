import tkinter as tk
import requests
import json

API_URL = "http://localhost:5000/check-key"

def check_api_key():
    entered_key = key_entry.get().strip()
    if not entered_key:
        result_label.config(text="Please enter an API key.")
        return
    headers = {"Content-Type": "application/json"}
    payload = {"api_key": entered_key}
    try:
        response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
        result = response.json()
        if response.status_code == 200:
            result_label.config(fg="green", text=result['message'])
        else:
            result_label.config(fg="red", text=result.get('error', 'Unknown error'))
    except Exception as e:
        result_label.config(fg="red", text=f"Request failed: {e}")

# --- Tkinter UI ---
apipage = tk.Tk()
apipage.title("API Key Checker")

tk.Label(apipage, text="Enter API Key:",font=("Calibri",14,"bold"),bg="white",fg="black").pack(pady=5)
key_entry = tk.Entry(apipage, width=50)
key_entry.pack(pady=5)

check_btn = tk.Button(apipage, text="Check Key", font=('calibri', 12,'bold'), fg='red', bg='blue', command=check_api_key)
check_btn.pack(pady=10)

result_label = tk.Label(apipage, text="", font=("Calibri", 10))
result_label.pack(pady=10)

apipage.mainloop()
