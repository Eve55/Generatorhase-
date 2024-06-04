def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    top_line = ""
    bottom_line = ""
    separator_line = ""
    result_line = ""

    for problem in problems:
        elements = problem.split()
        if len(elements) != 3:
            return "Error: Each problem should have two operands and one operator separated by spaces."
        operand1, operator, operand2 = elements

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Operands must be numeric."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Wykonanie odpowiedniej operacji w zależności od operatora
        if operator == '+':
            result = int(operand1) + int(operand2)
        elif operator == '-':
            result = int(operand1) - int(operand2)

        width = max(len(operand1), len(operand2)) + 2
        top_line += operand1.rjust(width) + "    "
        bottom_line += operator + operand2.rjust(width - 1) + "    "
        separator_line += "-" * width + "    "

        if show_answers:
            result_line += str(result).rjust(width) + "    "

    arranged_problems.extend([top_line.rstrip(),
                              bottom_line.rstrip(),
                              separator_line.rstrip()])

    if show_answers:
        arranged_problems.append(result_line.rstrip())

    return "\n".join(arranged_problems)


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
