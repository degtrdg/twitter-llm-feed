from helper import evaluate_tweet
from prompts import prompt


positive_prompt= '''- Startup advice
- Stories about his kids (ex. his 11 yo)"
'''

negative_prompt = '''- Politics, culture, drama, news
    - Basically, things that I have no control over and won't help me
- Content made to catch my attention
    - If it's intended to make me click I don't want to.
'''

tweet = f'User: {"paulg"} ' + '''"Sunday night: Me: Well, you managed to spend the whole day in the pyjamas you slept in last night. That's an achievement. 11 yo: You think I haven't done this before?"'''
# tweet = '''"Sunday night: Me: Well, you managed to spend the whole day in the pyjamas you slept in last night. That's an achievement. 11 yo: You think I haven't done this before?"'''

formatted_prompt = prompt.format(
    positive_prompt=positive_prompt, # Excel cells start with ' or " for bulleted lists
    negative_prompt=negative_prompt,
    tweet=tweet
)
print(formatted_prompt)
print(evaluate_tweet(formatted_prompt))