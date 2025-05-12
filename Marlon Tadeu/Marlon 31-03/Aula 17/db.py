import mysql.connector as mysql


conn = mysql.connect(
    host='0lgu6.h.filess.io',
    port=61002,
    user='Test_complexarm',
    password='c4dbc52cf0342a89df29b701aab873bc36749c52',
    database='Test_complexarm'
)

print('Conectado com sucesso!')
