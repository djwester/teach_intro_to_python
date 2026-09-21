"""Mad Libs: Funny Story Creation Game

Exercises:

1. How to replace the story?
2. How load the story and from a file?
3. How to add additional parts of speech?
"""

# The quick brown fox jumps over the lazy dog.
template = 'The |adjective| |adjective| |noun| |verb| over the |adjective| |noun|. '

chunks = []

for chunk in template.split('|'):
    if chunk.endswith(' '):
        chunks.append(chunk)
    else:
        prompt = 'Enter [{}]: '.format(chunk)
        word = input(prompt)
        chunks.append(word)
        

print('=' * 80)
story = ''.join(chunks)
print(story)
