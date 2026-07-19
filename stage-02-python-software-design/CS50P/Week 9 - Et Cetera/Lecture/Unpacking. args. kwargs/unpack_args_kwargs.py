def f(*args, **kwargs):
    print(
        "Named:", kwargs
    )  # collects any extra keyword (name=value) arguments into a dictionary
    print("Positional:", args)  # collects any extra positional arguments into a tuple


f(1, 2, name="Veselin", age=20)
