import unittest


def probability_of_category_given_vector():
    pass


class MultinomialNB:
    def __init__(self, articles_per_tag):
        # Don't change the following two lines of code.
        self.articles_per_tag = articles_per_tag  # See question prompt for details.
        self.train()

    def train(self):
        unique_tags = self.articles_per_tag.keys

        for tag in unique_tags:
            probability_of_category_given_vector(tag, self.ar)
        pass

    def predict(self, article):
        # Write your code here.
        pass


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        article = [
            "article",
            "writes",
            "while",
            "when",
            "owned",
            "Plus",
            "wanted",
            "upgrade",
            "memory",
            "just",
            "ordered",
            "toolkit",
            "from",
            "Macwarehouse",
            "something",
            "like",
            "included",
            "antistatic",
        ]
        expected = {"politics": -17.8298, "sports": -24.5914, "tech": -13.5427}

        articles_per_tag = {
            "politics": [
                ["article", "writes", "Joel", "Furr", "writes"],
                ["Distribution", "world", "following", "posted"]
            ],
            "sports": [
                ["article", "writes", "just", "wanted"],
                ["Phillies", "salvaged", "their", "weekend"]
            ],
            "tech": [
                ["Thanks", "Steve", "your", "helpful"],
                ["Please", "unsubscribe", "This", "user"]
            ]
        }
        multinomial_nb = MultinomialNB(articles_per_tag)
        multinomial_nb.train()
        actual = multinomial_nb.predict(article)
        print(actual)
