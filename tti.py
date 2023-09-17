tomeg = float(input("Kérem adja meg a tömegét kilogrammban: "))
magassag=float(input("magassag:"))
tti = tomeg / (magassag ** 2)
tti_kerekitett = round(tti, 2)
if 18.5 <= tti < 25:
    normalis_intervallum = "normál (18,5 – 24,99)"
else:
    normalis_intervallum = "nem normál"

print(f"A testtömeg-index (TTI) értéke: {tti_kerekitett}")
print(f"A normál testtömeg-intervallum (kg-ban) a megadott magassághoz viszonyítva: {normalis_intervallum}")

