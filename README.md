# Домашнее задание #01

### 1. Написать консольную игру крестики-нолики.

Пример того, как схематично можно изобразить класс игры.

```py
class TicTacGame:

    def show_board():
        pass

    def validate_input():
        pass

    def start_game():
        pass

    def check_winner():
        pass


if __name__ == "__main__":
    game = TicTac()
    game.start_game()

```
Допустима реализация без использования классов.

Пользовательский ввод осуществляется с помощью input, который необходимо валидировать и выводить понятное описание ошибки.

Схема класса не обязательно должна быть такой, можно добавлять и менять методы, держа в голове грамотную организацию кода, ненужное дублирование и код-лапшу.

По желанию, можно написать вспомогательную функцию, запустив которую, компьютер сыграет сам с собой без участия человека, либо сделать возможным игру между человеком и компьютером.


### 2. Написать тесты (unittest, assert) для игры, покрыв тестами основные методы

### 3. Проверить корректность и стиль кода с помощью pylint или flake8

# Домашнее задание #02

### Написать функцию, которая в качестве аргументов принимает строку json, список полей, которые необходимо обработать, список имён, которые нужно найти и функцию-обработчика имени, который срабатывает, когда в каком-либо поле было найдено ключевое имя.

Функция, должна принимать строку, в которой содержится json, и произвести парсинг этого json.
Упростим немного и представим, что json представляет из себя только коллекцию ключей-значений.
Причём ключами и значениями являются только строки.

```py
def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback)
```

Например, представим, что json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}', а required_fields = ["key1"], keywords = ["word2"]. Тогда keyword_callback будет вызвана только для слова 'word2' для ключа 'key1'.

Распарсить json можно так:
```py
import json

...
json_doc = json.loads(json_str)

```

Можно использовать ещё ujson, но его предварительно нужно установить с помощью pip.

### Написать декоратор, который выводит среднее время выполнения последних k вызовов при каждом вызове функции

```py
@mean(10)
def foo(arg1):
    pass

@mean(2)
def boo(arg1):
    pass

for _ in range(100):
    foo("Walter")
```

### Использовать mock-объект при тестировании
Использовать mock-объект, например, keyword_callback и проверить, что заглушка вызывалась n число раз.

### Узнать степень покрытия тестами с помощью библиотеки coverage

### Использовать flake8 и pylint для проверки кода

### Использовать factory boy (опционально!!!)
Для генерации данных и ключевых слов, можно использовать factory boy (см. файл factory_boy_example.py).

# Домашнее задание #03 (объектная модель, ООП)

### 1. Реализовать класс CustomList наследованием от list

При этом:
- CustomList должен наследоваться от встроенного списка `list`;
- экземпляры CustomList можно складывать друг с другом и с обычными списками:
  ```py
  CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])  # CustomList([6, 3, 10, 7])
  CustomList([1]) + [2, 5]  # CustomList([3, 5])
  [2, 5] + CustomList([1])  # CustomList([3, 5])
  ```
- экземпляры CustomList поддерживают вычитание между собой и с обычными списками:
  ```py
  CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])  # CustomList([4, -1, -4, 7])
  CustomList([1]) - [2, 5]  # CustomList([-1, -5])
  [2, 5] - CustomList([1])  # CustomList([1, 5])
  ```
- результатом сложения/вычитания должен быть новый кастомный список;
- после сложения/вычитания исходные списки не должны изменяться;
- при сложении/вычитании списков разной длины отсутствующие элементы меньшего списка считаются нулями;
- при сравнении (==, !=, >, >=, <, <=) экземмпляров CustomList должна сравниваться сумма элементов списков (сравнение с list не нужно);
- должен быть переопределен str, чтобы выводились элементы списка и их сумма;
- списки можно считать всегда числовыми.

### 2. Тесты CustomList в отдельном модуле

### 3. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black

# Домашнее задание #04 (дескрипторы, метаклассы, ABC)

### 1. Метакласс, который в начале названий всех атрибутов и методов, кроме магических, добавляет префикс "custom_"
  Подменяться должны атрибуты класса и атрибуты экземпляра класса, в том числе добавленные после выполнения конструктора (dynamic в примере).

```py
    class CustomMeta(...):
        pass


    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"


    assert CustomClass.custom_x == 50
    CustomClass.x  # ошибка

    inst = CustomClass()
    assert inst.custom_x == 50
    assert inst.custom_val == 99
    assert inst.custom_line() == 100
    assert str(inst) == "Custom_by_metaclass"

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
    inst.yyy  # ошибка

    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later"
    inst.dynamic  # ошибка
```


### 2. Дескрипторы с проверками типов и значений данных
  Нужно сделать три дескриптора для какой-то области интереса (наука, финансы, хобби и тд), но если совсем не получается, то можно использовать шаблона ниже в качестве основы.

```py
    class Integer:
        pass

    class String:
        pass

    class PositiveInteger:
        pass

    class Data:
        num = Integer()
        name = String()
        price = PositiveInteger()

        def __init__(...):
            ....
```


### 3. Тесты метакласса и дескрипторов

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black

# Домашнее задание #05 (стандартная библиотека)

### 1. LRU-кэш
Интерфейс:

```py
    class LRUCache:

        def __init__(self, limit=42):
            pass

        def get(self, key):
            pass

        def set(self, key, value):
            pass


    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3")) == "val3"
    assert cache.get("k2")) is None
    assert cache.get("k1")) == "val1"


    Если удобнее, get/set можно сделать по аналогии с dict:
    cache["k1"] = "val1"
    print(cache["k3"])
```

Сложность решения по времени в среднем должна быть константной O(1).
Реализация любым способом без использования OrderedDict.

### 2. Тесты в отдельном модуле

### 3. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black