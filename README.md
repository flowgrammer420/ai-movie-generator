# 🎬 AI Movie Generator

> **Automatische Erstellung von Filmen und Serien mit KI-Power**

Eine Windows-Anwendung, die vollautomatisch Drehbücher schreibt, Bilder generiert und Videos zusammenschneidet - alles mithilfe von Large Language Models (LLMs) und KI-Bildgenerierung.

## ✨ Features

- 📝 **Automatische Drehbucherstellung** mit lokalen LLMs (Ollama) oder externen APIs
- 🎨 **KI-Bildgenerierung** via Stable Diffusion (lokal) oder DALL-E/Midjourney APIs
- 🎥 **Video-Assembly** mit FFmpeg - automatisches Zusammenschneiden von Bildern zu Videos
- 🐳 **Docker-basiert** - Einfaches Setup mit lokalen LLMs und Bildgenerierung
- 💻 **Windows GUI** - Benutzerfreundliche PyQt6-Oberfläche
- ⚡ **GPU-Unterstützung** - Optimiert für NVIDIA GPUs

## 🚀 Quick Start

### Voraussetzungen

- **Windows 10/11** (64-bit)
- **Python 3.10+**
- **Docker Desktop** für lokale LLMs
- **NVIDIA GPU** (optional, aber empfohlen)
- **16GB+ RAM**

### Installation

1. **Repository klonen**
```bash
git clone https://github.com/flowgrammer420/ai-movie-generator.git
cd ai-movie-generator
```

2. **Virtuelle Umgebung erstellen**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Dependencies installieren**
```bash
pip install -r requirements.txt
```

4. **Docker Services starten**
```bash
docker-compose up -d
```

5. **Environment Variables konfigurieren**
```bash
cp .env.example .env
# .env anpassen mit deinen API Keys
```

6. **Anwendung starten**
```bash
python src/main.py
```

## 📦 Projektstruktur

```
ai-movie-generator/
├── src/                    # Source Code
│   ├── main.py            # Haupteinstiegspunkt
│   ├── llm/               # LLM Integration
│   │   ├── script_generator.py
│   │   └── ollama_client.py
│   ├── image/             # Bildgenerierung
│   │   └── image_generator.py
│   ├── video/             # Video-Verarbeitung
│   │   └── video_assembler.py
│   └── gui/               # PyQt6 GUI
├── docker/                # Docker Konfigurationen
├── config/                # Konfigurationsdateien
├── output/                # Generierte Videos
├── docker-compose.yml     # Docker Services
└── requirements.txt       # Python Dependencies
```

## 🐳 Docker Services

### Ollama (Local LLM)
- **Port**: 11434
- **Modelle**: llama3, mistral, codellama
- **Usage**: Drehbuch-Generierung

### Stable Diffusion WebUI
- **Port**: 7860
- **Modelle**: SD 1.5, SDXL
- **Usage**: Bild-Generierung für Szenen

## 🎯 Usage

### 1. GUI starten
```bash
python src/main.py
```

### 2. Projekt konfigurieren
- Genre auswählen (Action, Drama, Sci-Fi, etc.)
- Länge festlegen (Kurzfilm, Episode, Film)
- LLM-Modell wählen
- Bildstil definieren

### 3. Generierung starten
- Klick auf "Generate Movie"
- Fortschritt in Echtzeit verfolgen
- Fertiges Video in `output/` finden

## ⚙️ Konfiguration

### LLM Configuration

**Lokal (Ollama)**:
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
```

**Extern (OpenAI)**:
```env
OPENAI_API_KEY=sk-...
```

### Bildgenerierung

**Lokal (Stable Diffusion)**:
```env
SD_API_URL=http://localhost:7860
```

**Extern (DALL-E)**:
```env
DALL_E_API_KEY=sk-...
```

## 🛠 Entwicklung

### Setup Development Environment
```bash
pip install -r requirements.txt
pip install pytest black flake8
```

### Tests ausführen
```bash
pytest tests/
```

### Code formatieren
```bash
black src/
```

## 📋 Roadmap

- [x] Basis-Architektur
- [x] Docker Setup
- [x] LLM Integration
- [ ] Bildgenerierung
- [ ] Video-Assembly
- [ ] GUI Implementation
- [ ] Audio/Musik Integration
- [ ] Voice-Over mit TTS
- [ ] Multi-Sprachen Support

## 🤝 Contributing

Contributions sind willkommen! Bitte:
1. Fork das Projekt
2. Erstelle einen Feature Branch
3. Committe deine Änderungen
4. Push zum Branch
5. Öffne einen Pull Request

## 📄 Lizenz

Apache-2.0 License - siehe [LICENSE](LICENSE) für Details

## 🙏 Credits

- **Ollama** - Lokale LLM Inference
- **Stable Diffusion** - Open-Source Bildgenerierung
- **FFmpeg** - Video-Processing
- **PyQt6** - GUI Framework

## 📞 Support

Bei Fragen oder Problemen:
- 🐛 [Issues](https://github.com/flowgrammer420/ai-movie-generator/issues)
- 💬 [Discussions](https://github.com/flowgrammer420/ai-movie-generator/discussions)

---

**Made with ❤️ and AI**
