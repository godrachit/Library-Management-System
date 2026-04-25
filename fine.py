def calculate_fine(days_late):
    fine = 0
    rate = 10

    for week in range(1, (days_late // 7) + 2):
        fine += rate * week * min(7, days_late)
        days_late -= 7
        if days_late <= 0:
            break

    return fine