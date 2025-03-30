from linear_algebra import ComplexNumber

def main():
    print("Hello from learning-theory!")
    c: ComplexNumber = ComplexNumber(1, 1)
    d: ComplexNumber = c.conjugate()
    print(c, d)
    print(c.to_polar())


if __name__ == "__main__":
    main()
