import sys
import json
from pkg.calculator import Calculator
from pkg.render import format_json_output, format_text_output, format_csv_output


def parse_args(args):
    """Parse command line arguments and return (format, expression parts)."""
    format = "json"
    expression_parts = []
    i = 1  # Skip script name
    while i < len(args):
        arg = args[i]
        if arg == "--help" or arg == "-h":
            print("Calculator App")
            print('Usage: python main.py "<expression>" [OPTIONS]')
            print('Options:')
            print('  --help, -h              Show this help message')
            print('  --format FORMAT         Output format: json, text, or csv')
            print('Example: python main.py "3 + 5" --format text')
            sys.exit(0)
        elif arg == "--format":
            if i + 1 < len(args):
                format = args[i + 1]
                i += 1
            else:
                print("Error: --format requires an argument")
                sys.exit(1)
        else:
            expression_parts.append(arg)
        i += 1
    return format, expression_parts


def main() -> None:
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>" [OPTIONS]')
        print('Options:')
        print('  --help, -h              Show this help message')
        print('  --format FORMAT         Output format: json, text, or csv')
        print('Example: python main.py "3 + 5" --format text')
        return

    format, expression_parts = parse_args(sys.argv)
    expression = " ".join(expression_parts)

    try:
        result = calculator.evaluate(expression)
        if result is not None:
            # Choose formatter
            if format == "json":
                to_print = format_json_output(expression, result)
            elif format == "text":
                to_print = format_text_output(expression, result)
            elif format == "csv":
                to_print = format_csv_output(expression, result)
            else:
                to_print = format_json_output(expression, result)
            print(to_print)
        else:
            error_data = {"error": "Expression is empty or contains only whitespace.", "expression": expression}
            print(json.dumps(error_data, indent=2))
    except Exception as e:
        error_data = {"error": str(e), "expression": expression}
        print(json.dumps(error_data, indent=2))


if __name__ == "__main__":
    main()