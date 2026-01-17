src/utils/config.py"""
Configuration Management Module
Handles loading and managing application configuration
"""

import os
import json
from pathlib import Path
from typing import Dict, Any


DEFAULT_CONFIG = {
    "general": {
        "project_name": "AI Movie Generator",
        "output_dir": "output",
        "temp_dir": "temp",
        "log_level": "INFO"
    },
    "llm": {
        "provider": "ollama",  # ollama, openai, anthropic
        "model": "llama2",
        "ollama_url": "http://localhost:11434",
        "api_key": "",
        "temperature": 0.7,
        "max_tokens": 2000
    },
    "image_generation": {
        "provider": "stable_diffusion",  # stable_diffusion, dalle, midjourney
        "stable_diffusion_url": "http://localhost:7860",
        "api_key": "",
        "width": 1024,
        "height": 576,
        "steps": 30,
        "cfg_scale": 7.0
    },
    "video": {
        "fps": 24,
        "codec": "libx264",
        "quality": "high",
        "audio_codec": "aac"
    },
    "script_generation": {
        "scene_count": 10,
        "min_scene_duration": 5,
        "max_scene_duration": 30,
        "genre": "sci-fi"
    }
}


def load_config(config_path: str = ".env.json") -> Dict[str, Any]:
    """
    Load configuration from file or return defaults
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    config = DEFAULT_CONFIG.copy()
    
    config_file = Path(config_path)
    if config_file.exists():
        try:
            with open(config_file, 'r') as f:
                user_config = json.load(f)
                # Merge user config with defaults
                for key, value in user_config.items():
                    if key in config and isinstance(config[key], dict):
                        config[key].update(value)
                    else:
                        config[key] = value
        except Exception as e:
            print(f"Warning: Could not load config file: {e}")
    
    # Create output directories if they don't exist
    _create_directories(config)
    
    return config


def save_config(config: Dict[str, Any], config_path: str = ".env.json") -> None:
    """
    Save configuration to file
    
    Args:
        config: Configuration dictionary
        config_path: Path to save configuration
    """
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        print(f"Error saving config: {e}")


def _create_directories(config: Dict[str, Any]) -> None:
    """
    Create necessary directories from config
    
    Args:
        config: Configuration dictionary
    """
    dirs_to_create = [
        config['general']['output_dir'],
        config['general']['temp_dir']
    ]
    
    for dir_path in dirs_to_create:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
