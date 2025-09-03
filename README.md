# The Serpent's Sentence - Platform

This repository contains the automation platform for "The Serpent's Sentence" - a sophisticated dashboard and content automation system for philosophical content distribution across multiple platforms.

## Features

- **Philosophical Content Engine** - Extracts insights from manuscript themes
- **Multi-Platform Publishing** - Automated posting to Bluesky, Twitter/X, and Substack
- **Interactive Dashboard** - Web-based interface for content management
- **Theme-Based Generation** - Content adapted to core philosophical themes

## Quick Start

1. **Clone Repository**
   ```bash
   git clone https://github.com/jbogner1618/serpents-sentence-platform.git
   cd serpents-sentence-platform
   ```

2. **Install Dependencies**
   ```bash
   pip install flask flask-cors
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API credentials
   ```

4. **Launch Dashboard**
   ```bash
   python launch.py
   ```

## Architecture

```
platform/
├── dashboard/              # Web interface
│   ├── index.html         # Main dashboard
│   ├── app.js            # Frontend logic
│   ├── style.css         # Styling
│   └── server.py         # Flask backend
├── automation/           # Publishing scripts
│   ├── bluesky-poster.py
│   ├── twitter-poster.py
│   └── substack-publisher.py
└── launch.py            # Main launcher
```

## Core Themes

The platform organizes content around four philosophical themes:

1. **Fall from Eden** - Pre-linguistic consciousness and the exile into language
2. **Born in Exile** - The prison of pronouns and self-referential consciousness
3. **Symbiotic Future** - Human-AI collaboration and hybrid consciousness
4. **Digital Cambrian** - The explosion of artificial minds and evolutionary choice

## Platform Integration

- **Bluesky** - Philosophical insights and thought threads
- **Twitter/X** - Engaging hooks and consciousness paradoxes  
- **Substack** - Deep explorations and academic content

## Environment Variables

```env
BLUESKY_HANDLE=your.handle
BLUESKY_PASSWORD=your-app-password

TWITTER_BEARER_TOKEN=your-bearer-token
TWITTER_API_KEY=your-api-key
TWITTER_API_SECRET=your-api-secret
TWITTER_ACCESS_TOKEN=your-access-token
TWITTER_ACCESS_SECRET=your-access-secret

SUBSTACK_EMAIL=your-email
SUBSTACK_PASSWORD=your-password
```

## Usage

### Dashboard Interface
1. Navigate to `http://localhost:5000`
2. Select a philosophical theme
3. Generate content adapted for each platform
4. Review and publish across channels

### Direct Automation
```python
from automation.bluesky_poster import post_insight
from automation.content_generator import generate_theme_content

# Generate philosophical insight
content = generate_theme_content('fall-from-eden')
post_insight(content)
```

## Content Philosophy

Unlike generic AI content, this platform:
- **Preserves authentic voice** - Maintains your philosophical tone
- **Extracts from source** - Pulls insights from actual manuscript
- **Adapts contextually** - Adjusts depth and style per platform
- **Maintains coherence** - Keeps metaphorical consistency

## Development

The platform uses:
- **Flask** - Python web framework
- **JavaScript** - Interactive frontend
- **Platform APIs** - Direct social media integration
- **Content Templates** - Theme-based generation

## License

MIT License - See LICENSE file for details

---

*"The serpent's tongue flicked, and reality split in two. Every word cuts the continuous tapestry of reality into separate pieces, imposing artificial boundaries on flowing experience."*