# Anixart Other methods

## **Оглавление класса**

* Type:
    * [/type/all](#typeall) - Получение списка всех доступных озвучек.

## **Endpoints**

```python
#############    OTHER    #############

# GET
VOICE = "/type/all"

```

## **Type**

### **/type/all**

Метод получения списка всех доступных озвучек.

* Обращение:
    * Протокол: <span style="color:#02e400">GET</span>
    * Необходимо:
        * Payload - Данные запроса:
            * token: <span style="color:#f1c232">str</span>
    * Пример: `GET {API_URL}/type/all?token={token}`
* Ответ:
    * Тип: json
    * Res:

```json
{
  "code": 0,
  "types": [
    {
      "@id": 1, 
      "id": 1,
      "name": "AniDub", 
      "workers": "", 
      "episodes_count": 0, 
      "view_count": 0
    },
    ...
  ]
}
```