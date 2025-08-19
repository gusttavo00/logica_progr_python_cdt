from datetime import datetime, timedelta

def hoje():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def amanha():
    return (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S")
