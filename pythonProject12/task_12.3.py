def dictionary(input_file, output_file):
    ru_en_dict = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:

            if ' - ' in line:
                english, russian = line.strip().split(' - ')
                rus_worlds = russian.split(', ')

                for term in rus_worlds:
                    term = term.strip()
                    if term in ru_en_dict:
                        ru_en_dict[term].append(english)
                    else:
                        ru_en_dict[term] = [english]

    with open(output_file, 'w', encoding='utf-8') as f:
        for rus_term in sorted(ru_en_dict.keys()):
            eng_terms = ', '.join(sorted(ru_en_dict[rus_term]))
            f.write(f"{rus_term} – {eng_terms}\n")

input_file = 'en-ru.txt'
output_file = 'ru-en.txt'

dictionary(input_file, output_file)
print("Словарь успешно создан!")