"""
Dashboard Launcher for The Serpent's Sentence
Starts the Flask server and opens the dashboard in your browser
"""

import subprocess
import webbrowser
import time
import sys
import os
from pathlib import Path

def main():
    print("The Serpent's Sentence - Dashboard Launcher")
    print("=" * 50)
    
    # Check if Flask is installed
    try:
        import flask
        import flask_cors
        print("✓ Flask dependencies found")
    except ImportError:
        print("Installing Flask and Flask-CORS...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'flask', 'flask-cors'])
        print("✓ Dependencies installed")
    
    # Path to the dashboard server
    server_path = Path(__file__).parent / 'server.py'
    
    if not server_path.exists():
        print(f"Server script not found: {server_path}")
        return
    
    print("Starting dashboard server...")
    
    try:
        # Start the Flask server
        server_process = subprocess.Popen([
            sys.executable, str(server_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Check if server is running
        if server_process.poll() is None:
            print("✓ Server started successfully")
            print("Opening dashboard in browser...")
            
            # Open browser
            webbrowser.open('http://localhost:5000')
            
            print("\n" + "=" * 50)
            print("Dashboard Controls:")
            print("   • Extract Content: Generate insights from manuscript")
            print("   • Post to Bluesky: Share philosophical insights")
            print("   • Generate Articles: Create Substack content")
            print("   • Run Pipeline: Full automation workflow")
            print("\nThemes Available:")
            print("   • Fall from Eden: Pre-linguistic consciousness")
            print("   • Born in Exile: The prison of pronouns")
            print("   • Symbiotic Future: Human-AI collaboration")
            print("   • Cambrian Explosion: Digital consciousness evolution")
            print("\nPress Ctrl+C to stop the server")
            print("=" * 50)
            
            # Keep the script running until user stops it
            try:
                server_process.wait()
            except KeyboardInterrupt:
                print("\nStopping dashboard server...")
                server_process.terminate()
                print("✓ Server stopped")
        else:
            # Server failed to start
            stdout, stderr = server_process.communicate()
            print("Server failed to start")
            if stderr:
                print("Error:", stderr)
            if stdout:
                print("Output:", stdout)
    
    except Exception as e:
        print(f"Error starting dashboard: {e}")

if __name__ == '__main__':
    main()