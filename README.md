# Language Processing Toolkit

A comprehensive suite of natural language processing tools for English and Yoruba languages, featuring grammar checking, translation, and validation capabilities.

## 📋 Overview

This toolkit provides three specialized applications for language processing:

1. **English Grammar Checker** - Validates English sentence grammar using CFG rules
2. **Yoruba Grammar Checker** - Bilingual tool for Yoruba sentence validation  
3. **English-Yoruba Translator** - Machine translation with GUI and CLI interfaces

## 🛠️ Applications

### 🔍 English Grammar Checker

Located in `/english_checker/`

A command-line tool that validates English sentences against context-free grammar rules with robust error handling and interactive features.

**Key Features:**
- Grammar validation using CFG rules
- Interactive command interface
- Custom grammar file support
- Input sanitization and validation

📖 **[View Complete Documentation](english_checker/README.md)**

### 🇳🇬 Yoruba Grammar Checker

Located in `/yoruba_checker/`

A bilingual (English/Yoruba) grammar validation tool with full Unicode support for Yoruba diacritics and cultural sensitivity.

**Key Features:**
- Bilingual interface (Yoruba + English)
- Yoruba character and diacritic support
- Cultural context awareness
- Pattern-based text validation

📖 **[View Complete Documentation](yoruba_checker/README.md)**

### 🌍 English-Yoruba Translator

Located in `/translator/`

A comprehensive machine translation tool offering both graphical and command-line interfaces for English to Yoruba translation.

**Key Features:**
- Dual interface (GUI + CLI)
- Dictionary management (load/save)
- Real-time translation
- Word reordering for Yoruba grammar
- 50+ built-in vocabulary

📖 **[View Complete Documentation](translator/README.md)**

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- tkinter (for translator GUI - usually included)
- Unicode-capable terminal/font for Yoruba text

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd CPE510-project
   ```

2. Navigate to any application directory:
   ```bash
   # English Grammar Checker
   cd english_checker
   python app.py
   
   # Yoruba Grammar Checker  
   cd yoruba_checker
   python app.py
   
   # English-Yoruba Translator
   cd translator
   python app.py
   ```

## 📁 Project Structure

```
CPE510-project/
├── README.md                    # This file
├── english_checker/
│   ├── app.py                  # Main application
│   ├── README.md               # English checker documentation
│   ├── core/
│   │   └── validator.py        # Grammar validation logic
│   └── grammar/
│       └── english_grammar.cfg # CFG rules for English
├── yoruba_checker/
│   ├── app.py                  # Main application
│   ├── README.md               # Yoruba checker documentation
│   ├── core/
│   │   └── validator.py        # Grammar validation logic
│   └── grammar/
│       └── yoruba_grammar.cfg  # CFG rules for Yoruba
└── translator/
    ├── app.py                  # Main application
    ├── README.md               # Translator documentation
    └── [translation logic]     # Built-in dictionary and GUI/CLI
```

## 🌟 Features Across Applications

### Common Features
- ✅ **Error Handling**: Comprehensive error management
- ✅ **Input Validation**: Text sanitization and length limits
- ✅ **Unicode Support**: Full UTF-8 encoding for international characters
- ✅ **Cross-Platform**: Windows, macOS, and Linux compatibility
- ✅ **Interactive UI**: User-friendly command interfaces

### Language-Specific Features
- ✅ **English**: Context-free grammar validation
- ✅ **Yoruba**: Diacritic support, bilingual interface, cultural sensitivity
- ✅ **Translation**: Word reordering, dictionary management, dual interfaces

## 📚 Usage Examples

### English Grammar Checking
```bash
cd english_checker
python app.py

# Example session:
➤ Enter sentence: The cat sits on the mat
✅ Valid: Sentence is grammatically correct
```

### Yoruba Grammar Checking
```bash
cd yoruba_checker  
python app.py

# Example session:
➤ Tẹ gbolohun Yorùbá: Ọmọ náà lọ sí ilé
✅ Ó tọ́ / Valid: Sentence is grammatically correct
```

### English-Yoruba Translation
```bash
cd translator
python app.py

# GUI mode launches automatically
# Or use CLI mode:
python app.py --cli

# Example translation:
➤ Enter English text: The boy reads books
🌍 Yoruba: ọmọkùnrin nàà ka àwọn ìwé
```

## 🔧 Development

### Architecture
Each application follows a modular design:
- **Core Logic**: Grammar validation and translation engines
- **User Interface**: CLI and GUI implementations
- **Configuration**: Grammar files and dictionaries
- **Error Handling**: Comprehensive exception management

### Adding Features
1. **Grammar Rules**: Edit CFG files in `grammar/` directories
2. **Translation Dictionary**: Modify built-in dictionary in translator
3. **UI Enhancements**: Update CLI prompts or GUI layouts
4. **Language Support**: Extend Unicode handling and character sets

## 🐛 Troubleshooting

### Common Issues

1. **Grammar files not found**:
   - Ensure you're in the correct application directory
   - Check file paths and permissions

2. **Yoruba characters not displaying**:
   - Use Unicode-capable terminal
   - Install fonts with Yoruba diacritic support

3. **GUI not launching** (translator):
   - Install tkinter: `sudo apt-get install python3-tk` (Linux)
   - Use CLI mode: `python app.py --cli`

### Getting Help

For application-specific issues, see the detailed documentation:
- [English Checker Troubleshooting](english_checker/README.md#troubleshooting)
- [Yoruba Checker Troubleshooting](yoruba_checker/README.md#troubleshooting)  
- [Translator Troubleshooting](translator/README.md#troubleshooting)

## 🤝 Contributing

We welcome contributions to improve language processing capabilities:

1. **Code Quality**: Follow existing patterns and style
2. **Testing**: Test with diverse language samples
3. **Documentation**: Update READMEs for new features
4. **Localization**: Maintain proper Unicode and cultural sensitivity

### Development Setup
```bash
git clone <repository-url>
cd CPE510-project
# Navigate to specific application for development
cd english_checker  # or yoruba_checker, translator
```

## 📄 License

This project is an educational language processing toolkit. See individual application directories for specific licensing information.

## 🙏 Acknowledgments

- Linguistic experts for grammar rule validation
- Unicode Consortium for character encoding standards
- Python community for natural language processing tools
- Cultural consultants for Yoruba language accuracy