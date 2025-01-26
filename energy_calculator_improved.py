#!/usr/bin/env python3
"""
Калькулятор електроенергії

Обчислює електричну енергію та конвертує між різними одиницями вимірювання.

from typing import Union, Dict, Optional
import logging
from datetime import datetime

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=f'energy_calculator_{datetime.now().strftime("%Y%m%d")}.log'
)

# Константи
CONVERSION_FACTORS: Dict[str, float] = {
    'kWh': 1/3.6e6,  # 1 кВт·год = 3.6e6 Дж
    'MJ': 1/1e6,     # 1 МДж = 1e6 Дж
    'Wh': 1/3600,    # 1 Вт·год = 3600 Дж
    'cal': 1/4.184,  # 1 кал = 4.184 Дж
    'kcal': 1/4184   # 1 ккал = 4184 Дж
}

def validate_input(value: float, name: str) -> None:
    """
    Перевіряє коректність вхідних даних.
    
    Args:
        value: Значення для перевірки
        name: Назва параметра для повідомлення про помилку
    
    Raises:
        ValueError: Якщо значення від'ємне або занадто велике
    """
    if value < 0:
        raise ValueError(f"{name} повинно бути додатним числом")
    if value > 1e12:
        raise ValueError(f"{name} занадто велике (max: 1e12)")

def calculate_energy(power_watts: float, time_seconds: float) -> float:
    """
    Обчислює електроенергію в джоулях.
    
    Args:
        power_watts: Потужність у Ватах (W)
        time_seconds: Час у секундах (s)
    
    Returns:
        float: Енергія в джоулях (J)
    
    Raises:
        ValueError: Якщо вхідні дані некоректні
    """
    validate_input(power_watts, "Потужність")
    validate_input(time_seconds, "Час")
    
    energy = power_watts * time_seconds
    logging.info(f"Обчислено енергію: {energy:.2f} Дж")
    return energy

def convert_energy(energy_joules: float, target_unit: str) -> float:
    """
    Конвертує енергію з джоулів у вказану одиницю.
    
    Args:
        energy_joules: Енергія в джоулях (J)
        target_unit: Одиниця конвертації ('kWh', 'MJ', 'Wh', 'cal', 'kcal')
    
    Returns:
        float: Енергія у вибраній одиниці
    
    Raises:
        ValueError: Якщо вказана невідома одиниця вимірювання
    """
    if target_unit not in CONVERSION_FACTORS:
        raise ValueError(
            f"Невідома одиниця конвертації: {target_unit}. "
            f"Доступні одиниці: {', '.join(CONVERSION_FACTORS.keys())}"
        )
    
    result = energy_joules * CONVERSION_FACTORS[target_unit]
    logging.info(f"Конвертовано {energy_joules:.2f} Дж в {result:.4f} {target_unit}")
    return result

def format_energy(value: float, unit: str) -> str:
    """
    Форматує значення енергії для виведення.
    
    Args:
        value: Значення енергії
        unit: Одиниця вимірювання
    
    Returns:
        str: Відформатований рядок
    """
    if value >= 1e6:
        return f"{value:,.2e} {unit}"
    return f"{value:,.4f} {unit}"

def main() -> None:
    """Головна функція програми."""
    print("🔋 Калькулятор електроенергії\n")
    
    try:
        # Отримання вхідних даних
        power = float(input("Введіть потужність у Ватах (W): "))
        time = float(input("Введіть час у секундах (s): "))
        
        # Обчислення енергії
        energy_joules = calculate_energy(power, time)
        print(f"\nОбчислена енергія: {format_energy(energy_joules, 'Дж (J)')}")
        
        # Конвертація
        print(f"\nДоступні одиниці: {', '.join(CONVERSION_FACTORS.keys())}")
        target_unit = input("Введіть одиницю для конвертації: ").strip()
        
        converted_energy = convert_energy(energy_joules, target_unit)
        print(f"Результат: {format_energy(converted_energy, target_unit)}")
        
    except ValueError as e:
        logging.error(f"Помилка введення: {e}")
        print(f"❌ Помилка: {e}")
    except Exception as e:
        logging.error(f"Непередбачена помилка: {e}")
        print("❌ Сталася непередбачена помилка. Перевірте лог-файл.")

if __name__ == "__main__":
    main()
