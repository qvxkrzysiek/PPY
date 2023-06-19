import wikipediaapi


def read_wiki_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def calculate_average_letter_count(filename):
    total_letters = 0
    total_articles = 0
    unique_letters = set()

    title_generator = read_wiki_titles(filename)
    i = 0
    for title in title_generator:
        i = i + 1
        print(f"Artykuł: {i}")
        article = get_article(title)
        total_articles += 1
        for letter in article:
            if letter.isalpha():
                total_letters += 1
                unique_letters.add(letter.lower())

    average_letter_count = total_letters / total_articles
    return average_letter_count


average = calculate_average_letter_count("C:\\Users\\supse\\Desktop\\small.txt")
print("Średnia liczba liter na artykuł: {:.2f}".format(average))
