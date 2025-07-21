# Python_Projects
Python Projects
1) Se pone el archivo dist en el disco local C.
2) Una vez que este colocada se ejecuta el comando Win+R y se pone: shell:startup
3) Una vez realizado este proceso simplemente se pega el archivo archivo_progamado.bat en la direccion que se abra.
4) Se ejecuta una vez (apagando o reiniciando la PC) y se agrega los terminos y condiciones.
5) Se reinicia o apaga la pc y automaticamente ya estaria listo para usar mediante las siguientes urls:
    # Suspender y/o apagar en tiempo establecido
    5.1) http://localhost:4414/suspender?t=5
    5.2) http://localhost:4414/aapagar?t=5
    # Suspender y/o apagar en ese momento
    5.3) http://localhost:4414/suspender
    5.4) http://localhost:4414/apagar
6) Si se desea se puede reemplazar el localhost por una direccion ip puesto que el ejecutable permite el acceso interno unicamente, en futuras versiones se le podria poner conociendo su ip publica de red.