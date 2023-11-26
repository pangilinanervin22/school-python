import random

array_of_questions = [
    {
        "question": "Java and JavaScript are the same programming language.",
        "answer": "B",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "How many bits are in a byte.",
        "answer": "D",
        "choices": ["A. 16", "B. 2", "C. 12", "D. 8"],
    },
    {
        "question": "What is the brain of the computer.",
        "answer": "D",
        "choices": ["A. Motherboard", "B. RAM", "C. ROM", "D. CPU"],
    },
    {
        "question": '"ILOVEYOU virus" was created by a Chinese.',
        "answer": "B",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "__________ is used for making web pages interactive.",
        "answer": "D",
        "choices": ["A. HTML", "B. CSS", "C. XML", "D. JavaScript"],
    },
    {
        "question": "IT in computers stands for intelligent technology.",
        "answer": "B",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "____ is used for describing and styling the presentation of Web pages.",
        "answer": "D",
        "choices": ["A. CIA", "B. SSC", "C. XML", "D. CSS"],
    },
    {
        "question": "Flash drive is used for storing and transferring data.",
        "answer": "A",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "ML in computer science stands for _______________.",
        "answer": "A",
        "choices": ["A. Machine Learning", "B. Machine Laughing", "C. Monster Learning", "D. Mobile Legends"],
    },
    {
        "question": "__________ is the founder of SpaceX, PayPal, and Tesla.",
        "answer": "A",
        "choices": ["A. Elon Musk", "B. Jeff Bezos", "C. Tim Cook", "D. Donal Trump"],
    },
    {
        "question": "Virus, Worm, Trojan, and SpyWare are examples of malware.",
        "answer": "A",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "Python, Java, and C++ are examples of programming languages.",
        "answer": "A",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "The first programmer in the world is a woman.",
        "answer": "A",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "The first original name of Java is OAK.",
        "answer": "A",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "White hat hacker is also called a good hacker.",
        "answer": "A",
        "choices": ["A. True", "B. False"],
    },
    {
        "question": "Markup language used for describing the structure of Web pages.",
        "answer": "A",
        "choices": ["A. HTML", "B. CSS", "C. JavaScript", "D. XML"],
    },
    {
        "question": "Device that supplies electric power for a computer.",
        "answer": "A",
        "choices": ["A. Power supply", "B. Motherboard", "C. RAM", "D. CPU"],
    },
    {
        "question": "The father of the computer.",
        "answer": "A",
        "choices": ["A. Charles Babbage", "B. Albert Einstein", "C. Bill Gates", "D. Charles Darwin"],
    },
    {
        "question": "Who is the richest man at the end of 2021.",
        "answer": "A",
        "choices": ["A. Elon Musk", "B. Bill Gates", "C. Jeff Bezos", "D. Mark Zuckerberg"],
    },
    {
        "question": "____ is short for information and communications technology.",
        "answer": "A",
        "choices": ["A. ICT", "B. CIA", "C. CCT", "D. TCI"],
    },
    {
        "question": "Google is an example of ____________.",
        "answer": "A",
        "choices": ["A. Search engine", "B. Cryptocurrency", "C. Operating system", "D. Internet"],
    },
    {
        "question": "TikTok originated in __________.",
        "answer": "A",
        "choices": ["A. China", "B. USA", "C. India", "D. Philippines"],
    },
    {
        "question": "Java was invented by __________.",
        "answer": "A",
        "choices": ["A. James Gosling", "B. Elon Musk", "C. Guido van Rossum", "D. James Bond"],
    },
    {
        "question": "Binary number is a set of _______? ",
        "answer": "A",
        "choices": ["A. 0s and 1s", "B. 2s and 0s", "C. 1s and 2s", "D. any number"],
    },
    {
        "question": "What is the heart of the computer?",
        "answer": "A",
        "choices": ["A. Power Supply", "B. GPU", "C. CPU", "D. Motherboard"],
    },
    {
        "question": "Who is the CEO of Facebook?",
        "answer": "A",
        "choices": ["A. Mark Zuckerberg", "B. Bill Gates", "C. Tim Cook", "D. Warren Buffet"],
    },
    {
        "question": "USB stands for ___________?",
        "answer": "A",
        "choices": ["A. Universal Serial Bus", "B. Universal Cereal Bus", "C. United Serial Bass", "D. none of the above"],
    },
    {
        "question": "What was invented by Linus Torvalds?",
        "answer": "A",
        "choices": ["A. Linux", "B. Microsoft", "C. Ubuntu", "D. macOS"],
    },
    {
        "question": "What kind of language is HTML?",
        "answer": "A",
        "choices": ["A. Markup language", "B. Programming language", "C. Scripting language", "D. Structured query language"],
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
