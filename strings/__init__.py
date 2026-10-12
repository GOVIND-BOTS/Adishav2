
import os
import yaml

languages = {}
languages_present = {}

LANG_DIR = "./strings/langs/"


def get_string(lang: str):
    return languages[lang]


# Load English language first
with open(os.path.join(LANG_DIR, "en.yml"), encoding="utf8") as file:
    languages["en"] = yaml.safe_load(file)

if not isinstance(languages["en"], dict) or "name" not in languages["en"]:
    raise ValueError("strings/langs/en.yml is invalid or missing the 'name' field.")

languages_present["en"] = languages["en"]["name"]

# Load other YAML language files
for filename in os.listdir(LANG_DIR):
    if not filename.endswith(".yml"):
        continue

    language_name = filename[:-4]

    if language_name == "en":
        continue

    file_path = os.path.join(LANG_DIR, filename)

    try:
        with open(file_path, encoding="utf8") as file:
            language_data = yaml.safe_load(file)

        if not isinstance(language_data, dict):
            raise ValueError("File is empty or does not contain valid YAML data.")

        # Fill missing translations from English
        for item, value in languages["en"].items():
            if item not in language_data:
                language_data[item] = value

        if "name" not in language_data:
            raise ValueError("Missing the 'name' field.")

        languages[language_name] = language_data
        languages_present[language_name] = language_data["name"]

    except Exception as error:
        raise ValueError(
            f"Language file '{filename}' has an issue: {error}"
        ) from error
