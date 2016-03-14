def get_questions():
    questions, answers = [], []
    with open('read_questions_ask_user.txt') as f:
        for i, line in enumerate(f):
            answers.append(line.strip()) if i % 2 else questions.append(line)
    return zip(questions, answers)