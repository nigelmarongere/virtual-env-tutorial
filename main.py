import random

def fun_fact_about_honey():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "Honey is the only food that includes all the substances necessary to sustain life, including enzymes, vitamins, minerals, and water.",
        "Bees must visit approximately 2 million flowers to make just one pound of honey.",
        "Honey has natural antibacterial and antifungal properties, making it a popular remedy for sore throats and wounds.",
        "There are over 300 unique types of honey in the United States, each originating from a different floral source."
    ]
    print(random.choice(facts))

if __name__ == "__main__":
    fun_fact_about_honey()