import os
import pickle
from functools import wraps

def memoize_to_file(file_path='memoize_cache.pkl'):
    def decorator(func):
        cache = {}

        # Load existing cache if file exists
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                cache = pickle.load(file)

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if result exists in cache
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                # Call the function and store the result
                result = func(*args, **kwargs)
                cache[key] = result
                with open(file_path, 'wb') as file:
                    pickle.dump(cache, file)
            else:
                print(f"Cache hit for {file_path}!")
            return cache[key]

        return wrapper

    return decorator

if __name__ == '__main__':
    with open('/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/backend/memoize_http', 'rb') as file:
        cache = pickle.load(file)
        print(cache)