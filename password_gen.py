import random
import string

words = [
    "abstruse", "aberration", "abrogate", "abstemious", "acumen", "admonition", "adroit",
    "aesthetic", "affable", "alacrity", "allusion", "ambiguous", "ambivalent", "anachronism",
    "apocryphal", "arcane", "audacious", "auspicious", "belligerent", "blasphemous", "cabalistic",
    "cacophony", "capricious", "catalyst", "cogent", "commensurate", "compelling", "concomitant",
    "conflagration", "conundrum", "corroborate", "cryptic", "deference", "delectable", "deliberate",
    "desultory", "diffident", "discrepancy", "disparate", "divergent", "effervescent", "effulgent",
    "elegant", "elucidate", "enervate", "enthralling", "ephemeral", "equanimity", "equivocate",
    "exquisite", "fallacious", "fatuous", "fleeting", "fractious", "histrionic", "impeccable",
    "impregnable", "incandescent", "incongruous", "inexorable", "inimical", "insidious", "intrepid",
    "invincible", "juxtaposition", "kaleidoscopic", "loquacious", "magnanimous", "magnitude",
    "malfeasance", "mellifluous", "mercurial", "nebulous", "nonplussed", "obdurate", "paradoxical",
    "penultimate", "pervasive", "phlegmatic", "plausible", "precarious", "prodigious", "propitious",
    "quintessential", "recalcitrant", "recondite", "resilient", "sagacious", "salient",
    "sanctimonious", "sanguine", "scintillating", "sequester", "soliloquy", "somnolent", "spurious",
    "stentorian", "sublime", "supercilious", "subliminal", "tantamount", "tedious", "torrid",
    "transitory", "trepidation", "ubiquitous", "unassailable", "unconventional", "unfathomable",
    "untenable", "usurp", "vacuous", "vainglorious", "veracity", "verbose", "veritable",
    "vexatious", "voluptuous", "wanton", "zenith", "abstruse", "adjudicate", "allegory", "ascertain",
    "bifurcate", "cogent", "commensurate", "dichotomy", "debilitate", "disparate", "effervescent",
    "elucidate", "entropic", "epiphany", "equanimity", "esoteric", "exorbitant", "fortuitous",
    "grandiloquent", "heterogeneous", "immutable", "incendiary", "indomitable", "ineffable",
    "inexorable", "intermittent", "introspection", "juxtaposition", "kaleidoscopic", "liberation",
    "munificent", "nefarious", "obfuscate", "omnipotent", "paradigm", "perspicacious",
    "philanthropic", "recalcitrant", "reciprocal", "redolent", "remonstrate", "resilient",
    "salubrious", "sanguine", "serendipity", "soporific", "subterfuge", "surreptitious",
    "transcendent", "turbulent", "venerable", "voracious", "winsome", "zeitgeist", "alleviate",
    "capitulate", "circumspect", "dissonance", "ebullient", "exemplary", "fortuitous",
    "intransigent", "loquacious", "maudlin", "nebulous", "nonchalant", "parsimonious",
    "perfunctory", "philanderer", "precarious", "rhapsodic", "superfluous", "tenacious",
    "transitory", "vacillate", "vicissitude", "voracious", "warranted", "zealous", "abrogate",
    "altruistic", "anathema", "arbitrary", "blatant", "chimerical", "circumlocution", "cogitate",
    "connubial", "contumacious", "cosmopolitan", "cryptic", "dissonant", "ebullient", "euphoric",
    "exorbitant", "fastidious", "fecund", "fervent", "gregarious", "hallowed", "idiosyncratic",
    "impecunious", "intractable", "intrepid", "inveterate", "laconic", "magnanimous", "malignant",
    "narcissistic", "nihilistic", "obfuscate", "opulent", "paradigmatic", "pecuniary", "perpetual",
    "pertinent", "phlegmatic", "prolific", "quintessential", "resilient", "sardonic", "soporific",
    "specious", "stoic", "substantiate", "temerarious", "turbulent", "ubiquitous", "unctuous",
    "verbose", "verdant", "vitriolic", "wily", "zealot", "abstruse", "admonish", "ascetic",
    "bastion", "cacophony", "caveat", "decry", "detract", "eclectic", "exemplary", "flagrant",
    "forbearance", "hyperbole", "incumbent", "ineffable", "intransigent", "invective", "jovial",
    "mendacious", "negligible", "obviate", "palpable", "paragon", "perturb", "polemical",
    "precipitous", "raucous", "recalcitrant", "resilient", "serendipitous", "susceptible",
    "tenacious", "transient", "unfathomable", "vacillate", "vicarious", "wry", "zephyr",
    "abandon", "assiduous", "austere", "banal", "capricious", "circumspect", "conducive",
    "conspicuous", "culpable", "dissonant", "enervated", "ephemeral", "inimical", "inscrutable",
    "inveterate", "mellifluous", "narcissistic", "omnipotent", "paradox", "pedantic",
    "pervasive", "reclusive", "resilient", "sanguine", "satirical", "scintillating", "sophisticated",
    "transient", "ubiquitous", "venerable", "vexing", "voracious", "wary", "zealous"
]

