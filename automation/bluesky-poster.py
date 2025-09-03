#!/usr/bin/env python3
"""
Simple Bluesky poster for The Serpent's Sentence content
Handles authentication and posting with minimal fuss
"""

import os
import json
from pathlib import Path
from atproto import Client
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv('.env')

class BlueskyPoster:
    def __init__(self):
        self.client = None
        self.username = os.getenv('BLUESKY_USERNAME')
        self.password = os.getenv('BLUESKY_APP_PASSWORD')
        
        if not self.username or not self.password:
            print("❌ Missing Bluesky credentials in .env file")
            print("Please check BLUESKY_USERNAME and BLUESKY_APP_PASSWORD")
            return
            
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Bluesky"""
        try:
            self.client = Client()
            profile = self.client.login(self.username, self.password)
            print(f"✅ Authenticated as @{profile.handle}")
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            self.client = None
    
    def post(self, text: str, dry_run: bool = False):
        """Post to Bluesky"""
        if dry_run:
            print("🔍 DRY RUN - Would post:")
            print(f"'{text}'")
            print(f"Length: {len(text)} characters")
            return True
            
        if not self.client:
            print("❌ Not authenticated")
            return False
            
        try:
            post = self.client.send_post(text=text)
            print(f"✅ Posted successfully: {post.uri}")
            return True
        except Exception as e:
            print(f"❌ Failed to post: {e}")
            return False

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Post to Bluesky')
    parser.add_argument('--content', type=str, help='Content to post')
    parser.add_argument('--dry-run', action='store_true', help='Test without posting')
    
    args = parser.parse_args()
    
    poster = BlueskyPoster()
    
    if args.content:
        poster.post(args.content, dry_run=args.dry_run)
    else:
        # Default philosophical insight
        content = "The voice in your head isn't you—it's the internal narrator that language created. Before words, there was awareness without commentary."
        poster.post(content, dry_run=args.dry_run)