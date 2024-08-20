from pathlib import Path

def get_cats_info(path: str) -> str:
    cats_info = []

    try:
        with open(path, "r", encoding="utf=8") as file:
            for line in file:
                line = line.strip()
                cats_split = line.split(',')

                if len(cats_split) == 3:
                    cat_dict = {
                        "id": cats_split[0],
                        "name": cats_split[1],
                        "age": cats_split[2]
                    }
                    cats_info.append(cat_dict)

        return cats_info


    except FileNotFoundError:

        print("File not found")

        return []

    except Exception as e:

        print(f"An error occurred: {e}")

        return []

cats_info = get_cats_info("./cats.txt")
print(cats_info)

