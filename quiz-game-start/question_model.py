# Important of this model is easier to manage and manipulate quiz data
class Question:
    def __init__(self, q_text, q_answer, q_category):
        self.answer = q_answer
        self.text = q_text
        self.category = q_category

