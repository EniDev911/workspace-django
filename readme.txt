## CREAR LA BASE DE DATOS:

```sql
CREATE DATABASE triviador_chile;
```

## CARGAR DATOS (opcional):

- Incluye al superadmin con las siguientes credenciales:
 - username: admin
 - password: admin


```bash
python manage.py loaddata users
python manage.py loaddata categorias
python manage.py loaddata preguntas
```

O puede ejecutar el archivo seed.sh (usando git-bash en WINDOWS):

```bash
bash seed.sh
```