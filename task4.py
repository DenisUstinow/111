# 1


def dict_constructor(v_num, v_tara, v_name="контейнер"):

    dictor = {
        "number": v_num,
        "tara": v_name,
        "name": v_tara
    }

    return dictor


print(dict_constructor(23, 546565, "контейнер"))
print(dict_constructor)


# 2


def do_tuple(*args):
    print("Кортеж:", args)


do_tuple((1, 2, 3), [1, 2, 3], {"1": 2})


do_tuple()
