def do_dict(**args):
    print("словарь:", args)

    do_dict(v_num=546789, v_tara=23, v_name="контейнер")

    do_dict()


print = do_dict
