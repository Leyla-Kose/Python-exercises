import re
def text_analyzer(file):
  words = re.split(' |\n', file) 
  word_count = len(words) - words.count('.')
  sentences = re.split('\. |\n', file)
  sentence_count = len(sentences) - sentences.count('')
  average_length_sentence = word_count // sentence_count
  return average_length_sentence

f1 = open('text1.txt', 'r')
print('text1.txt is opened')
t1 = f1.read()
f1.close()
print('text1.txt is closed')

f2 = open('text2.txt', 'r')
print('text2.txt is opened')
t2 = f2.read()
f2.close()
print('text2.txt is closed')

print(f'{text_analyzer(t1)}, {text_analyzer(t2)}')

short_sentences = 'Hemingway'
long_sentences = 'Charles Dickens'

if text_analyzer(t1) > text_analyzer(t2):
  print(f'The first text belongs to {long_sentences} and the second one belongs to {short_sentences}.')
else:
  print(f'The first text belongs to {short_sentences} and the second one belongs to {long_sentences}.')
