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

PHONEME_GROUPS = {
    "VOWELS": VOWELS,
    "GUTTURALS": GUTTURALS,
    "LABIALS": LABIALS,
    "DENTALS": DENTALS,
    "VELARS": VELARS,
    "SIBILANTS": SIBILANTS,
    "NASALS": NASALS,
    "LIQUIDS": LIQUIDS,
    "GLIDES": GLIDES
}

def classify_phonemes(word: str):
    results = {group: [] for group in PHONEME_GROUPS}

    # multi-character phonemes like "kh", "gh", "ṭ", "ṣ"
    # must be checked first because Hebrew has digraphs.
    i = 0
    while i < len(word):
        # check for two-character phonemes first
        if i + 1 < len(word) and word[i:i+2] in VELARS:
            phoneme = word[i:i+2]
            i += 2
        else:
            phoneme = word[i]
            i += 1

        # match the phoneme to its group(s)
        for group, members in PHONEME_GROUPS.items():
            if phoneme in members:
                results[group].append(phoneme)

    return {group: values for group, values in results.items() if values}


