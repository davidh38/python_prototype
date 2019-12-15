from source.calculator import calculation
from source.config import read

if __name__ == "__main__":
    mycalc = calculation(1,3)
    yml_config = read()
    print(yml_config["test"]["key"])
    print(f"hello world {mycalc} {yml_config['test']['key']}")


