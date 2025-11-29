# Reddit AI Agent Scraper

A Python tool to fetch AI agent ideas, solutions, and problems from Reddit's r/AI_Agent subreddit. Supports both simple read-only access and authenticated API access with higher rate limits.

## Features

- **Dual Authentication Modes**:
  - Read-only mode: No credentials needed, quick start
  - Authenticated mode: Higher rate limits, more reliable for bulk fetches

- **Multiple Fetch Types**:
  - Hot/trending posts
  - New posts
  - Top posts (by time period: hour/day/week/month/year/all)
  - Keyword search

- **Comment Extraction**: Fetch top comments from each post

- **CSV Export**: Export posts and comments to CSV files for analysis

- **Flexible Configuration**: Customizable limits, filters, and search queries

## Project Structure

```
reddit-ai-agent-scraper/
├── app.py                       # 🏠 Streamlit main page (Home)
├── pages/                       # 📑 Streamlit pages (auto-navigation)
│   ├── 2_⚙️_Settings.py        # Configure credentials
│   ├── 3_📊_Fetch_Data.py      # Fetch Reddit posts
│   ├── 4_🔍_View_Data.py       # View & explore data
│   └── 5_📥_Export.py          # Export to CSV/Excel/JSON
│
├── src/
│   ├── reddit_scraper/          # Core scraping functionality
│   │   ├── __init__.py          # Package exports
│   │   ├── scraper.py           # Reddit scraper class
│   │   ├── config.py            # Configuration settings
│   │   ├── models.py            # Pydantic data models
│   │   └── exporter.py          # CSV/Excel export
│   └── streamlit_ui/            # Web UI utilities
│       └── utils/
│           └── session_state.py # Session management
│
├── examples/
│   └── example_usage.py         # Python API examples
│
├── pyproject.toml               # Project dependencies
├── .env                         # API credentials (gitignored)
├── .gitignore
└── README.md
```

### 🧭 How Navigation Works

When you run `streamlit run app.py`, Streamlit **automatically** creates a navigation sidebar with all pages:

- **🏠 Main page** (`app.py`) - Welcome/Home page
- **⚙️ Settings** - Configure Reddit API credentials
- **📊 Fetch Data** - Retrieve posts from Reddit
- **🔍 View Data** - Explore posts and comments
- **📥 Export** - Download data as CSV/Excel/JSON

**Navigation is automatic** - just click the page names in the **left sidebar** to switch between pages!

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-directory>
```

### 2. Create virtual environment and install dependencies

Using `uv` (recommended):
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install praw pandas python-dotenv pydantic
```

Or using standard pip:
```bash
python -m venv .venv
source .venv/bin/activate
pip install praw pandas python-dotenv pydantic
```

## Quick Start

### Option 1: 🌐 Streamlit Web UI (Recommended) - NO CREDENTIALS NEEDED!

The easiest way to use the scraper - **works immediately with zero setup**!

```bash
streamlit run app.py
```

The web app will open in your browser with an intuitive interface:

- **⚙️ Settings**: Choose API mode (JSON or Official)
- **📊 Fetch Data**: Retrieve posts (hot/new/top/search)
- **🔍 View Data**: Explore posts and comments interactively
- **📥 Export**: Download as CSV, Excel, or JSON

**🚀 Instant Start (JSON API - No Setup):**
1. Run `streamlit run app.py`
2. Go to **📊 Fetch Data**
3. Start fetching immediately - **no credentials needed!**

**⚙️ Optional: Advanced Mode (Official API):**
1. Go to Settings → Switch to "Official API" mode
2. Get credentials from [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
3. Enter credentials and test connection
4. Enjoy higher rate limits!

### Option 2: 💻 Python API (Advanced)

For programmatic use and automation:

**A) JSON API (No Credentials - Recommended for Testing):**

```python
from src.reddit_scraper import RedditJSONScraper, CSVExporter

# Initialize JSON scraper - NO credentials needed!
scraper = RedditJSONScraper()

# Fetch hot posts
posts = scraper.fetch_hot_posts(subreddit="AI_Agent", limit=100)

# Export to CSV
exporter = CSVExporter(output_dir="output")
exporter.export_posts_to_csv(posts)
```

**B) Official API (Requires Credentials - Higher Rate Limits):**

```python
from src.reddit_scraper import RedditScraper, CSVExporter

# Initialize scraper (requires credentials in .env)
scraper = RedditScraper()

# Fetch hot posts
posts = scraper.fetch_hot_posts(subreddit="AI_Agent", limit=100)

# Export to CSV
exporter = CSVExporter(output_dir="output")
exporter.export_posts_to_csv(posts)
```

Run the example:
```bash
python examples/example_usage.py
```

### Option 3: Authenticated Mode (Higher Rate Limits)

For larger data fetches with better reliability:

#### Step 1: Get Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Fill in the form:
   - **Name**: Choose any name (e.g., "AI Agent Scraper")
   - **App type**: Select "script"
   - **Description**: Optional
   - **About URL**: Leave blank
   - **Redirect URI**: Use `http://localhost:8080`
4. Click "Create app"
5. Note your credentials:
   - **Client ID**: The string under "personal use script"
   - **Client Secret**: The string labeled "secret"

#### Step 2: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# .env file
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=AIAgentScraper/1.0 by YourRedditUsername
```

Replace:
- `your_client_id_here` with your actual client ID
- `your_client_secret_here` with your actual client secret
- `YourRedditUsername` with your Reddit username

#### Step 3: Use Authenticated Mode

```python
from reddit_scraper import RedditScraper

# Initialize with authentication (auto-detects credentials)
scraper = RedditScraper()  # or RedditScraper(use_auth=True)

