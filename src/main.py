#!/usr/bin/env python3
"""
AI Movie Generator - Main Entry Point
Generates movies and series automatically using AI
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from utils.config import load_config
from utils.logger import setup_logger


def main():
    """Main application entry point"""
    # Setup logging
    logger = setup_logger()
    logger.info("Starting AI Movie Generator...")
    
    # Load configuration
    config = load_config()
    logger.info(f"Configuration loaded: {config['general']['project_name']}")
    
    # Create Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("AI Movie Generator")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = MainWindow(config)
    window.show()
    
    logger.info("Application started successfully")
    
    # Start event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
