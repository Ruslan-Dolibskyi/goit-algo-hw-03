import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли за розширенням.")
    parser.add_argument("-s", "--source", type=Path,
                        required=True, help="Шлях до вихідної папки")
    parser.add_argument("-d", "--destination", type=Path,
                        default=Path("dist"), help="Шлях до папки призначення")
    return parser.parse_args()


def recursive_copy(source: Path, destination: Path):
    try:
        for element in source.iterdir():
            if element.is_dir():
                recursive_copy(element, destination)
            else:
                file_extension = element.suffix
                folder = destination / file_extension
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy(element, folder)
    except PermissionError as e:
        print(f"Помилка доступу: {e}")
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")


def main():
    args = parse_argv()
    recursive_copy(args.source, args.destination)


if __name__ == "__main__":
    main()