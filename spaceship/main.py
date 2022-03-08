from RocketEngine import *

if __name__ == '__main__':
    print("Statek stoi zacumowany w porcie.")
    RocketEngine.status()
    print("Materializacja dwóch silników manewrowych.")
    small_engine1 = RocketEngine("manewrowy_lewy", 50)
    small_engine2 = RocketEngine("manewrowy_prawy", 50)
    print(f"Stan silnikow:\n{small_engine1}\n{small_engine2}")
    print("Stan statku:")
    RocketEngine.status()
    print("Uruchomienie silników manewrowych.")
    small_engine1.start()
    small_engine2.start()
    print(f"Stan silnika manewrowego:\n{small_engine2}")
    print("Stan statku:")
    RocketEngine.status()

    print("Statek wymanewrowuje z portu i materializuje silniki do rozpedzenia sie do hiperpredkosci.")
    medium_engine1 = RocketEngine("Sredni_lewy", 500)
    medium_engine2 = RocketEngine("Sredni_prawy", 500)
    print("Statek wylacza silniki manewrowe i przechodzi na naped glowny.")
    small_engine1.stop()
    small_engine2.stop()
    medium_engine1.start()
    medium_engine2.start()
    print("Stan statku:")
    RocketEngine.status()

    print("Statek materializuje silniki hiperpredkosciowe, wylacza glowny naped i przzechodzi na hipernaped.")
    medium_engine1.stop()
    medium_engine2.stop()
    big_engine1 = RocketEngine("Hiper_lewy", 400000)
    big_engine2 = RocketEngine("Hiper_prawy", 400000)
    big_engine1.start()
    big_engine2.start()
    print("Status statku:")
    RocketEngine.status()

    print("Statek dolatuje na miejsce docelowe, dematerializuje silniki hiperpredkosci i wlacza glowny naped.")
    del big_engine2
    del big_engine1
    medium_engine2.start()
    medium_engine1.start()
    print("Stan statku:")
    RocketEngine.status()

    print("Statek dolatuje do portu, dematerializuje naped glowny i wlacza silniki manewrowe.")
    del medium_engine1
    del medium_engine2
    small_engine2.start()
    small_engine1.start()
    print("Stan statku:")
    RocketEngine.status()

    print("Statek cumuje do portu i dematerializuje wszystkie pozostale silniki.")
    del small_engine1
    del small_engine2
    print("Stan statku:")
    RocketEngine.status()
