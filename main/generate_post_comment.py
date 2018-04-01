import random
base = 'abcdefghijklmnopqrstuvwxyz'

def post_generator():
	text_word = random.randint(1,20)
	post = ''
	for i in range(text_word):
		word = ''
		word_len = random.randint(1,10)
		for j in range(word_len):
			word += base[random.randint(0,len(base)-1)]
		post += word + ' '
		
	return post

def comment_generator():
	while True:
		comment = post_generator()
		if len(comment) <= 100:
			return comment

