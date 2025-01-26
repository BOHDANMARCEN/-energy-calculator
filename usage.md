# Інструкція користувача

## Встановлення

```bash
pip install energy-calculator
```

## Використання

### Як програма командного рядка

```bash
energy-calculator
```

### Як Python модуль

```python
from energy_calculator import calculate_energy, convert_energy

# Обчислення енергії
energy = calculate_energy(power_watts=1000, time_seconds=3600)
print(f"Енергія: {energy} Дж")

# Конвертація в кВт·год
kwh = convert_energy(energy, "kWh")
print(f"Енергія: {kwh} кВт·год")
```

## Підтримувані одиниці вимірювання

- kWh (кіловат-години)
- MJ (мегаджоулі)
- Wh (ват-години)
- cal (калорії)
- kcal (кілокалорії)

## Обробка помилок

Програма валідує вхідні дані та видає зрозумілі повідомлення про помилки:

- Від'ємні значення
- Занадто великі значення
- Невідомі одиниці вимірювання