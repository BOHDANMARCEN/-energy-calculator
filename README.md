# Energy Calculator 🔋

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

Калькулятор для обчислення та конвертації електричної енергії з підтримкою різних одиниць вимірювання.

## Основні можливості

- ⚡ Обчислення електроенергії за формулою `E = P·t`
- 🔄 Конвертація між одиницями вимірювання (kWh, MJ, Wh, cal, kcal)
- ✅ Валідація введених даних
- 📝 Логування операцій
- 🛡️ Обробка помилок

## Швидкий старт

```bash
# Клонування репозиторію
git clone https://github.com/username/energy-calculator.git
cd energy-calculator

# Створення віртуального середовища
python -m venv venv
source venv/bin/activate  # Linux/Mac
# або
venv\Scripts\activate     # Windows

# Встановлення залежностей
pip install -r requirements.txt

# Запуск програми
python energy_calculator.py
```

## Приклад використання

```python
from energy_calculator import calculate_energy, convert_energy

# Обчислення енергії (1 кВт протягом 1 години)
energy = calculate_energy(power_watts=1000, time_seconds=3600)
print(f"Енергія: {energy} Дж")  # 3,600,000 Дж

# Конвертація в кіловат-години
kwh = convert_energy(energy, "kWh")
print(f"Енергія: {kwh} кВт·год")  # 1.0 кВт·год
```

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

## Ліцензія

MIT License - дивіться [LICENSE](LICENSE) для деталей.

## Автор

-  Bogdan Martseniuk
- bodykabest@gmail.com
- GitHub: [@BOHDANMARCEN](https://githubBOHDANMARCEN.com/)
