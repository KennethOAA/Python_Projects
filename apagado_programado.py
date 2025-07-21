from flask import Flask, request
import os
import platform
import threading
import time

app = Flask(__name__)
# Ejecucion que no bloquea al principal /hilo
def ejecutar_accion(accion, delay):
    time.sleep(delay)
    sistema = platform.system()

    if accion == "apagar":
        if sistema == "Windows":
            os.system("shutdown /s /t 0")
        elif sistema == "Linux":
            os.system("shutdown now")
        elif sistema == "Darwin":
            os.system("sudo shutdown -h now")
    elif accion == "suspender":
        if sistema == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif sistema == "Linux":
            os.system("systemctl suspend")
        elif sistema == "Darwin":
            os.system("pmset sleepnow")

@app.route("/apagar")
def apagar():
    delay = int(request.args.get("t", 0))  # Ej: /apagar?t=45
    threading.Thread(target=ejecutar_accion, args=("apagar", delay)).start()
    return f"Apagado programado en {delay} segundos"

@app.route("/suspender")
def suspender():
    delay = int(request.args.get("t", 0))
    threading.Thread(target=ejecutar_accion, args=("suspender", delay)).start()
    return f"Suspensión programada en {delay} segundos"

if __name__ == "__main__":
    app.run(port=4414)
