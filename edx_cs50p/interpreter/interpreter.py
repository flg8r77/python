def main():
    expression = input("Expression: ")
    x, y, z = expression.split()

    match y:
        case '+':
            rv = float(x) + float(z)
        case '-':
            rv = float(x) - float(z)
        case '*':
            rv = float(x) * float(z)
        case '/':
            rv = float(x) / float(z)

    print(f"{rv:.1f}")

main()