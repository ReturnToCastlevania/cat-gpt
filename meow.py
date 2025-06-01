import json
import os
import time
import random

# Создание мяуканья
def meow():

    # Получение мяуканья
    MeowBase = [ 
"🐈", "🐈 ", "⛈", "🐛", "😺", "😾", "😻", "😸", "😼", "Мяу", "мЯу ", "мяУ", "МЯу ", "ня ", "мя", "🐱 ", "мурр ", "муя", "мяяя ", "няя" 
                ]
    result = ""
    for i in range(random.randint(1, 10)):
        rand = random.choice(MeowBase)
        result += rand

    # Редактировантие config.json
    with open("config.json", "r") as f:
        config = json.load(f)

    config["meowco"] += 1
    
    # 3. Сохраняем
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    print(time.strftime('%X'), f"помявкал {config['meowco']} раз", )

    return result

def stats():
    with open("config.json", "r") as f:
        config = json.load(f)

    print(time.strftime('%X'), "Открыто инлайн меню")
    return f"Проg🐈jизuошло {config['meowco']} 🐈мяlkjвканьей"
