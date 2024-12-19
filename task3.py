import time
import random

class Fighter:
    def __init__(self, name: str, health: float, damage: list[float, float], attack_speed: list[float, float]):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed

    def __sub__(self, other: 'Fighter'):
        """
        Метод получения урона от другого бойца.
        """
        damage_received = random.uniform(*other.damage)
        self.health -= damage_received
        return damage_received

    def next_attack_time(self) -> float:
        """
        Вычисляет время до следующей атаки.
        """
        return random.uniform(*self.attack_speed)

def battle(fighter1: Fighter, fighter2: Fighter):
    """
    Функция, сталкивающая двух бойцов в схватке насмерть.
    Летопись сражения записывается в файл logger.txt.
    """
    start_time = time.time()
    log = []

    while fighter1.health > 0 and fighter2.health > 0:
        # Вычисляем время следующей атаки для каждого бойца
        time_to_next_attack_f1 = fighter1.next_attack_time()
        time_to_next_attack_f2 = fighter2.next_attack_time()

        if time_to_next_attack_f1 <= time_to_next_attack_f2:
            time.sleep(time_to_next_attack_f1)
            damage = fighter2 - fighter1
            elapsed_time = time.time() - start_time
            log.append(f"{elapsed_time:.2f}s: {fighter1.name} атаковал {fighter2.name} и нанёс {damage:.2f} урона. У {fighter2.name} осталось {fighter2.health:.2f} здоровья.")
            if fighter2.health <= 0:
                break
        else:
            time.sleep(time_to_next_attack_f2)
            damage = fighter1 - fighter2
            elapsed_time = time.time() - start_time
            log.append(f"{elapsed_time:.2f}s: {fighter2.name} атаковал {fighter1.name} и нанёс {damage:.2f} урона. У {fighter1.name} осталось {fighter1.health:.2f} здоровья.")
            if fighter1.health <= 0:
                break

    # Определяем победителя
    winner = fighter1 if fighter1.health > 0 else fighter2
    elapsed_time = time.time() - start_time
    log.append(f"{elapsed_time:.2f}s: Победитель - {winner.name}!")

    # Запись лога в файл
    with open("logger.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(log))

# Пример использования
fighter1 = Fighter("Боец 1", 100, [10, 20], [0.5, 1.5])
fighter2 = Fighter("Боец 2", 100, [5, 15], [1.0, 2.0])

battle(fighter1, fighter2)