import random

array_of_questions = [
    {
        "question": "Java and JavaScript are the same programming language.",
        "answer": "False",
        "choices": ["True", "False"],
    },
    {
        "question": "How many bits are in a byte.",
        "answer": "8",
        "choices": ["16", "2", "12", "8"],
    },
    {
        "question": "What is the brain of the computer.",
        "answer": "CPU",
        "choices": ["Motherboard", "RAM", "ROM", "CPU"],
    },
    {
        "question": '"ILOVEYOU virus" was created by a Chinese.',
        "answer": "False",
        "choices": ["True", "False"],
    },
    {
        "question": "__________ is used for making web pages interactive.",
        "answer": "JavaScript",
        "choices": ["HTML", "CSS", "XML", "JavaScript"],
    },
    {
        "question": "IT in computers stands for intelligent technology.",
        "answer": "False",
        "choices": ["True", "False"],
    },
    {
        "question": "____ is used for describing and styling the presentation of Web pages.",
        "answer": "CSS",
        "choices": ["CIA", "SSC", "XML", "CSS"],
    },
    {
        "question": "Flash drive is used for storing and transferring data.",
        "answer": "True",
        "choices": ["True", "False"],
    },
    {
        "question": "ML in computer science stands for _______________.",
        "answer": "Machine Learning",
        "choices": ["Machine Learning", "Machine Laughing", "Monster Learning", "Mobile Legends"],
    },
    {
        "question": "__________ is the founder of SpaceX, PayPal, and Tesla.",
        "answer": "Elon Musk",
        "choices": ["Elon Musk", "Jeff Bezos", "Tim Cook", "Donal Trump"],
    },
    {
        "question": "Virus, Worm, Trojan, and SpyWare are examples of malware.",
        "answer": "True",
        "choices": ["True", "False"],
    },
    {
        "question": "Python, Java, and C++ are examples of programming languages.",
        "answer": "True",
        "choices": ["True", "False"],
    },
    {
        "question": "The first programmer in the world is a woman.",
        "answer": "True",
        "choices": ["True", "False"],
    },
    {
        "question": "The first original name of Java is OAK.",
        "answer": "True",
        "choices": ["True", "False"],
    },
    {
        "question": "White hat hacker is also called a good hacker.",
        "answer": "True",
        "choices": ["True", "False"],
    },
    {
        "question": "Markup language used for describing the structure of Web pages.",
        "answer": "HTML",
        "choices": ["HTML", "CSS", "JavaScript", "XML"],
    },
    {
        "question": "Device that supplies electric power for a computer.",
        "answer": "Power supply",
        "choices": ["Power supply", "Motherboard", "RAM", "CPU"],
    },
    {
        "question": "The father of the computer.",
        "answer": "Charles Babbage",
        "choices": ["Charles Babbage", "Albert Einstein", "Bill Gates", "Charles Darwin"],
    },
    {
        "question": "Who is the richest man at the end of 2021.",
        "answer": "Elon Musk",
        "choices": ["Elon Musk", "Bill Gates", "Jeff Bezos", "Mark Zuckerberg"],
    },
    {
        "question": "____ is short for information and communications technology.",
        "answer": "ICT",
        "choices": ["ICT", "CIA", "CCT", "TCI"],
    },
    {
        "question": "Google is an example of ____________.",
        "answer": "Search engine",
        "choices": ["Search engine", "Cryptocurrency", "Operating system", "Internet"],
    },
    {
        "question": "TikTok originated in __________.",
        "answer": "China",
        "choices": ["China", "USA", "India", "Philippines"],
    },
    {
        "question": "Java was invented by __________.",
        "answer": "James Gosling",
        "choices": ["James Gosling", "Elon Musk", "Guido van Rossum", "James Bond"],
    },
    {
        "question": "Binary number is a set of _______? ",
        "answer": "0s and 1s",
        "choices": ["0s and 1s", "2s and 0s", "1s and 2s", "any number"],
    },
    {
        "question": "What is the heart of the computer?",
        "answer": "Power Supply",
        "choices": ["Power Supply", "GPU", "CPU", "Motherboard"],
    },
    {
        "question": "Who is the CEO of Facebook?",
        "answer": "Mark Zuckerberg",
        "choices": ["Mark Zuckerberg", "Bill Gates", "Tim Cook", "Warren Buffet"],
    },
    {
        "question": "USB stands for ___________?",
        "answer": "Universal Serial Bus",
        "choices": [
            "Universal Serial Bus",
            "Universal Cereal Bus",
            "United Serial Bass",
            "none of the above",
        ],
    },
    {
        "question": "What was invented by Linus Torvalds?",
        "answer": "Linux",
        "choices": ["Linux", "Microsoft", "Ubuntu", "macOS"],
    },
    {
        "question": "What kind of language is HTML?",
        "answer": "Markup language",
        "choices": [
            "Markup language",
            "Programming language",
            "Scripting language",
            "Structured query language",
        ],
    },
]


def get_random_question():
    index_arr = []
    main_questions = []

    while len(index_arr) != 10:
        rand = random.randint(0, len(array_of_questions) - 1)
        if rand in index_arr:
            continue

        index_arr.append(rand)
        main_questions.append(array_of_questions[rand])

    return main_questions


get_random_question()
