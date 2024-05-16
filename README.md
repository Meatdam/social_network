# Проект Онлайн рассылок "Social_Network"
________
В данном проекте реализована рассылка электронных писем для пользователей. 
Пользователь на сайте может заполнить форму с обратной связью. Эти данные попадают в БД, затем клиент, может создать сообщение для рассылки, с акциями например или новым поступлением. Затем он (клиент) может создать рассылку, выбрать пользователей из списка, кому бы он хотел отправить электронные письма, и создать рассылку. 
<br>Так же клиент может выбирать периодичность отправки рассылок: раз в день, раз в неделю, раз в месяц, и когда заканчивать рассылку: число, месяц, год, время.
<br>В проекте реализована регистрация , авторизация пользователя с проверкой, которая отправляет на email ссылку от нашего приложения. 

В проекте подключены:
1. Регистрация и авторизация пользователя;
2. Админ-панель для суперпользователя;
3. Профиль пользователя с возможностью менять данные, добавления аватарки и отображение товаров корзины;
4. Возможность создавать, редактировать, удалять отдельные рассылки.

Данный проект написан не фрейморке Django, с подключением реляционной базы данных "PostgreSQL"<br>
Ипользовалось вирутальное окружение ```venv```
В  проекте построенно 7 модель БД:
1. Таблица "category";
2. Таблица "Product" прямая связь с "category";
3. Таблица "Users" прямая связь с "category" и "products";
4. Таблица "Carousel" связи нет;
5. Таблица "Basket" прямая связь с "Users", "Product";
6. Таблица "Comments" прямая связь c "Users", "Product";
7. Таблица "Version" прямая связь c "Product".

Для запуска проекта необходимо сделать 
1. git clone репозитория
```
git@github.com:Meatdam/online_shop.git
```
2. Установить виртуальное окружение ```venv```
```
python3 -m venv venv
```
3. Подключить виртуальное окружение
```
source venv/bin/activate
```
4. Создать базу данных в ```PgAdmin```, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'config' в константе (словаре) 'DATABASES'
5. Обязательно установить пакет со всеми зависимостями 
```
pip install -r requirements.txt
```
6. Создать файл .env в корне проекта и заполнить следующие данные:
```
USER_DB= имя пользователя от вашей БД
PASSWORD_DB= пороль от БД
EMAIL_HOST_USER_MAIL= email адрес от которого будут приходит письма при регистрации (указать необходимо существующий адрес)
EMAIL_HOST_PASSWORD_MAIL=пороль от email (как правило на email приходит сообщение о создании проложения, и выдаст пороль, куда надо будет вставить сюда)
```

