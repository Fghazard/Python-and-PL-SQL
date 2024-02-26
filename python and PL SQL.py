class MiniTermFragmentGenerator:
    def __init__(self, relations):
        self.relations = relations

    def generate_mini_term_fragments(self, predicates):
        mini_term_fragments = []

        for predicate in predicates:
            for relation in self.relations:
                if relation in predicate:
                    mini_term_fragments.append((relation, predicate))

        return mini_term_fragments

# Example usage
relations = ['A', 'B', 'C']
predicates = ['A.X = 1', 'B.Y > 5', 'C.Z < 10']

generator = MiniTermFragmentGenerator(relations)
mini_terms = generator.generate_mini_term_fragments(predicates)

for fragment in mini_terms:
    print(fragment)