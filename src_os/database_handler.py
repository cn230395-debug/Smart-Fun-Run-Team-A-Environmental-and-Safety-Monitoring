import os
import openpyxl
from datetime import datetime

EXCEL_FILE = "environment_log.xlsx"

def initialize_excel():
    if not os.path.exists(EXCEL_FILE):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Environmental Monitoring"

        headers = ["Timestamp", "Temperature (°C)", "Humidity (%)", "Status"]
        ws.append(headers)

        wb.save(EXCEL_FILE)

def save_to_excel(temperature, humidity):

    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active

    # Simple safety status
    if temperature > 35:
        status = "Critical"
    elif temperature > 30:
        status = "Warning"
    else:
        status = "Safe"

    ws.append([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        temperature,
        humidity,
        status
    ])

    wb.save(EXCEL_FILE)
