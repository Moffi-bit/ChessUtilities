import generate

def main():
    gen = generate.Generator()
    gen.evaluateArguments()
    for i in range(0, 10):
        print(f"Fen #{i + 1}: " + gen.getRandomFEN())

if __name__ == '__main__':
    main()