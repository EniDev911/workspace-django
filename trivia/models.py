from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

class Pregunta(models.Model):
    pregunta = models.TextField()
    resp_correcta = models.TextField(null=False)
    resp_incorrecta1 = models.CharField(max_length=45, null=False)
    resp_incorrecta2 = models.CharField(max_length=45,  null=False)
    resp_incorrecta3 = models.CharField(max_length=45,  null=False)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Respuesta(models.Model):
    respuesta = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Resultado(models.Model):
    puntaje = models.IntegerField(default=0)
    fecha = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Like(models.Model):
    resultado_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resultados")
