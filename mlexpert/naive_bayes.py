def probability_of_tag_given_vector(vector, corpus):
    unique_tags = corpus.keys()

    total_num_documents = total_num_documents_in_train(corpus, unique_tags)
    prob_tags = prob_for_each_tag(corpus, total_num_documents, unique_tags)

    prob_vector_given_tag_map = {}
    for tag in unique_tags:
        prob_vector_given_tag = calc_prob_vector_given_tag(tag, vector, corpus)
        prob_vector_given_tag_map[tag] = prob_vector_given_tag

    prob_vector_given_not_tag_map = {}
    for tag in unique_tags:
        prob_vector_given_not_tag = calc_prob_vector_given_not_tag(tag, vector, corpus)
        prob_vector_given_not_tag_map[tag] = prob_vector_given_not_tag

    prob_tag_given_vector_map = {}
    for tag in unique_tags:
        prob_tag_given_vector = (
                                        prob_vector_given_tag_map[tag] * prob_tags[tag]
                                ) / (
                                        prob_vector_given_tag_map[tag] * prob_tags[tag] +
                                        prob_vector_given_not_tag_map[tag] * (1 - prob_tags[tag])
                                )
        prob_tag_given_vector_map[tag] = prob_tag_given_vector

    return prob_tag_given_vector_map


def calc_prob_vector_given_tag(tag, vector, corpus):
    documents_for_tag = corpus[tag]

    num_matches = 0
    for document in documents_for_tag:
        if vector in document:
            num_matches += 1

    return num_matches / len(documents_for_tag)


def calc_prob_vector_given_not_tag(tag, vector, corpus):
    documents_from_other_tags = sum([v for k, v in corpus.items() if k != tag], [])

    num_matches = 0
    for document in documents_from_other_tags:
        if vector in document:
            num_matches += 1

    return num_matches / len(documents_from_other_tags)


def prob_for_each_tag(corpus, total_num_documents, unique_tags):
    prob_tags = {}
    for tag in unique_tags:
        prob_tag = [len(v) / total_num_documents for k, v in corpus.items() if k == tag]
        prob_tags[tag] = prob_tag[0]
    return prob_tags


def total_num_documents_in_train(corpus, unique_tags):
    total_num_documents = 0
    for tag in unique_tags:
        total_num_documents += len(corpus[tag])
    return total_num_documents


class MultinomialNB:
    def __init__(self, articles_per_tag):
        # Don't change the following two lines of code.
        self.articles_per_tag = articles_per_tag  # See question prompt for details.
        # self.train()

    def train(self):
        prob_tag_given_vector_map = probability_of_tag_given_vector("article", self.articles_per_tag)
        print(prob_tag_given_vector_map)
        pass

    def predict(self, article):
        # Write your code here.
        pass


def main():
    articles_per_tag = {
        "politics": [
            ["article", "writes", "Joel", "Furr", "writes"],
            ["Distribution", "world", "following", "posted"]
        ],
        "sports": [
            ["article", "writes", "just", "wanted"],
            ["Phillies", "salvaged", "their", "weekend", "article"]
        ],
        "tech": [
            ["Thanks", "Steve", "your", "helpful"],
            ["Please", "unsubscribe", "This", "user"]
        ]
    }
    multinomial_nb = MultinomialNB(articles_per_tag)
    multinomial_nb.train()


if __name__ == '__main__':
    main()

# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         article = [
#             "article",
#             "writes",
#             "while",
#             "when",
#             "owned",
#             "Plus",
#             "wanted",
#             "upgrade",
#             "memory",
#             "just",
#             "ordered",
#             "toolkit",
#             "from",
#             "Macwarehouse",
#             "something",
#             "like",
#             "included",
#             "antistatic",
#         ]
#         expected = {"politics": -17.8298, "sports": -24.5914, "tech": -13.5427}
#
#         articles_per_tag = {
#             "politics": [
#                 ["article", "writes", "Joel", "Furr", "writes"],
#                 ["Distribution", "world", "following", "posted"]
#             ],
#             "sports": [
#                 ["article", "writes", "just", "wanted"],
#                 ["Phillies", "salvaged", "their", "weekend"]
#             ],
#             "tech": [
#                 ["Thanks", "Steve", "your", "helpful"],
#                 ["Please", "unsubscribe", "This", "user"]
#             ]
#         }
#         multinomial_nb = MultinomialNB(articles_per_tag)
#         multinomial_nb.train()
#         actual = multinomial_nb.predict(article)
#         print(actual)
