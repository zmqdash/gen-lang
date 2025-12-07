# VOWELS
SHORT_VOWELS = ["a", "e", "i", "o", "u"]
LONG_VOWELS  = ["ā", "ē", "ī", "ō", "ū"]
REDUCED_VOWELS = ["ə"]

VOWELS = SHORT_VOWELS + LONG_VOWELS + REDUCED_VOWELS

# Gutturals (split into natural groups)
LARYNGEALS = ["ʔ", "h"]
PHARYNGEALS = ["ḥ", "ʕ"]
GUTTURALS = LARYNGEALS + PHARYNGEALS

# Stops and fricatives
LABIALS = ["p", "b", "f", "v"]
DENTALS = ["t", "d", "ṯ", "ḏ"]
VELARS = ["k", "g", "kh", "gh"]
STOPS_AND_FRICATIVES = LABIALS + DENTALS + VELARS

# Emphatics
EMPHATICS = ["ṭ", "ṣ", "q"]

# Other groups
SIBILANTS = ["s", "z", "š"]
NASALS = ["m", "n"]
LIQUIDS = ["l", "r"]
GLIDES = ["y", "w"]

# FULL INVENTORY
CONSONANTS = (
    GUTTURALS +
    STOPS_AND_FRICATIVES +
    EMPHATICS +
    SIBILANTS +
    NASALS +
    LIQUIDS +
    GLIDES
)

print(LABIALS[3])