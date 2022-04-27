
import random
import re

# ¿Quién comienza?
#seleccion aleatora de las preguntas
file=open('.\Ficheros\pregunta.txt','r',encoding='utf8')

lvl1 = random.randint(0, 4)
lvl2 = random.randint(5, 9)
lvl3 = random.randint(10, 14)
lvl4 = random.randint(15, 19)
lvl5 = random.randint(20, 24)

question=list()
ans=list()
res=list()
for line in file:
    line = line.rstrip()
    question.append(re.findall('[0-9].+\?', line))
    ans.append(re.findall(';a.+\;',line))
    

preguntas=[question[lvl1],question[lvl2],question[lvl3],question[lvl4],question[lvl5]]# 5 preguntas de diferente nivel

ans=[ans[lvl1],ans[lvl2],ans[lvl3],ans[lvl4],ans[lvl5]] # 4 opciones de respuesta

res=str(ans)
res=res.split(';')# separacion 
pre=str(preguntas)
pre=pre.split("'")
#print(res[7])

