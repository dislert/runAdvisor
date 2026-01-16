def calculate_run_comfort(weather):
    score = 100
    reasons = []

    # Температура
    if weather.temperature < -10:
        return {
            "comfort_score": 0,
            "is_good_for_run": False,
            "explanation": "Слишком холодно для бега (ниже -10°C)"
        }

    if weather.temperature > 35:
        return {
            "comfort_score": 0,
            "is_good_for_run": False,
            "explanation": "Слишком жарко для бега (выше +35°C)"
        }

    if weather.temperature < 0:
        score -= 30
        reasons.append("холодно")

    elif weather.temperature > 25:
        score -= 25
        reasons.append("жарко")

    # Ветер
    if weather.wind_speed > 15:
        return {
            "comfort_score": 0,
            "is_good_for_run": False,
            "explanation": "Слишком сильный ветер"
        }

    elif weather.wind_speed > 8:
        score -= 20
        reasons.append("сильный ветер")

    # Влажность
    if weather.humidity > 85:
        score -= 15
        reasons.append("высокая влажность")

    # Осадки
    if weather.precipitation > 5:
        return {
            "comfort_score": 0,
            "is_good_for_run": False,
            "explanation": "Сильные осадки"
        }

    elif weather.precipitation > 0:
        score -= 10
        reasons.append("есть осадки")

    # Итог
    is_good = score >= 60

    if not reasons:
        explanation = "Отличные условия для бега"
    else:
        explanation = "Условия неидеальны: " + ", ".join(reasons)

    return {
        "comfort_score": max(score, 0),
        "is_good_for_run": is_good,
        "explanation": explanation
    }
