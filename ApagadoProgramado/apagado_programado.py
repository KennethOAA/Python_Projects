from flask import Flask, request
import os
import platform
import threading
import time
#localhost:4414/suspender?t=10
app = Flask(__name__)
# Ejecucion que no bloquea al principal /hilo
def ejecutar_accion(accion, delay):
    time.sleep(delay)
    if accion == "apagar":
        os.system("shutdown /s /t 0")
    elif accion == "suspender":
        os.system(r'"FILES_APAGADO\PSTools\psshutdown.exe" -d -t 0')

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

    