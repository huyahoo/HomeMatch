## Environment

Create Virtual Environment & Install required packages
``` bash
cd HomeMatch
chmod +x setup.sh
./setup.sh
```

Install Rust Complier if error is ocurred when installing `tiktoken` 
``` bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

Verify if successfully installed, then then install again
``` bash
rustc --version
./setup.sh
```

Create .env to store your OPEN_API_key
``` bash
cd HomeMatch
touch .env
echo "OPENAI_API_KEY=your_openai_api_key" >> .env
```

## Synthetic Data Generation
``` bash
python3 src/generate_listings.py
```
Data will be saved into [data/listings.json](data/listings.json)

## Semantic Search

1. Creating a Vector Database and Storing Listings

``` bash
python3 src/vector_db.py
```
Data will be saved into [db](db)

2. Semantic Search of Listings Based on Buyer Preferences
- Create a Buyer Preferences Interface
``` bash
python3 src/user_preferences.py
```

- Search Listings Based on Buyer Preferences
``` bash
python3 src/search_listings.py
```

## Augmented Response Generation
``` bash
python3 src/augment_listings.py
```

