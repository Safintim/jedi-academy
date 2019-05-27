# jedi-academy

## Описание
jedi-academy - это тестовое задание от компании [БАРС Груп](https://bars.group/)

Мои комментарии по процессу выполнения [в блоге]()

Это мой первый проект на django.

## ТЗ

Создать кадровую службу ордена Джедаев:
* Нужно создать веб приложение на Django (версию можно выбрать самому), Python 2/3.
* Верстка и внешний вид системы абсолютно не важны, фокус внимания на backend части.
* Исходники нужно обязательно выложить на github.

Описание системы
Кадровая служба(далее Система) осуществляет:

*  поиск и учет кандидатов на планетах;
* отбор кандидатов по средствам вступительных испытаний;
* оповещение кандидатов о результатах вступительных испытаний и зачисление их в орден.

Система содержит сущности:

* Кандидат (Имя, Планета обитания, Возраст, Email);
* Джедай (Имя, Планета на которой он обучает);
* Планета (Наименование);
* Тестовое испытание падавана (уникальный код ордена, список вопросов);

Такие сущности как Джедай / Планета / Тестовое испытание падавана заводятся в систему через админку.

**На главной странице системы нужно отобразить выбор формы:**

(авторизацию делать не надо!)

Для Джедаев | Для кандидатов

**Если пользователь выбрал "Для кандидатов", то отобразить ему форму:**

В которой он укажет свою планету обитания, укажет свои данные и нажмет "Далее".
Мы сохраним нового кандидата в базу кандидатов.
Потом ему надо отобразить вопросы испытания, на которые он даст ответы
(список вопросов меняется время от времени, сегодня их всего три, но кто знает что будет через полгода).
(для простоты ответы можно просто сделать True/False).

**Если пользователь выбрал “Для Джедаев”, то отобразить ему форму:**

В которой он выберет себя из списка Джедаев.
Далее ему надо отобразить кандидатов, прошедших тест на его планете, но еще не ставших падаванами.
Джедай может посмотреть ответы каждого кандидата.
Если ответы кандидата устраивают джедая, он зачисляет его к себе в падаваны.
Если кандидат зачислен в падаваны, ему отправляется уведомление 
(Мы предполагаем, что в будущем уведомления могут отправляться по средствам интергалактической связи вместо
 email но это еще не точно известно, наши ученые трудятся над этим).

**Бонусная секция для продвинутых (не обязательно к выполнению):**

Ввести ограничения на количество падаванов у одного джедая (пусть будет не более 3-х);
Вывести полный список джедаев в котором для каждого джедая будет указано количество его падаванов;
Вывести всех джедаев у которых более 1-го падавана;

**Вершина крутизны для самых продвинутых:**

Загнать все это на Heroku и приложить ссылку.