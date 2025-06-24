import sys
import re
import json
import os
try:
    import tkinter as tk
    from tkinter import messagebox, filedialog
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False
    print("⚠️  GUI not available. Running in CLI mode only.")

# English-to-Yoruba word mappings
DEFAULT_DICTIONARY = {
    "the": "nàà",
    "a": "kan",
    "an": "kan",
    "my": "mi",
    "your": "rẹ",
    "his": "rẹ̀",
    "her": "rẹ̀",
    "boy": "ọmọkùnrin",
    "girl": "ọmọbìnrin",
    "man": "ọkùnrin",
    "woman": "obìnrin",
    "apple": "àpù",
    "dog": "ajá",
    "cat": "ológbò",
    "ade": "adé",
    "carried": "gbé",
    "carry": "gbé",
    "chair": "àga",
    "table": "tábìlì",
    "teacher": "olùkọ́",
    "student": "akẹ́kọ̀ọ́",
    "reads": "ka",
    "read": "ka",
    "book": "ìwé",
    "books": "àwọn ìwé",
    "friend": "ọ̀rẹ́",
    "plays": "ṣeré",
    "play": "ṣeré",
    "football": "bọ́ọ̀lù-ẹlẹ́sẹ̀",
    "sees": "rí",
    "see": "rí",
    "ate": "jẹ",
    "eat": "jẹ",
    "love": "fẹ́ràn",
    "loves": "fẹ́ràn",
    "house": "ilé",
    "water": "omi",
    "food": "oúnjẹ",
    "good": "dára",
    "bad": "burú",
    "big": "ńlá",
    "small": "kékeré",
    "go": "lọ",
    "goes": "lọ",
    "come": "wá",
    "comes": "wá",
    "hello": "pẹ̀lẹ́",
    "goodbye": "ó dàbọ̀",
    "yes": "bẹ́ẹ̀ni",
    "no": "bẹ́ẹ̀kọ́",
    "is": "jẹ́",
    "am": "jẹ́",
    "are": "jẹ́",
    "was": "jẹ́",
    "were": "jẹ́"
}

# DEFAULT_DICTIONARY = {
#     "the": "nàà",
#     "a": "kan",
#     "my": "mi",
#     "your": "rẹ",
#     "boy": "ọmọ",
#     "girl": "ọmọbìnrin",
#     "apple": "àpù",
#     "dog": "ajá",
#     "cat": "ologbo",
#     "ade": "adé",
#     "carried": "gbé",
#     "chair": "àga",
#     "teacher": "olùkọ́",
#     "reads": "ka",
#     "books": "àwọn ìwé",
#     "friend": "ọ̀rẹ́",
#     "plays": "ṣeré",
#     "football": "bọ́ọ̀lù",
#     "sees": "rí",
#     "ate": "jẹ"
# }

