import sys
import os
from core.validator import SentenceValidator

def main():
    grammar_file = './grammar/english_grammar.cfg'
    
    if len(sys.argv) > 1:
        grammar_file = sys.argv[1]
    
    if not os.path.exists(grammar_file):
        print(f"❌ Error: Grammar file '{grammar_file}' not found.")
        print("Usage: python app.py [grammar_file]")
        sys.exit(1)
    
    try:
        validator = SentenceValidator(grammar_file)
    except Exception as e:
        print(f"❌ Error initializing validator: {e}")
        sys.exit(1)
    
    print("🔍 English Grammar Checker")
    print(f"📝 Using grammar file: {grammar_file}")
    print("💡 Enter sentences to check grammar (type 'help' for commands, 'q' to quit)")
    
    while True:
        try:
            sentence = input("\n➤ Enter sentence: ").strip()
            
            if not sentence:
                continue
            
            if sentence.lower() == 'q' or sentence.lower() == 'quit':
                print("👋 Goodbye!")
                break
            
            if sentence.lower() == 'help':
                print("\n📖 Available commands:")
                print("  help  - Show this help message")
                print("  q     - Quit the program")
                print("  quit  - Quit the program")
                continue
            
            if len(sentence) > 1000:
                print("❌ Error: Sentence too long (max 1000 characters)")
                continue
            
            valid, message = validator.validate(sentence)
            status = "✅ Valid" if valid else "❌ Invalid"
            print(f"{status}: {message}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == '__main__':
    main()
