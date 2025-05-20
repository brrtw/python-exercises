import math

angulo = (float(input("informe um angulo: ")))
sen = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)

print("seno {:.2} coseno {:.2} tangente{:.2}".format(sen, cos, tang))