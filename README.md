# Twitter LLM Feed

## Dependencies

### Creating environment

```
conda create -n feed python=3.10
```

### Activating environment

```
conda activate feed
```

### Installing dependencies

```
pip3 install -r requirements.txt
```

## Running the server

```
python3 server.py
```

## Getting following list
Navigate to your following list: https://twitter.com/{username}/following and run the `get_following_list.py` script. This will log the users you are following.