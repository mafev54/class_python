class Texts:
    def __init__(self, text):
        self.text = text
        self.quantity = len(self.text)
        self.capital = self.text.upper()
        self.small = self.text.lower()

    def counting_words(self):
        return len(self.text.split())

    def count_characters(self):
        return len(self.text)

    def capital_words(self):
        return self.text.upper()

    def small_words(self):
        return self.text.lower()

    def replace_word(self, replaced, new):
        return self.text.replace(replaced, new)

    def show_info(self):
        print(f"Texto: {self.text}")
        print(f"quantity of words: {self.counting_words()}")
        print(f"quantity of char: {self.count_characters()}")
        print(f"text in capital letters: {self.capital_words()}")
        print(f"small text: {self.small_words()}")
        print(f"replace the word: {self.replace_word('example', 'text')}")


an_example = "hi people, this is a message for you as an example."
a_text = Texts(an_example)
a_text.show_info()
modified_text = a_text.replace_word("example", "text")


class Paragraph(Texts):
    def __init__(self, text, orthography):
        super().__init__(text)
        self.orthography = orthography

    def check_orthography(self):
        return f"This text has a good {self.orthography}."


e1 = ("hi")
instantiate = Paragraph(e1, "orthography")
instantiate.show_info()
print(instantiate.check_orthography())
