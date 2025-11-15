from io_utils import load_logs, save_output
from log_analysis import analyze_logs
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description="Analisi log anonimizzati")
    parser.add_argument("-i", "--input", default="test_data/test_large.json")
    parser.add_argument("-o", "--output", default="result.json")
    return parser.parse_args()

def main():
    args = parse_args()
    logs = load_logs(args.input)
    result = analyze_logs(logs)
    save_output(result, args.output)
    print(f"Analisi completata. Risultati salvati in {args.output}")

if __name__ == "__main__":
    main()