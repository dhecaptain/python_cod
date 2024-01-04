from difflib import SequenceMatcher

text1="My name is David Wambua"
text2="Hi, my name is David Wambua"
sequenceScore=SequenceMatcher(None,text1,text2).ratio()
print(f"Both are {sequenceScore * 100}% similar")