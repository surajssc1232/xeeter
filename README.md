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

## ��️ Installation

### Method 1: Using pipx (Recommended)

#### For Arch Linux:
```bash
sudo pacman -S python-pipx
```

#### For Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

#### For Fedora:
```bash
sudo dnf install pipx
```

After installing pipx:
1. Clone the repository:
   ```bash
   git clone https://github.com/surajssc1232/xeeter.git
   cd xeeter
   ```

2. Install using pipx:
   ```bash
   pipx install .
   ```

### Method 2: Using Virtual Environment

1. Install Python and pip (if not already installed)

   #### Arch Linux:
   ```bash
   sudo pacman -S python python-pip
   ```

   #### Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

   #### Fedora:
   ```bash
   sudo dnf install python3 python3-pip
   ```

2. Clone and setup:
   ```bash
   git clone https://github.com/surajssc1232/xeeter.git
   cd xeeter
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   ```

## 🔑 Configuration

1. Create a Twitter Developer Account at [developer.twitter.com](https://developer.twitter.com)
2. Create a new project and app (select "Native App")
3. Enable "Read and Write" permissions for your app
4. Generate API Keys and Access Tokens
5. Set up your environment variables by adding these to your shell config file:
   - For bash: `~/.bashrc`
   - For zsh: `~/.zshrc`
   - For fish: `~/.config/fish/config.fish`

   ```bash
   export TWITTER_API_KEY="your_api_key"
   export TWITTER_API_SECRET_KEY="your_api_secret_key"
   export TWITTER_ACCESS_TOKEN="your_access_token"
   export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
   ```

6. Apply the changes:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc
   ```

## 🚀 Usage

Post a tweet:
```bash
tweet "Hello, Twitter! 🚀"
```

Note: Twitter doesn't allow posting identical tweets. Add small variations to post similar content:
```bash
tweet "Hello World!"
tweet "Hello World!!"  # Different punctuation
tweet "Hello World $(date)"  # With timestamp
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

1. **Command Not Found**
   ```bash
   # For pipx installations, ensure pipx is in your PATH
   pipx ensurepath
   
   # For venv installations, make sure you're in the virtual environment
   source venv/bin/activate
   
   # Restart your terminal or source your shell config
   source ~/.bashrc  # or ~/.zshrc
   ```

2. **Permission Issues**
   ```bash
   # If pip install fails with permission error
   pip install --user -e .
   
   # If pipx command not found after installation
   export PATH="$HOME/.local/bin:$PATH"
   ```

3. **"Unauthorized" Error**
   - Verify your API keys and tokens are correct
   - Check if environment variables are set:
     ```bash
     echo $TWITTER_API_KEY  # Should show your key
     ```
   - Ensure your app has "Read and Write" permissions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tweepy](https://www.tweepy.org/) - The awesome Python library for accessing the Twitter API
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api) - For providing the API

## 📧 Contact

For any questions or feedback, feel free to reach out:
- Create an issue in this repository
- Follow me on Twitter: [@yourusername](https://twitter.com/surajkhahai)

---
Made with ❤️ by suraj <3.