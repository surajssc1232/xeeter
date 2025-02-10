# 🐦 Tweet CLI Tool

[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Twitter API](https://img.shields.io/badge/Twitter%20API-v2-blue.svg)](https://developer.twitter.com/en/docs/twitter-api)

A sleek command-line tool that lets you post tweets directly from your terminal. Simple, fast, and developer-friendly!

## ✨ Features

- 🚀 Post tweets directly from your terminal
- 🔐 Secure authentication using Twitter API v2
- 💻 Simple and intuitive command-line interface
- ⚡ Fast and lightweight

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/surajssc1232/xeeter.git
   cd tweet-cli-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package:
   ```bash
   pip install -e .
   ```

## 🔑 Configuration

1. Create a Twitter Developer Account at [developer.twitter.com](https://developer.twitter.com)
2. Create a new project and app (select "Native App")
3. Enable "Read and Write" permissions for your app
4. Generate API Keys and Access Tokens
5. Set up your environment variables:

   ```bash
   export TWITTER_API_KEY="your_api_key"
   export TWITTER_API_SECRET_KEY="your_api_secret_key"
   export TWITTER_ACCESS_TOKEN="your_access_token"
   export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
   ```

   Pro tip: Add these to your `~/.bashrc` or `~/.zshrc` for persistence!

## 🚀 Usage

Post a tweet:
```bash
tweet "Hello, Twitter! Tweeting from my custom CLI tool 🚀"
```

## 📁 Project Structure

```
tweet_cli_tool/
├── README.md
├── requirements.txt
├── setup.py
└── tweet_cli_tool/
    ├── __init__.py
    ├── cli.py           # Command-line interface
    └── twitter/
        ├── __init__.py
        └── client.py    # Twitter API client
```

## 🔧 Development

Want to contribute? Great! Here's how to set up the development environment:

1. Fork the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
4. Make your changes
5. Submit a pull request

## 🐛 Troubleshooting

### Common Issues

1. **"Unauthorized" Error**
   - Verify your API keys and tokens are correct
   - Ensure you've set the correct environment variables
   - Check if your app has "Read and Write" permissions

2. **Command Not Found**
   - Make sure you've installed the package (`pip install -e .`)
   - Verify your Python scripts directory is in your PATH

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tweepy](https://www.tweepy.org/) - The awesome Python library for accessing the Twitter API
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api) - For providing the API

## 📧 Contact

For any questions or feedback, feel free to reach out:
- Create an issue in this repository
- Follow me on Twitter: [@yourusername](https://twitter.com/yourusername)

---
Made with ❤️ by suraj <3.