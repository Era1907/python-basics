name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter current year: "))

birth_year = current_year - age

print("\n-----------------------------")
print(f"Hey {name} ✨")
print(f"Your birth year is approx: {birth_year}")
print("-----------------------------\n")

# validation
if age < 0:
    print("❌ Invalid age. Time traveler detected?")
elif age > 120:
    print("👀 Bro are you immortal or what?")
else:

    # generation logic
    if birth_year >= 2013:
        print("🧒 Generation: Gen Alpha")
        quote = "You are growing in the age of AI and infinite possibilities."
    elif birth_year >= 1997:
        print("🧑 Generation: Gen Z")
        quote = "You are built different — chaos, creativity, and ambition."
    elif birth_year >= 1981:
        print("🧑‍💼 Generation: Millennial")
        quote = "You are the bridge between analog dreams and digital reality."
    elif birth_year >= 1965:
        print("👨‍🦳 Generation: Gen X")
        quote = "You are the silent strength holding everything together."
    elif birth_year >= 1946:
        print("👴 Generation: Baby Boomer")
        quote = "You carry wisdom built through decades of change."
    else:
        print("🕰️ Generation: Silent Generation")
        quote = "You are history itself — resilience in human form."

    # life calculation
    lifespan = 80
    life_lived = (age / lifespan) * 100
    years_left = lifespan - age

    print(f"\n📊 Life lived: {life_lived:.2f}%")

    # progress bar (10 blocks)
    filled = int(life_lived // 10)
    bar = "█" * filled + "░" * (10 - filled)
    print(f"📈 Life progress: [{bar}]")

    print(f"⏳ Approx years left: {years_left} years")

    print(f"\n💬 Motivation: {quote}")

print("\n✨ Remember: your generation doesn’t define you — your actions do.")