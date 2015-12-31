import questions_model as qm
import tkinter as tk
class User:
	def __init__(self,name):
		self.name = name
		self.score = 0
		self.level = 0

	def update_score(self,amount):
		self.score += amount

	def set_name(self, new_name):
		self.name = new_name

	def update_level(self, amount):
		self.level += amount

class MainQuizApp:
	def __init__(self, questions_file='questions.csv'):
		self.questions_file = questions_file
		
		self.root = tk.Tk()
		self._build_gui()
		self.current_question_index=0
		self.user_answer = tk.IntVar()
		# self.user = self._create_user()
		self.root.mainloop()

	# def _get_next_question(self):
	# 	for question_line in self.questions:
	# 		yield question_line
	def get_question(self):
		# print(self.questions[self.current_question_index])
		return self.questions[self.current_question_index][0]

	def get_options(self):
		print(self.current_question_index)
		print(self.questions[self.current_question_index])
		return self.questions[self.current_question_index][1:-1]

	def get_current_answer(self):
		return self.questions[self.current_question_index][-1]

	def start(self):
		self.questions = qm.get_questions(self.questions_file)
		current_question = self.get_question()
		self._update_question(current_question)
		options = self.get_options()
		self._make_options(options)

	def is_answer_correct(self):
		return self.get_current_answer() == self.get_options()[self.user_answer.get()-1]

	def _update_answer_label(self):
		status = 'correct' if self.is_answer_correct() else 'wrong'
		if status == 'wrong':
			status += ' correct answer: {}'.format(self.get_current_answer())
		self.answer_label.config(text=status)

	def _update_questions_remaining(self):
		pass

	def _update_question(self,question):
		self.questions_label.config(text=question)

	def get_next_question(self):
		self.current_question_index += 1
		if self.current_question_index == len(self.questions):
			return
			
		else:
			self._update_questions_remaining()
		self._update_question(self.get_question())
		self._update_options(self.get_options())

	def check_and_update(self):
		self._update_answer_label()
		self.root.after(100,self.get_next_question)
		# self.get_next_question()


	def _build_gui(self):
		self.user_answer = tk.IntVar()
		self.questions_box = tk.Frame(self.root)
		
		self.questions_label = tk.Label(self.questions_box)
		self.questions_label.grid(row=0)
		self.option_buttons = []
		self.answer_label = tk.Label(self.questions_box)
		self.answer_label.grid(row=5)

		self.submit_button = tk.Button(self.questions_box, text="Submit",command=self.check_and_update)
		self.submit_button.grid(row=5,column=1)
		self.questions_box.grid(row=0,column=0)

		self.side_box = tk.Frame(self.root)
		self.start_button = tk.Button(self.side_box, text="Start", command=self.start)
		self.start_button.grid(row=0)
		self.next_button = tk.Button(self.side_box, text="Next")
		self.next_button.grid(row=1)
		self.side_box.grid(row=0,column=1)

	def _make_options(self,options_list):
		for option,index in zip(options_list,range(len(options_list))):
			self.option_buttons.append(tk.Radiobutton(self.questions_box, text=option, value=index+1, variable=self.user_answer))
			self.option_buttons[-1].grid(row=index+1)

	def _update_options(self,options_list):
		self.user_answer.set(7)
		for option_button,option,index in zip(self.option_buttons,options_list,range(len(options_list))):
			option_button.config(text=option, value=index+1)





if __name__ == '__main__':
	MainQuizApp()


