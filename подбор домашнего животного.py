from owlready2 import *

onto_path.append(".")
onto = get_ontology("file://pets.owx").load()

def choose_from_menu(title, options):
    print("\n" + title)
    for i, (key, _) in enumerate(options.items(), start=1):
        print(f"{i}. {key}")

    try:
        choice = int(input("Введите номер: "))
        if 1 <= choice <= len(options):
            return list(options.values())[choice - 1]
    except ValueError:
        pass

    print("Неверный ввод")
    return None

def recommend_pet():
    life_span_options = {
        "Короткая": onto["Короткая"],
        "Средняя": onto["Средняя"],
        "Долгая": onto["Долгая"],
    }

    living_condition_options = {
        "Свободное": onto["Свободное"],
        "Клетка": onto["Клетка"],
        "Аквариум": onto["Аквариум"],
        "Террариум": onto["Террариум"],
    }

    animal_class_options = {
        "Млекопитающее": onto["Млекопитающее"],
        "Птицы": onto["Птицы"],
        "Рыбы": onto["Рыбы"],
        "Пресмыкающиеся": onto["Пресмыкающиеся"],
        "Паукообразное": onto["Паукообразное"],
    }

    life_span = choose_from_menu(
        "Выберите продолжительность жизни:", life_span_options
    )
    if not life_span:
        return

    living_condition = choose_from_menu(
        "Выберите условия проживания:", living_condition_options
    )
    if not living_condition:
        return

    animal_class = choose_from_menu(
        "Выберите класс животного:", animal_class_options
    )
    if not animal_class:
        return

    Animal = onto["Домашнее_животное"]
    LifeSpanProp = onto["имеет_продолжительность_жизни"]
    LivingConditionProp = onto["требует_условия_проживания"]

    print("\nРекомендованные животные:")
    found = False

    for animal in Animal.instances():
        if (
            animal_class in animal.is_a and
            LifeSpanProp.some(life_span) in animal.is_a and
            LivingConditionProp.some(living_condition) in animal.is_a
        ):
            print("-", animal.name)
            found = True

    if not found:
        print("Подходящих животных не найдено")

recommend_pet()
