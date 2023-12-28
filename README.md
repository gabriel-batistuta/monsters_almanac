## Comandos pra rodar:
- cria todo o ecossistema básico do framework 
```shell
django-admin startproject [nome-do-projeto]
```

- Executa o servidor local
```bash
python manage.py runserver
```

- cria um app django no sistema, um produto de loja pode ser um app
```shell
python manage.py startapp
```

- cria um admin no sistema
```shell
python manage.py createsuperuser
```

- cria os códigos sql das mudanças do sistema
```shell
python manage.py makemigrations
```

- executa os códigos sql criados pelo makemigration
```shell
python manage.py migrate
```