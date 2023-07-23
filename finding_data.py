import re
import spacy
from geotext import GeoText

def extract_bacteria_names(text):
    # Regular expression pattern for bacteria names
    pattern = r'\b(?:[A-Z][a-z]+(?: [a-z]+)?(?: [a-z]+)?)\b'

    # Extract bacteria names using the pattern and convert to a set to remove duplicates
    bacteria_names = set(re.findall(pattern, text))
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    geolocations = set([ent.text for ent in doc.ents if ent.label_ == "GPE"])
    print(geolocations)

    #print(bacteria_names)

    names_id_pairs = checking(bacteria_names)

    return names_id_pairs, geolocations

def is_bacterium_name(name_class):
    # Function to check if a name is a bacterium name based on name class.
    # You can customize this function based on your specific name class for bacteria.
    return name_class == "scientific name"

def checking(words_to_check):
    # Step 1: Read the names.dmp file and extract bacterium names and taxonomy IDs
    file_path = "C:/Users/Настя/PycharmProjects/Summer/taxdump/names.dmp"  # Replace with the actual file path
    bacterium_info = []  # List to store pairs of Taxonomy ID and bacterium names

    with open(file_path, "r", encoding="utf-8") as names_file:
        for line in names_file:
            components = line.strip().split("|")
            tax_id = components[0].strip()
            name = components[1].strip()
            name_class = components[3].strip()

            # Check if the name is a bacterium name based on name class
            if is_bacterium_name(name_class):
                bacterium_info.append((tax_id, name))

    # Step 2: Search for words in the bacterium names and create pairs
    pairs = []
    for word in words_to_check:
        lowercase_word = word.lower()
        for tax_id, name in bacterium_info:
            if lowercase_word == name.lower():
                pairs.append((tax_id, name))
                break  # Stop searching once a match is found to avoid duplicates

    return pairs