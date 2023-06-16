def get_medical_servise(preparet):
    def d0_treat():
        print(f"[{preparet}] Я тебя вылечил")
    return d0_treat


theater1 = get_medical_servise("Парацетамол")
theater2 = get_medical_servise("Цитрамон")

theater1()
theater2()
# [Парацетамол] Я тебя вылечил
# [Цитрамон] Я тебя вылечил

print("="*80)

def init_counter(start_from):
    def count():
        nonlocal start_from
        start_from +=1
        print(f"Number: {start_from}")
    return count

counter1 = init_counter(0)
counter2 = init_counter(100)
counter2()
counter1()
counter1()
counter1()
counter1()
counter1()
# Number: 101
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5


