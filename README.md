![base](https://github.com/user-attachments/assets/0751d497-4bd1-4654-a418-a0eda675035f)
![signup](https://github.com/user-attachments/assets/14fb21c5-1936-48f7-8c42-c580db73b88b)
![Login](https://github.com/user-attachments/assets/1cfaab1c-65c0-4168-ad43-ce06743720bd)
![Course_details](https://github.com/user-attachments/assets/766d2dd1-6eab-488e-89e1-b9cf4672187f)
![Teacher_details](https://github.com/user-attachments/assets/b2f473d5-315f-4f4e-a2e7-31506f647328)
![Add_course](https://github.com/user-attachments/assets/6c90fe56-8181-4272-8939-b653db8d089c)
# HyperSchool

Мой проект системы управления образовательными курсами на Django.

Задача была сделать простую и функциональную платформу для учебного центра.

## Основной функционал

**Курсы**: Добавление, просмотр, запись на курс. У каждого курса есть название, описание, продолжительность (в месяцах), цена и прикреплённые преподаватели.

**Пользователи:** Sign in, Login, Logout.

**Роли:**
- **Студенты:** У каждого есть профиль (имя, фамилия, возраст) и список курсов, на которые они записаны.
- **Преподаватели:** У них аналогичный профиль плюс поле «О себе».

**Навигация:** Поиск курсов по названию. Есть страницы с деталями курса и информацией о преподавателях. Есть возможность записи на курсы.

## Что использовал

**Backend:** Django 4.0.2

**База данных:** SQLite

**Инструменты:** Django Admin для администрирования, Django Forms для форм, Class-based Views, Function-based Views для представлений и стандартная система шаблонов.
