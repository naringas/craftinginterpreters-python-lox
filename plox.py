import sys

from scanner import Scanner, Token, TokenType
from parser import Parser
from interpreter import Interpreter
from statements import StmtVisitor


global hadError


def runPrompt():
	while True:
		try:
			line = input("plox> ")
		except (EOFError, KeyboardInterrupt):
			print("\n\nbuhbuy!")
			break
		else:
			# Interpreter().interpret(Parser(Scanner(line).scanTokens()).parse())
			run(line)
		hadError = False

def runFile(filepath):
	print(f'readin {filepath}')
	with open(filepath, 'r', encoding="utf-8") as f:
		run(f.read())

def run(source):
	print('TOKENS')
	tokens = Scanner(source).scanTokens()
	for t in tokens:
		print(t)

	print('\nSTATEMENTS')
	stmts_list = Parser(tokens).parse()
	stmt_printer = StmtVisitor()
	for stmt in stmts_list:
		if stmt is not None:
			stmt_printer.print(stmt)
		else:
			print('none stmt')

	print('\nINTERPRETATION')
	i = Interpreter()
	for stm in stmts_list:
		if stm is not None:
			i.interpret(stm)
		else:
			print(f'skip none stmt `{stm}`')

	print()

if __name__ == "__main__":
	hadError = False
	# print(sys.argv)
	if len(sys.argv) == 1:
		runPrompt()
	elif len(sys.argv) == 2:
		runFile(sys.argv[1])
		if hadError:
			sys.exit(65)  # uhm say wha!?
