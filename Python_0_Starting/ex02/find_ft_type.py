def all_thing_is_obj(obj: any) -> int:
    obj_type = type(obj).__name__
    if obj_type == "str":
        print(obj + " is in the kitchen :", type(obj))
    elif obj_type in ["list", "tuple", "set", "dict"]:
        print(obj_type.capitalize(), ":", type(obj))
    else:
        print("Type not found", ":", type(obj))
    return 42