# Now you can fetch more data with higher rate limits
posts = scraper.fetch_hot_posts(subreddit="AI_Agent", limit=100)
```

## Usage Examples

### 1. Fetch Hot Posts

```python
from reddit_scraper import RedditScraper

scraper = RedditScraper()
hot_posts = scraper.fetch_hot_posts(
    subreddit="AI_Agent",
    limit=25,
    fetch_comments=True,
    comment_limit=10
)

print(f"Fetched {hot_posts.total_posts} posts")
```

### 2. Fetch New Posts

```python
new_posts = scraper.fetch_new_posts(
    subreddit="AI_Agent",
    limit=50
)
```

### 3. Fetch Top Posts

```python
# Top posts from this week
top_posts = scraper.fetch_top_posts(
    subreddit="AI_Agent",
    time_filter="week",  # Options: hour, day, week, month, year, all
    limit=25
)
```

### 4. Search for Specific Keywords

```python
# Search for posts about problems
problem_posts = scraper.search_posts(
    query="problem",
    subreddit="AI_Agent",
    limit=30,
    sort="relevance"  # Options: relevance, hot, top, new, comments
)
```

### 5. Comprehensive Fetch (All Types)

```python
# Fetch hot, new, top posts and search results
all_data = scraper.fetch_all_ideas(
    subreddit="AI_Agent",
    post_limit_per_type=25,
    fetch_comments=True
)

# all_data contains:
# - all_data['hot']
# - all_data['new']
# - all_data['top_week']
# - all_data['search_results']
```

### 6. Export to CSV

```python
from csv_exporter import CSVExporter

exporter = CSVExporter(output_dir="output")

# Export single collection
posts_csv, comments_csv = exporter.export_posts_to_csv(hot_posts)

# Export multiple collections
results = exporter.export_multiple_collections(all_data)

# Create summary report
summary = exporter.create_summary_report(all_data)

# Export to Excel
excel_file = exporter.export_all_to_excel(all_data)
```

## Understanding Authentication Modes

### Read-Only Mode (Simple)

**Pros:**
- No setup required
- Works immediately
- Good for testing and learning

**Cons:**
- Lower rate limits (~60 requests/minute)
- May encounter rate limiting with large fetches
- Less reliable for production use

**When to use:** Quick testing, small data fetches, learning the API

### Authenticated Mode

**Pros:**
- Higher rate limits (~600 requests/minute)
- More reliable and stable
- Better for production use
- Required for some advanced features

**Cons:**
- Requires Reddit account
- Need to register an app
- Setup takes 5 minutes

**When to use:** Large data fetches, production applications, reliability is important

## Configuration

Customize settings in `reddit_config.py`:

```python
class RedditConfig:
    DEFAULT_SUBREDDIT = "AI_Agent"
    DEFAULT_POST_LIMIT = 100
    DEFAULT_COMMENT_LIMIT = 50
    DEFAULT_TIME_FILTER = "week"

    # Search keywords for AI agent ideas
    DEFAULT_SEARCH_KEYWORDS = [
        "problem",
        "solution",
        "idea",
        "startup",
        "use case",
        # ... add more
    ]
```

## Data Models

### RedditPost

- `post_id`: Unique post identifier
- `title`: Post title
- `author`: Post author
- `score`: Upvotes/score
- `upvote_ratio`: Ratio of upvotes
- `url`: Linked URL
- `selftext`: Post content
- `created_utc`: Creation timestamp
- `num_comments`: Comment count
- `subreddit`: Subreddit name
- `permalink`: Reddit permalink
- `link_flair_text`: Post flair
- `comments`: List of RedditComment objects

### RedditComment

- `comment_id`: Unique comment ID
- `author`: Comment author
- `body`: Comment text
- `score`: Comment score
- `created_utc`: Creation timestamp
- `is_submitter`: Whether commenter is OP
- `permalink`: Comment permalink
- `parent_id`: Parent comment/post ID

## Output Files

CSV files are saved to the `output/` directory with timestamps:

- `reddit_AI_Agent_hot_posts_YYYYMMDD_HHMMSS.csv`
- `reddit_AI_Agent_hot_comments_YYYYMMDD_HHMMSS.csv`
- `reddit_summary_report_YYYYMMDD_HHMMSS.csv`

## Troubleshooting

### "Rate limit exceeded" error

- **Solution 1**: Use authenticated mode for higher limits
- **Solution 2**: Reduce `limit` parameter
- **Solution 3**: Add delays between requests

### "Invalid credentials" error

- Check your `.env` file has correct credentials
- Verify client ID and secret are copied correctly
- Ensure no extra spaces in `.env` file

### "Subreddit not found" error

- Verify subreddit name is correct (case-sensitive)
- Check if subreddit is private or banned

## Advanced Usage

### Custom Subreddit

```python
# Fetch from any subreddit
posts = scraper.fetch_hot_posts(subreddit="MachineLearning", limit=50)
```

### Multiple Keywords Search

```python
keywords = ["agent", "automation", "workflow", "problem"]
results = {}

for keyword in keywords:
    results[keyword] = scraper.search_posts(
        query=keyword,
        limit=20
    )
```

### Filter Posts by Score

```python
posts = scraper.fetch_hot_posts(limit=100)
high_quality = [p for p in posts.posts if p.score > 50]
```

## Rate Limits

- **Read-only**: ~60 requests/minute
- **Authenticated**: ~600 requests/minute

Reddit may impose additional limits based on:
- Time of day
- API usage patterns
- Account status

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review example_usage.py for working code
3. Open an issue on GitHub

## Credits

Built with:
- [PRAW](https://praw.readthedocs.io/) - Python Reddit API Wrapper
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Pydantic](https://docs.pydantic.dev/) - Data validation