sys_prompt= '''You are a highly personalized content filter for a user of Twitter.  You want to help your user not get into time sinks by perceiving their feed for them and representing them in a way that objectively shows the purpose and content of the tweet.  You are aware of how social media uses Skinner boxes to keep users, and you want to be the filter that protects your user from that.'''

prompt = '''I'm on twitter to see ideas that are relevant to my current work. I don't want to be nerd-sniped by things that aren't relevant though. Judge on the content rather than the presentation of these.

These are some of the things that I'm interested in:
{positive_prompt}

I'm NOT interested in:
{negative_prompt}

I want you to look at the following tweet and reason whether or not I should see it. Be very critical and sure if you decide to reccomend something to the user. They don't have time to waste.

Tweet
```
{tweet}
```

IMPORTANT: After you think about the tweet concisely, end with an '###' THEN a 'Yes' or 'No' ONLY
'''

example_tweet = '''Jim Fan
@DrJimFan
Chatbot Arena is a unique LLM benchmark that
(1) captures the elusive "in-the-wild vibe" to some degree;
(2) live updated and adaptive;
(3) relatively hard to game.
It works like democracy: people vote for their preferred models on the prompts they actually care about. Unlike traditional benchmarks, it is difficult to "train on the test set" or overfit a particular prompt distribution. Arena is scalable by design: its accuracy improves as more models and users participate.

ELO score is another clever metric. Just like in chess tournaments, difference in ELO score reflects how consistently a model A's response is better than model B given the same prompt. Unlike static benchmarks that lose potency over time, ELO score cannot be saturated. GPT-9 and Gemini-8 might both score 99.9% on MMLU, but they will still have meaningful ELO scores that show their relative strengths.

There are limitations to this Arena approach:
(1) Noisy: many people are just lazy to examine the outputs carefully.
(2) Biased: the democracy is not representative of the general population. It's skewed to people who know what HuggingFace is.
(3) Hard to evaluate certain capabilities: for example, it's really difficult to rank a model's coding skills by human preferences. More automated ways are better, e.g. with compiler in the loop.

It's remarkable that both Mistral's commercial model (Medium) and open-source one (Mixtral-8x7B) climb the ranks this rapidly. Would love to see more players in the Arena!

LMSys ranking on HuggingFace: https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
Chat & vote here: https://chat.lmsys.org
'''