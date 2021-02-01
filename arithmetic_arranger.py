
import re

operator_re = "[+-]"
non_digit_re = '[a-zA-Z]+'
operand_re = "[0-9][0-9]?[0-9]?[0-9]?[0-9]?"

def arithmetic_arranger( problems, solutions=False ) :
    arranged_problems_list = []

    if len( problems ) > 5 :
        return 'Error: Too many problems.'                      # too many problem error

    first_operands = []
    second_operands = []
    dashes = []
    results = []
    for problem in problems :
        non_digit_error = re.search( non_digit_re, problem )
        operator = re.search( operator_re, problem )
        operands = re.findall( operand_re, problem )
        if not operator :
            return "Error: Operator must be '+' or '-'."        # incorrect operator error
        if non_digit_error :
            return "Error: Numbers must only contain digits."    # non-digit operand error
        else :
            first_operand = operands[0]
            second_operand = operands[1]
            result = eval(problem)
            if len( first_operand ) > 4 or len( second_operand ) > 4 :
                return "Error: Numbers cannot be more than four digits."    # operand out of range error

        max_space = max( [len( operands[0].strip() ), len( operands[1].strip() )] )
        max_space += 2          # make spaces for operator

        first_row = list( first_operand ).copy()
        while len( first_row ) < max_space :
            first_row.insert(0, ' ')

        second_row = list( second_operand ).copy()
        while len( second_row ) < max_space - 1 :
            second_row.insert(0, ' ')
        second_row.insert(0, operator.group(0))

        dash_row = ['-']*max_space

        result_row = list( str( result ) ).copy()
        while len( result_row ) < max_space :
            result_row.insert(0, ' ')

        if problems[ len(problems) - 1 ] != problem :
            first_row.append('    ')
            second_row.append('    ')
            dash_row.append('    ')
            result_row.append('    ')

        first_operands += first_row
        second_operands += second_row
        dashes += dash_row
        results += result_row

    arranged_problems_list.append( first_operands )
    arranged_problems_list.append('\n')
    arranged_problems_list.append( second_operands )
    arranged_problems_list.append('\n')
    arranged_problems_list.append( dashes )

    if solutions == True :
        arranged_problems_list.append('\n')
        arranged_problems_list.append( results )

    arranged_problems = ''
    for row in arranged_problems_list :
        arranged_problems += ''.join(row)

    return arranged_problems

print( arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) )
