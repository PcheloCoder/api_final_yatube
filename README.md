# Описание:
Проект «API для Yatube» - это проект по созданию API для социальной сети "Yatube", в котором реализованы такие функции как: публикация постов, коментирование постов, а так же возможность подписаться на других пользователей/авторов или от них отписаться.

Автор: Федорченко Александр
# Установка:
1. Клонировать репозиторий и перейти в него в командной строке.
2. Установите и активируйте виртуальное окружение c учетом версии Python 3.9 (выбираем python не ниже 3.9):
```
python3 -m venv venv
```
```
source venv/bin/activate
```
3. Затем нужно установить все зависимости из файла requirements.txt и выполнить миграции
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
python3 manage.py migrate
```
4. Запустить проект:
```
python3 manage.py runserver
```
# Примеры запросов к API от любого пользователя (Только GET):
* Получить список всех публикаций (GET).
```
api/v1/posts/
```
* Получить определенный пост по его {id} (GET):
```
api/v1/posts/{id}/
```
* Получить список доступных сообществ (GET):
```
api/v1/groups/ 
```
* Получить информацию о сообществе по его {id} (GET):
```
api/v1/groups/{id}/
```
* Получить все комментарии к публикации по {id} поста (GET):
```
api/v1/{post_id}/comments/
```
* Получить комментарий к публикации по его {id} (GET):
```
api/v1/{post_id}/comments/{id}/
```
# Примеры запросов к API от авторизированного пользователя:
***Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.
Пользователи могут изменять и удалять контент, автором которого они являются.***
* Создать публикацию (POST):
```
/api/v1/posts/
```
*body:*
```
{
"text": "string",
"image": "string",
"group": 0
}
```
* Изменение публикации (PUT):
```
/api/v1/posts/{id}/
```
*body:*
```
{
"text": "string",
"image": "string",
"group": 0
}
```
* Частичное изменение публикации (PATCH):
```
/api/v1/posts/{id}/
```
*body:*
```
{
"text": "string",
"image": "string",
"group": 0
}
```
* Удаление публикации (DEL):
```
/api/v1/posts/{id}/
```
