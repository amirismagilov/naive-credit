def is_creditable(age, salary):
    #первый тест позитивный
    """
    >>>is_creditable(30,40_000)
    True

    >>>is_creditable(20, 40_000)
    False

    >>>is_creditable(70, 40_000)
    False
    >>>is (30, 20_000)
    False
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000
    if min_age <= age <= max_age and salary >= min_salary:
        return True
    else:
        return False