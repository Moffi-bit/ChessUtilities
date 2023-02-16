import fen
import generate

def main():
    demoFen = fen.Fen()
    print(demoFen.getNewFen())
    gen = generate.Generator()
    gen.evaluateArguments()

if __name__ == '__main__':
    main()