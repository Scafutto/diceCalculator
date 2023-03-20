# Math explanation here:
# https://www.mathsisfun.com/data/binomial-distribution.html

def factorial(num):
    if (num < 0):
        return -1
    elif (num == 0):
        return 1
    else:
        return (num*factorial(num-1))


class Attacker:
    def __init__(self, dieSize, dicePool, damage, penDamage):
        self.dieSize = dieSize
        self.dicePool = dicePool
        self.damage = damage
        self.penDamage = penDamage

    def __str__(self) -> str:
        print(f"")

    def calc(self, target):
        lowestValue = 3 # anything above 4 is a success
        n = self.dicePool
        p = (self.dieSize - lowestValue) / self.dieSize
        arr = []

        for i in range(0, self.dicePool+1):
            finalDamage = (i - target.totalDefense) * self.damage
            if (finalDamage < 0):
                finalDamage = 0

            finalPenDamage = (i - (target.totalDefense - target.armorDefense)) * self.penDamage
            if (finalPenDamage < 0):
                finalPenDamage = 0

            r = i # Just adjusting the variable to better fit "n choose r"
            nCr = factorial(n) / (factorial(r) * factorial(n - r))
            prob = nCr * (p**r) * ((1 - p)**(n - r))

            arr.append([prob, finalDamage, finalPenDamage])

        print(arr)
        self.report(arr, target)

    def report(self, arr, target):
        # Fix formatting 
        # rows should have the same length and alignment
        print(f"Die Size: {self.dieSize} | Dice pool: {self.dicePool} | Damage: {self.damage} | Penetration damage: {self.penDamage}")

        print(f'{"Successes":<10} {"Probability":>15} {"Damage":>15} {"Pen. Damage":>15}')
        for i, e in enumerate(arr):
            print(f"{i:<4} {(e[0]*100):>15.2f}% {e[1]:>15} {e[2]:>15}")


class Defender:
    def __init__(self, totalDefense, armorDefense):
        self.totalDefense = totalDefense
        self.armorDefense = armorDefense

        # Further implement Health Points
        # Further implement active rolls for defense 
        

# define an attacker and defender, call the method calc() from the attacker]
# a1 = Attacker(die size, number of dice, damage, penetration damage)
# d1 = Defender(number of successes to get hit [defense], armor defense)
# a1.calc(d1)

a1 = Attacker(6, 4, 2,1)
d1 = Defender(2, 1)
a1.calc(d1)