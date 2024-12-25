# Samokat
Перед запуском тестов необходимо установить пакет pytest и requests
# <a name="up" />Проект Яндекс Самокат

Яндекс Самокат - это сервис, который позволяет арендовать электрический самокат на несколько дней.  
У сервиса есть веб-приложение, мобильное приложение и API.
В веб-приложении пользователь может оформить заказ на самокат и посмотреть статус доставки курьером.
В мобильном приложении курьер отслеживает и выполняет заказы по доставке самокатов.
Документация API доступна после запуска стенда (сервера)

## Содержание
- [Задачи](#задачи-тестировщика)
- [Требования по проекту](#требования-по-проекту)
- [Инструменты](#инструменты)
- 
## Задачи

1. Автоматизировать сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.

***

2. Работа с базой данных
Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.
Технические примечания:
Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.
***

## Требования

<details>
<summary> Требования к веб-приложению </summary> 

### Поддерживаемые окружения  
Приложение поддерживает эти браузеры: Яндекс.Браузер не ниже версии 20.0.1, Chrome не ниже версии 85. Будет поддерживаться разрешение экрана 1280x720 и 1920x1080.  

### Лендинг
Есть заголовок и чертёж самоката. При скролле происходит анимация: чертёж сменяется фотографией, появляется таблица с описанием самоката.  
В шапке лендинга есть две кнопки: «Заказать», «Статус заказа».   
Появляется запрос на согласие использовать куки.   
Если доскроллить до третьего блока, появляется информация: «Как это работает», «Вопросы о важном».  

#### Экран «Сделать заказ»  
Чтобы сделать заказ, нужно заполнить две формы: «Для кого самокат», «Про аренду».  

**Для кого самокат**
Поля: «Имя», «Фамилия», «Адрес: куда привезти самокат», «Станция метро», «Телефон: на него позвонит курьер».  
Все поля обязательные. Если они не заполнены корректно, нельзя перейти на следующую страницу.  
Внизу кнопка «Дальше»: она переводит на форму «Про аренду».   

**Про аренду**
Поля: «Когда привезти самокат», «Срок аренды», «Цвет», «Комментарий».   
«Когда привезти самокат», «Срок аренды» — обязательные поля.   
«Цвет», «Комментарий» — необязательные.  

**Кнопка «Назад».** При нажатии пользователь переходит на страницу «Для кого самокат».  При переключении между страницами введённая информация сохраняется.  

**Кнопка «Заказать».** Если все поля заполнены корректно, при клике по кнопке «Заказать» заказ будет оформлен. Появится всплывающее окно с текстом «Номер заказа NNNNN.   Запишите его: пригодится, чтобы отслеживать статус» и кнопкой «Посмотреть статус». Кнопка «Посмотреть статус» ведёт на экран «Статус заказа»: в нём уже заполнено поле «Номер заказа».  
Если не все обязательные поля заполнены корректно, при нажатии на кнопку «Заказать» появится ошибка «Введите корректный <имя поля>»  
Пользователь может сделать несколько заказов один за другим.  

#### Экран «Статус заказа»
Если нажать на «Статус заказа» в шапке лендинга, появляется поле ввода «Номер заказа». Нужно ввести значение и нажать Enter. Если номер заказа введён корректно, появляется информация:  
- Данные заказа пользователя: имя, фамилия, адрес и остальные. Для всех полей действует правило: если текст не умещается в одной строке, он переносится на вторую.  
- Цепочка статусов заказа. Текущий статус выделен чёрным, остальные — серые. Если статус пройден, цифра перед ним сменяется на галочку.  
Если номер заказа введён некорректно, появляется сообщение об ошибке: «Такого заказа нет. Точно верный номер?».  
На экране статуса заказа четыре статуса. Активным может быть только один из них — он показывает, на какой стадии находится заказ:     
- **«Самокат на складе»**. Становится активным, когда пользователь сделал заказ.  
- **«Курьер едет к вам»**. Становится активным, когда курьер подтвердил у себя в приложении, что принял заказ. Когда статус активен, в подписи появляется имя курьера: «Курьер Фродо едет к вам». Если имя курьера слишком длинное и подпись не умещается в одну строчку, текст переносится на вторую строчку.  
- **«Курьер на месте»**. Становится активным, когда курьер нажал кнопку «Завершить» у себя в приложении.  
- **«Ну всё, теперь кататься»**. Становится активным, когда курьер подтвердил завершение заказа. Под заголовком статуса подпись «Аренда закончится...». Показываемое время рассчитывается от момента, когда самокат передали пользователю с учётом количества дней. Когда время аренды заканчивается, статус меняется на «Время аренды кончилось» с подписью «Скоро курьер заберёт самокат».  
Пользователь может ввести номер другого заказа и посмотреть его статус.  

**Отмена заказа**
Есть кнопка «Отменить заказ». Если кликнуть по ней, появится всплывающее окно с текстом «Хотите отменить заказ?» На всплывающем окне две кнопки: «Отменить», «Назад». 
Если кликнуть по «Назад», пользователь вернётся на страницу статуса заказа.   
Если кликнуть по «Отменить», появится всплывающее окно с текстом «Заказ отменён. Возвращайтесь, мы всегда вас ждём :)» и кнопкой «Хорошо». Кнопка «Хорошо» ведёт на главную страницу лендинга.  
Пользователь может отменить заказ, пока курьер не взял его в работу. Когда заказ уже у курьера, кнопка «Отменить заказ» будет некликабельной.  
Отменённый заказ удаляется из системы. Пользователь не может его посмотреть.  

**Просроченный заказ**
Заказ считается просроченным, если курьер не успел выполнить его вовремя. Например, пользователь заказал самокат на 1 января. Если 1 января самокат не доставлен до 23:59, этот заказ — просроченный.  
Если заказ просрочен, его статус меняется на «Курьер задерживается», а подпись — на «Не успеем привезти самокат вовремя. Чтобы уточнить статус заказа, позвоните в поддержку: 0101». Статус и подпись подсвечиваются красным.  
Если пользователю доставили просроченный заказ, отсчёт времени до конца аренды начинается с момента получения заказа.  

### Доработка фронтенда
В цепочку статусов добавлен пятый статус: «Время аренды кончилось»**.** Это фича, которую реализовали только во фронтенде, и бэкенд ещё не готов. ****Раньше этот текст появлялся на месте четвёртого статуса — в момент, когда время аренды заканчивалось. Теперь текст в четвёртом статусе не меняется: он просто становится серым, как и остальные статусы.  
Пример ответа описан в документации к API в блоке *Orders — Получить заказ по его номеру.*  
Номер нового статуса в запросе = 3.  

<summary> Требования к мобильному приложению </summary> 

## Экран «Вход»  
1. При первом входе в приложение появляется экран авторизации с логином и паролем.    
2. Если курьер уже авторизовался, он видит экран списка заказов по умолчанию.  
3. На экране два поля ввода: под логин и пароль. Есть кнопка «Войти».  
4. Если тапнуть по «Не помню пароль», появится уведомление с текстом «Свяжитесь с менеджером: 0101» и кнопка «Ок».  
5. Пользователь может выйти из приложения с любого экрана. Тогда при входе он снова попадёт на экран авторизации.  

## Экран «Список заказов»  
На экране две вкладки: «Все», «Мои».   
На вкладке «Все» курьеры видят один и тот же список заказов: это заказы без исполнителей.   
Как только один из курьеров принимает заказ, он перемещается во вкладку «Мои». Остальные курьеры перестают его видеть.  
Внутри вкладки «Мои» курьер видит заказы, которые он принял.   
Чтобы список обновился, нужно потянуть за экран вниз (англ. pull-to-refresh).   
При pull-to-refresh:  
1. Для вкладки «Все»: заказы, которые принял другой курьер, пропадают из списка.   
2. Для вкладки «Все»: заказы, которые отменил пользователь, удаляются.   
3. Для вкладок «Все» и «Мои»: карточки сортируются по дате доставки, которую указал пользователь. Просроченные заказы — сверху.  
При каких действиях список заказов обновляется:  
1. При pull-to-refresh.  
2. Если перейти во вкладку «Мои» на главном экране, а потом вернуться назад во вкладку «Все».  
3. Если применить фильтр по станции метро.  
При каких действиях список заказов не обновляется:  
1. Если принять заказ, он перемещается в «Мои», но остальной список не обновляется.  
Функциональность экрана «Список заказов»:  
1. Когда нет заказов, отображается экран «Заказов нет». Чтобы обновить экран, нужно сделать pull-to-refresh.  
2. Когда пользователь делает заказ, появляется короткая версия карточки заказа.   
3. Список заказов сортируется по приоритетности доставки: просроченные — сверху. Просроченным считается заказ, который не доставлен клиенту до 23:59 в нужный день. Рамка и дата просроченной карточки подсвечивается красным цветом, жирность текста — Medium. Условие работает для списков заказов «Все» и «Мои».  
4. Внутри вкладки «Все» есть фильтр по выбору метро. С его помощью курьер может настроить, заказы на каких станциях он хочет видеть. По тапу на фильтр открывается список: он формируется из тех станций, на которые уже есть заказы. Если есть два и более заказа с одинаковым метро, в фильтре появляется только одно наименование: одинаковые станции не дублируются.  
5. Карточка фильтра увеличивается по мере добавления станций метро. В карточку вмещается максимум 8 станций: начиная с девятой появляется скролл.  
6. Карточка заказа может быть в краткой или полной версии.   
    - Поля для краткой версии: «Адрес», «Дата доставки», выбранная станция метро.  
    - Поля для полной версии: «Адрес», «Дата доставки», выбранная станция метро. Добавляется «Имя», «Фамилия», «Телефон», «Цвет», «Комментарий». Если пользователь не заполнил поле «Цвет», пишется «любой».  
7. Переключить версию карточки можно через тап по карточке. Это работает для вкладок «Все» и «Мои».  
8. При переходе в полный режим карточки кнопка «Принять» остаётся на месте. Карточки, которые идут следом, сдвигаются вниз.  
9. Чтобы принять заказ, нужно тапнуть по кнопке «Принять». Это работает и для краткой, и для полной версий карточки.   
10. При тапе по кнопке появляется уведомление с текстом «Хотите принять заказ?» и две кнопки «Да» и «Нет». Тап по «Нет» возвращает обратно на список заказов, кнопка «Принять» остаётся активной. Тап по «Да» подтверждает принятие заказа.  
11. Чужой или отменённый заказ принять нельзя. Появляется сообщение: «Ты не можешь принять заказ. Его взял уже другой курьер или пользователь отменил его».  
12. Когда заказ принят, карточка уезжает из списка «Все» — с анимацией движения вверх. У вкладки «Мои» появляется синяя точка — она обозначает, что во вкладке появился новый принятый заказ.   
13. Логика работы синей точки: появляется, если есть непросмотренные карточки во вкладке «Мои». Автоматическое переключение на вкладку «Мои» не происходит.  
14. Карточка, которую принял курьер, помещается во вкладку «Мои». Кнопка меняется на «Завершить». Завершить заказ можно тапом по кнопке «Завершить» — как в коротком, так и в полном виде карточки.   
15. Если нажать на «Завершить», появляется уведомление «Вы завершили заказ?» и две кнопки — «Да» и «Нет». Тап по «Нет» возвращает обратно на список заказов, кнопка «Завершить» остаётся активной. Тап по «Да» подтверждает завершение заказа.  
16. Когда заказ завершён, карточка заказа перемещается в самый низ списка. Если заказ был просрочен, но потом выполнен, карточка не подсвечивается красным.  
17. Завершённые заказы сортируются по времени выполнения: чем раньше завершён заказ, тем он ниже.  

### Нотификация  
**1. Уведомление приходит, когда осталось 2 часа, чтобы выполнить заказ. Заказ нужно доставить в день, который указал пользователь, до 23:59. Например, заказ на 8 мая. Если в 21:59 8 мая курьер ещё не доставил самокат, ему приходит пуш-уведомление.**   
**2. Уведомление содержит такой текст: «2 часа до конца заказа. Заказ «ул Комнатная 12-14» нужно выполнить до `времени N`. Если не успеваете, предупредите поддержку: 0101»**
**3. Переход по нотификации ведёт в приложение на вкладку «Мои».**  

### Отсутствие интернет-соединения  
**1. Если нет интернет-соединения, отображается всплывающее окно «Отсутствует интернет-соединение». Оно появляется, если тапнуть по любой активной кнопке на любом экране. Пропадает только по тапу по кнопке «Ок».**   
**2. Когда пользователь тапнул по кнопке «Ок», всплывающее уведомление закрывается. Если интернета всё ещё нет, процесс повторяется: тап по любой активной зоне ведёт на всплывающее уведомление «Отсутствует интернет-соединение».**  

### Ориентация  
Приложение только в портретной ориентации.  

<summary> Требования к бэкенду приложения </summary> 

### Технологии
Язык приложения — JavaScript.   
Выполняется в среде Node.js v12.17.0.  
Доступ к приложению по протоколу HTTP 1.1.   

### Общие требования
Приложение использует базу данных. БД — PostgreSQL. Приложение взаимодействует с БД через npm-пакет `sequelize` поверх пакета `pg`. `sequelize` — ORM для работы с различными БД в node.js.  
Запросы логируются через модуль `winston`. Документация к приложению осуществляется с помощью модуля `apidoc`.
Приложение должно отвечать требованиям REST.  
В приложении должен быть глобальный обработчик ошибок. При возникновении исключений они должны быть обработаны, а приложение должно продолжить работу.  
Ошибки приложения (неуспешно обработанные запросы, исключения; ответы, отличные от 2XX) должны логироваться в отдельный файл `error.log`  

### Требования к URL
**Вспомогательные URL**  
- Должен присутствовать URL, через который можно проверить, что бэкенд запущен и принимает запросы. При успешном ответе должен вернуться статус `200 OK`.  
- Должен присутствовать URL, через который работает поиск станций метро. В случае успешного поиска должны вернуться номер станции, её цвет и название. Если станций   несколько, для каждой должны возвращаться номер, цвет и название. Если станция не найдена, должен вернуться пустой список.  

**URL для курьеров**  
**- Должен присутствовать URL: при обращении к нему курьер может зарегистрироваться в приложении. URL должен принимать логин, пароль и имя курьера. Логин, хэш пароля и имя курьера должны записываться в поля *`login`, `passwordHash`* и *`firstName`* таблицы *Couriers*. В поле `passwordHash` хранится хэш пароля, генерируется стандартными функциями, поэтому соответствие хэш-пароль проверить можно через авторизацию.**  
**- Поле login должно быть уникальным. При успешной регистрации соответствующая запись должна появиться в базе. При неуспешной должна вернуться ошибка. Подробнее об ошибках в документации `/docs/#api-Courier-CreateCourier`**  
- Должен присутствовать URL для входа в учётную запись курьером. На вход должны отправляться логин и пароль курьера. При успешном входе должен вернуться `id` курьера. Если войти не удалось, должна вернуться ошибка.   
**- Должен присутствовать URL для удаления учётной записи курьера. На вход должен подаваться `id` курьера в таблице Couriers. При удалении связанные заказы в таблице Orders должны быть стёрты.**  

**URL для заказов**  
Каждый раз, когда какой-нибудь из URL возвращает полные данные о заказе, ответ должен  содержать и статус каждого заказа. В статусе должны быть такие значения:  
- `0` — заказ создан, больше ничего с ним не происходило;  
- `1` — заказ принят курьером;    
- `2` — заказ завершён;  
- `-1` — заказ отменён.  
Статус должен вычисляться относительно значений полей в БД в таблице Orders (см. пункт «Описание содержимого базы данных»). Поля указаны в порядке приоритетности:  
- `finished = true` -> `status = 2`  
- `cancelled = true` -> `status = -1`  
- `inDelivery = true` -> `status = 1`  
- `Остальные случаи` -> `status = 0`  
Должен присутствовать URL для создания заказа. При создании заказа указываются следующие параметры:  
- имя;  
- фамилия;  
- адрес;  
- ближайшая станция метро;  
- телефон;  
- количество дней аренды;  
- дата доставки;  
- комментарий;  
- список подходящих цветов.  
При создании заказа ему должен быть присвоен индивидуальный номер для отслеживания.  
 Переданные параметры записываются в таблицу `Orders` следующим образом:  
- имя: `firstName`  
- фамилия: `lastName`  
- адрес: `address`  
- ближайшая станция метро: `metroStation`  
- телефон: `phone`  
- количество дней аренды: `rentTime`  
- дата доставки: `deliveryDate`  
- комментарий: `comment`  
- список подходящих цветов: `color`  
- номер отслеживания: `track`  
Если заказ создан успешно, должен вернуться его номер отслеживания. В противном случае должна вернуться ошибка. Подробнее об ошибках в документации: `/docs/#api-Orders-CreateOrder`  
**- Должен присутствовать URL для получения данных о заказе по его номеру отслеживания. На вход должен подаваться номер. Если соответствующий заказ найден, должны вернуться данные о нём. Иначе должна вернуться ошибка.**  
- Должен присутствовать URL для принятия заказа курьером. URL принимает номер отслеживания заказа и id курьера. Если при принятии заказа возникли проблемы, должна вернуться ошибка.  
- Должен присутствовать URL для отмены заказа. URL принимает номер для отслеживания заказа. В случае неуспешной отмены должна вернуться ошибка.  
- Должен присутствовать URL для завершения заказа. На вход подаётся номер заказа. В случае неуспешного завершения должна вернуться ошибка.  
- Должен присутствовать URL для получения всех заказов, которые соответствуют заданным параметрам. Параметры поиска — ближайшая станция метро и id курьера. Также должны быть переданы ограничения по количеству выводимых записей на странице и номер страницы. Подробнее об ошибках и кейсах применения в документации: `/docs/#api-Orders-GetOrdersPageByPage`  
- Должен присутствовать URL для получения количества выполненных заказов курьера. На вход должен подаваться id курьера. Подробнее об ошибках и кейсах использования в документации: `/docs/#api-Couriers-GetOrdersCountByCourierId`  


### Описание содержимого базы данных
БД состоит из двух таблиц: Couriers и Orders. Первая таблица содержит данные о курьерах, вторая — данные о заказах.  


</details>

## Инструменты
<p align="left"> 
   <a href="https://miro.com/" target="_blank" rel="noreferrer"><img src="https://w7.pngwing.com/pngs/885/629/png-transparent-miro-hd-logo-thumbnail.png" width="36" height="36" alt="Miro" /></a>
   <a href="https://www.figma.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/figma-colored.svg" width="36" height="36" alt="Figma" /></a>
  <a href="https://docs.google.com/" target="_blank" rel="noreferrer"><img src="https://w7.pngwing.com/pngs/240/1015/png-transparent-g-suite-google-docs-google-angle-rectangle-logo.png" width="36" height="36" alt="Google Sheets" /></a>
  <a href="https://www.jetbrains.com/youtrack/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/9/95/YouTrack_Icon.png" width="36" height="36" alt="Youtrack" /></a>
  <a href="https://developer.android.com/studio" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Android_Studio_icon_%282023%29.svg/800px-Android_Studio_icon_%282023%29.svg.png" width="36" height="36" alt="Android_Studio" /></a>
   <a><img src="https://d33wubrfki0l68.cloudfront.net/38b5c953a4667366685d55db55d057c86db1fc54/a0fdc/static/acae6b24d940347661ca901ea07f47c1/chrome-dev-logo-icon.png" width="36" height="36" alt="Devtools" /></a>
  <a href="https://www.postman.com/" target="_blank" rel="noreferrer"><img src="https://seeklogo.com/images/P/postman-logo-0087CA0D15-seeklogo.com.png" title="postman" width="36" height="36" alt="Postman" /></a>
  <a href="https://www.charlesproxy.com/" target="_blank" rel="noreferrer"><img src="https://davidwalsh.name/demo/charlesproxyicon.svg" width="36" height="36" alt="Charles" /></a>
  <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="36" height="36" alt="PostgreSQL" /></a>
</p> 




