from math import sqrt

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
check = [100, 100]


def print_grades(grades_input):
    for grade in grades:
        print(grade)


print(print_grades(grades))


def grades_sum(scores):
    total = 0
    for x in scores:
        total += x
    return total


print(grades_sum(grades))


def grades_average(grades_input):
    average = float(grades_sum(grades_input)) / float(len(grades_input))
    return average


print(grades_average(grades))


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        x = (average - score) ** 2
        variance += x
    result = variance / float(len(scores))
    return result


print(grades_variance(grades))


def grades_std_deviation(variance):
    return sqrt(variance)


variance = grades_variance(grades)

print(grades_std_deviation(variance))





