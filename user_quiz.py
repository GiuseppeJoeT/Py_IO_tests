# Define two empty lists on the same line to hold our questions and answers.
def get_questions():
    questions, answers = [], []
    with open('read_questions_ask_user.txt') as f:
        for i, line in enumerate(f):
            answers.append(line.strip()) if i % 2 else questions.append(line)
    return zip(questions, answers)
    # The zip function is a useful way of merging two lists into one

'''
If we just wanted to iterate through the lines in the file, we could use for
line in f , but we also want the line number, so that we can see whether the line is a
question (odd number) or answer(even number). The way to do this is to use the
enumerate keyword - now we are returning the line and the line number.
'''

'''
Here’s a simple program that asks those questions, and counts the number
of questions correctly answered:
'''
questions = get_questions()
score = 0
total = len(questions)

for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score += 1
print 'You got %s of %s questions right' % (score, total)