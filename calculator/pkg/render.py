import json
import csv
from io import StringIO


def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    return json.dumps(output_data, indent=indent)


def format_text_output(expression: str, result: float) -> str:
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    else:
        result_str = str(result)
    return f"{expression} = {result_str}"


def format_csv_output(expression: str, result: float) -> str:
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    else:
        result_str = str(result)

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["expression", "result"])
    writer.writerow([expression, result_str])
    return output.getvalue().strip()