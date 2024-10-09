#Flow 9. Okt. 2024
def einfacher_taschenrechner(eingabe):
    # Entferne mögliche Leerzeichen aus dem Eingabestring
    eingabe = eingabe.replace(" ", "")

    # Erlaube nur Zeichen, die für den Taschenrechner relevant sind
    erlaubte_zeichen = "0123456789+-*/%^()"
    
    if not all(char in erlaubte_zeichen for char in eingabe):
        return "Ungültige Eingabe!"

    # Überprüfe, ob die Klammern korrekt sind
    if not klammern_sind_korrekt(eingabe):
        return "Klammerfehler: Die Anzahl der öffnenden und schließenden Klammern ist nicht korrekt."
    
    try:
        # Ersetze `^` durch `**` für Potenzberechnungen, da Python `**` verwendet
        eingabe = eingabe.replace('^', '**')
        
        # Berechne das Ergebnis mit eval
        ergebnis = eval(eingabe)
        return ergebnis
    except Exception as e:
        return f"Fehler bei der Berechnung: {e}"

def klammern_sind_korrekt(eingabe):
    stack = []
    for char in eingabe:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Beispielverwendung
print("Rechne wie in einem Taschenrechner\n^ : Hoch\n+ : Plus\n- : Minus\n* : Mahl\n/ : Geteilt")
example = "1^4*3*(3+4)"
print("Beispiel : 1^4*3*(3+4)")
print(f"Ergebnis: {einfacher_taschenrechner(example)}")
while True:
    eingabe = input("Gib deinen Ausdruck ein: ")
    print(f"Ergebnis: {einfacher_taschenrechner(eingabe)}")