# ASCII characters and special symbols
ascii_symbols = "!?.,-@#$%^&*()_+=<>/{}[]|:;~`"
ascii_characters = string.ascii_letters + string.digits + ascii_symbols

# Non-ASCII characters from various languages
non_ascii_characters = (
    '你好你好'  # Chinese
    'こんにちはこんにちは'  # Japanese
    '안녕하세요안녕하세요'  # Korean
    'ЗдравствуйтеЗдравствуйте'  # Russian
    'αβγδεζηθικλμνξοπρστυφχψωαβγδεζηθικλμνξοπρστυφχψω'  # Greek
    'àéèìòùàéèìòù'  # French
    'äöüßäöüß'  # German
    'çãõçãõ'  # Portuguese
    'שלטוןשלטון'  # Hebrew
    'अआइईउऊअआइईउऊ'  # Hindi
    'السلام عليكم'  # Arabic
    'नमस्ते'  # Nepali
    'ਜੀ ਆਇਆਂ ਨੂੰ'  # Punjabi
    'សួស្តី'  # Khmer
    'မင်္ဂလာပါ'  # Burmese
    'ਸਤ ਸ੍ਰੀ ਅਕਾਲ'  # Gurmukhi
    'सुप्रभात'  # Sanskrit
    'สวัสดี'  # Thai
    'Xin chào'  # Vietnamese
    'Witaj'  # Polish
    'Cześć'  # Polish with diacritics
    'Zdravo'  # Serbian Latin
    'नमस्कार'  # Marathi
    'שלום'  # Hebrew (alternative)
    'Добрый день'  # Russian (alternative)
)

def generate_passwords(count=10, min_length=12, max_length=24, use_non_ascii=False):
    if min_length > max_length:
        raise ValueError("min_length cannot be greater than max_length")

    def generate_password(min_length, max_length, characters):
        word = random.choice(words)

        # Randomly capitalize some letters in the word
        word = ''.join(
            char.upper() if random.choice([True, False]) else char
            for char in word
        )

        # Ensure the total length and the number of symbols
        length = random.randint(min_length, max_length)

        min_symbols = 5
        if length < len(word) + min_symbols:
            length = len(word) + min_symbols

        # Calculate the number of symbols and additional characters needed
        num_symbols = min_symbols
        num_additional_chars = length - len(word) - num_symbols

        # Ensure no negative length
        if num_additional_chars < 0:
            num_additional_chars = 0
            num_symbols = length - len(word)

        # Generate required symbols without consecutive repetitions
        def generate_non_repeating_symbols(num_symbols):
            symbol_chars = []
            last_char = ""
            for _ in range(num_symbols):
                new_char = random.choice(characters)
                while new_char == last_char:
                    new_char = random.choice(characters)
                symbol_chars.append(new_char)
                last_char = new_char
            return ''.join(symbol_chars)

        symbol_chars = generate_non_repeating_symbols(num_symbols)
        additional_chars = ''.join(random.choice(characters) for _ in range(num_additional_chars))

        # Combine the word, symbols, and additional characters
        result = list(word)
        combined_chars = list(symbol_chars + additional_chars)
        random.shuffle(combined_chars)

        # Insert symbols and additional characters randomly into the word
        for char in combined_chars:
            result.insert(random.randint(0, len(result)), char)

        # Ensure the final result length is correct
        if len(result) > length:
            result = result[:length]
        elif len(result) < length:
            result += ''.join(random.choice(characters) for _ in range(length - len(result)))

        return ''.join(result)

    characters = ascii_characters if not use_non_ascii else ascii_characters + non_ascii_characters
    return [generate_password(min_length, max_length, characters) for _ in range(count)]

# Generate and print ASCII passwords
ascii_passwords = generate_passwords(use_non_ascii=False)
print("ASCII Passwords:")
for pwd in ascii_passwords:
    print(pwd)

# Generate and print non-ASCII passwords
non_ascii_passwords = generate_passwords(use_non_ascii=True)
print("\nNon-ASCII Passwords:")
for pwd in non_ascii_passwords:
    print(pwd)
