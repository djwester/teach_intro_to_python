"""Mad Libs: Funny Story Creation Game

Exercises:

1. How to replace the story?
2. How to load the story from a file?
"""
import random
# The quick brown fox jumps over the lazy dog.
template = 'The |adjective| |adjective| |noun| |verb| over the |adjective| |noun|. '

# The cow jumped over the moon
template = 'The |noun| |verb| '
chunks = []

for chunk in template.split('|'):
    if chunk.endswith(' '):
        chunks.append(chunk)
    else:
        word = input(f"Enter an [{chunk}] ")
        chunks.append(word)
        

print('=' * 80)
story = ''.join(chunks)
print(story)
