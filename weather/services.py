def calculate_run_comfort(weather):
    
    score = 100
    reasons = []

    # Температура
    if weather.temperature < 0:
        score -= 30
        reasons.append("Слишком холодно")
    elif weather.temperature < 5:
        score -= 15
        reasons.append("Холодная погода")
    elif weather.temperature > 30:
        score -= 30
        reasons.append("Слишком жарко")
    elif weather.temperature > 25:
        score -= 15
        reasons.append("Жаркая погода")

    # Ветер
    if weather.wind_speed > 10:
        score -= 20
        reasons.append("Сильный ветер")
    elif weather.wind_speed > 5:
        score -= 10
        reasons.append("Умеренный ветер")

    # Влажность
    if weather.humidity > 85:
        score -= 15
        reasons.append("Высокая влажность")

    # Осадки
    if weather.precipitation > 0:
        score -= 25
        reasons.append("Есть осадки")

    # Ограничение диапазона
    score = max(score, 0)

    is_good = score >= 60

    if not reasons:
        reasons.append("Погодные условия близки к идеальным")

    return {
        "comfort_score": score,
        "is_good_for_run": is_good,
        "explanation": ", ".join(reasons),
    }