class EnglishYorubaTranslator:
    def __init__(self, dictionary_file=None):
        self.dictionary = DEFAULT_DICTIONARY.copy()
        if dictionary_file and os.path.exists(dictionary_file):
            self.load_dictionary(dictionary_file)
    
    def load_dictionary(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                custom_dict = json.load(f)
                self.dictionary.update(custom_dict)
                print(f"✅ Loaded {len(custom_dict)} additional translations from {file_path}")
        except Exception as e:
            print(f"⚠️  Warning: Could not load dictionary file {file_path}: {e}")
    
    def save_dictionary(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.dictionary, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"❌ Error saving dictionary: {e}")
            return False
    
    def add_translation(self, english, yoruba):
        if not english or not yoruba:
            return False
        self.dictionary[english.lower().strip()] = yoruba.strip()
        return True
    
    def clean_input(self, text):
        if not text or not isinstance(text, str):
            return ""
        text = text.strip()
        if len(text) > 1000:
            text = text[:1000]
        text = re.sub(r'[^\w\s.,!?;:-]', '', text)
        return text
    
    def translate_word(self, word):
        word_clean = re.sub(r'[^\w]', '', word.lower())
        return self.dictionary.get(word_clean, word)
    
    def translate_to_yoruba(self, sentence):
        sentence = self.clean_input(sentence)
        if not sentence:
            return ""
        
        words = sentence.lower().split()
        if len(words) > 100:
            return "❌ Sentence too long (max 100 words)"
        
        translated = []
        for word in words:
            translated.append(self.translate_word(word))
        
        result = self.apply_word_order_rules(translated)
        return " ".join(result)
    
    def apply_word_order_rules(self, translated_words):
        result = []
        skip = False
        determiners = ["kan", "nàà", "mi", "rẹ", "rẹ̀"]
        
        for i in range(len(translated_words)):
            if skip:
                skip = False
                continue
            
            if (i < len(translated_words) - 1 and 
                translated_words[i] in determiners and 
                translated_words[i + 1] not in determiners):
                result.append(translated_words[i + 1])
                result.append(translated_words[i])
                skip = True
            else:
                result.append(translated_words[i])
        
        return result

def run_cli_mode(translator):
    print("🌍 English to Yoruba Translator (CLI Mode)")
    print("💡 Commands: 'help', 'add <english> = <yoruba>', 'save <file>', 'load <file>', 'q' to quit")
    
    while True:
        try:
            text = input("\n➤ Enter English text: ").strip()
            
            if not text:
                continue
            
            if text.lower() in ['q', 'quit', 'exit']:
                print("👋 Goodbye!")
                break
            
            if text.lower() == 'help':
                print("\n📖 Available commands:")
                print("  help                    - Show this help")
                print("  add <english> = <yoruba> - Add new translation")
                print("  save <filename>         - Save dictionary to file")
                print("  load <filename>         - Load dictionary from file")
                print("  q, quit, exit          - Exit program")
                continue
            
            if text.startswith('add '):
                parts = text[4:].split(' = ')
                if len(parts) == 2:
                    if translator.add_translation(parts[0], parts[1]):
                        print(f"✅ Added: {parts[0]} → {parts[1]}")
                    else:
                        print("❌ Invalid translation format")
                else:
                    print("❌ Format: add <english> = <yoruba>")
                continue
            
            if text.startswith('save '):
                filename = text[5:].strip()
                if translator.save_dictionary(filename):
                    print(f"✅ Dictionary saved to {filename}")
                continue
            
            if text.startswith('load '):
                filename = text[5:].strip()
                translator.load_dictionary(filename)
                continue
            
            yoruba = translator.translate_to_yoruba(text)
            print(f"🌍 Yoruba: {yoruba}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def run_gui_mode(translator):
    if not GUI_AVAILABLE:
        print("❌ GUI mode not available. Install tkinter.")
        return
    
    root = tk.Tk()
    root.title("English to Yoruba Translator")
    root.geometry("700x500")
    root.configure(bg='white')
    
    # Main frame
    main_frame = tk.Frame(root, bg='white', padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Title
    title_label = tk.Label(main_frame, text="🌍 English to Yoruba Translator", 
                          font=("Arial", 16, "bold"), bg='white', fg='black')
    title_label.pack(pady=(0, 20))
    
    # Input section
    tk.Label(main_frame, text="Enter English text:", font=("Arial", 12), bg='white', fg='black').pack(anchor='w')
    
    input_frame = tk.Frame(main_frame, bg='white')
    input_frame.pack(fill=tk.X, pady=5)
    
    entry = tk.Text(input_frame, height=3, width=70, wrap=tk.WORD, bg='white', fg='black', 
                   insertbackground='black', relief='solid', bd=1)
    entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    input_scroll = tk.Scrollbar(input_frame, orient=tk.VERTICAL, command=entry.yview)
    input_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    entry.config(yscrollcommand=input_scroll.set)
    
    # Output section
    tk.Label(main_frame, text="Yoruba translation:", font=("Arial", 12), bg='white', fg='black').pack(anchor='w', pady=(20, 5))
    
    output_frame = tk.Frame(main_frame, bg='white')
    output_frame.pack(fill=tk.BOTH, expand=True, pady=5)
    
    translation_output = tk.Text(output_frame, height=3, width=70, wrap=tk.WORD, 
                                fg="black", bg='white', font=("Arial", 11), state=tk.DISABLED,
                                relief='solid', bd=1)
    translation_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    output_scroll = tk.Scrollbar(output_frame, orient=tk.VERTICAL, command=translation_output.yview)
    output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    translation_output.config(yscrollcommand=output_scroll.set)
    
    def on_translate():
        try:
            text = entry.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Warning", "Please enter some text to translate.")
                return
            
            yoruba = translator.translate_to_yoruba(text)
            
            translation_output.config(state=tk.NORMAL)
            translation_output.delete("1.0", tk.END)
            translation_output.insert("1.0", yoruba)
            translation_output.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")
    
    def clear_all():
        entry.delete("1.0", tk.END)
        translation_output.config(state=tk.NORMAL)
        translation_output.delete("1.0", tk.END)
        translation_output.config(state=tk.DISABLED)
    
    def load_dict():
        filename = filedialog.askopenfilename(
            title="Load Dictionary",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            translator.load_dictionary(filename)
            messagebox.showinfo("Success", f"Dictionary loaded from {filename}")
    
    def save_dict():
        filename = filedialog.asksaveasfilename(
            title="Save Dictionary",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            if translator.save_dictionary(filename):
                messagebox.showinfo("Success", f"Dictionary saved to {filename}")
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg='white')
    button_frame.pack(pady=20)
    
    tk.Button(button_frame, text="🔄 Translate", command=on_translate, 
             font=("Arial", 11), bg='#2E7D32', fg='black', padx=20, 
             relief='raised', bd=2).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="🗑️ Clear", command=clear_all, 
             font=("Arial", 11), bg='#C62828', fg='black', padx=20,
             relief='raised', bd=2).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="📁 Load Dict", command=load_dict, 
             font=("Arial", 11), bg='#1565C0', fg='black', padx=15,
             relief='raised', bd=2).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="💾 Save Dict", command=save_dict, 
             font=("Arial", 11), bg='#E65100', fg='black', padx=15,
             relief='raised', bd=2).pack(side=tk.LEFT, padx=5)
    
    # Bind Enter key
    root.bind('<Control-Return>', lambda _: on_translate())
    
    # Status bar
    status_frame = tk.Frame(root, bg='#F5F5F5', relief='sunken', bd=1)
    status_frame.pack(fill=tk.X, side=tk.BOTTOM)
    
    status_label = tk.Label(status_frame, text=f"📚 Dictionary contains {len(translator.dictionary)} translations | Press Ctrl+Enter to translate", 
                           bg='#F5F5F5', fg='black', font=("Arial", 9))
    status_label.pack(anchor='w', padx=10, pady=2)
    
    root.mainloop()

def main():
    translator = EnglishYorubaTranslator()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--cli':
            run_cli_mode(translator)
        elif sys.argv[1] == '--gui':
            run_gui_mode(translator)
        elif sys.argv[1] == '--help':
            print("🌍 English to Yoruba Translator")
            print("Usage: python app.py [--cli|--gui|--help] [dictionary_file]")
            print("  --cli    : Run in command line mode")
            print("  --gui    : Run in GUI mode (default if available)")
            print("  --help   : Show this help message")
        elif os.path.exists(sys.argv[1]):
            translator.load_dictionary(sys.argv[1])
            if GUI_AVAILABLE:
                run_gui_mode(translator)
            else:
                run_cli_mode(translator)
        else:
            print(f"❌ File not found: {sys.argv[1]}")
    else:
        if GUI_AVAILABLE:
            run_gui_mode(translator)
        else:
            run_cli_mode(translator)

if __name__ == '__main__':
    main()