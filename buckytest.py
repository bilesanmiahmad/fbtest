def health_checker(age, apples, cigs):
    answer = (age * 30) + (apples + 5) + (cigs * 3)
    print(answer)


medo = [34, 56, 0]
health_checker(*medo)

