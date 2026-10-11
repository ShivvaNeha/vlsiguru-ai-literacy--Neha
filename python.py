
"""
Week 01: AI Literacy Learning Helper

This program explains common AI concepts using predefined
examples and simple rules.

It is traditional rule-based software, not a machine-learning model.
"""

AI_CONCEPTS = {
    "Artificial Intelligence": {
        "meaning": "Computer systems performing tasks associated with intelligence.",
        "example": "An AI assistant answering questions."
    },
    "Machine Learning": {
        "meaning": "Systems learning patterns from data.",
        "example": "A spam filter trained on email examples."
    },
    "Deep Learning": {
        "meaning": "Machine learning using multilayer neural networks.",
        "example": "A model recognising objects in images."
    },
    "Generative AI": {
        "meaning": "AI that generates new content.",
        "example": "An AI tool generating Python code."
    }
}


def display_concepts():
    """Display AI concepts and their examples."""
    print("=== AI Literacy Learning Helper ===\n")

    for concept, details in AI_CONCEPTS.items():
        print(f"Concept: {concept}")
        print(f"Meaning: {details['meaning']}")
        print(f"Example: {details['example']}")
        print("-" * 50)


def main():
    display_concepts()

    print("\nLearning tip:")
    print("Always verify AI-generated information using reliable sources.")
    print("This program uses predefined information, not machine learning.")


if __name__ == "__main__":
    main()
