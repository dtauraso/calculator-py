
import hierarchial_context_sensitive_state_machine.hierarchial_context_sensitive_state_machine as hcssm

from collections import OrderedDict as od


def getA(node, var_store):
	# all chains start with this function
	var_store['operation_vars']['chain_length'] = 0

	#print(var_store['operation_vars']['kind_of_number'])
	i = var_store['i']
	input_ = var_store['input']
	var_store['operation_vars']['a'] = input_[i]
	var_store['operation_vars']['chain_length'] += 1
	var_store['i'] += 1
	#print(var_store)

	return True


def getB(node, var_store):

	#print(var_store['operation_vars']['kind_of_number'])
	i = var_store['i']
	input_ = var_store['input']
	var_store['operation_vars']['b'] = input_[i]
	var_store['operation_vars']['chain_length'] += 1
	var_store['i'] += 1
	#print(var_store)

	return True


def isOp(node, var_store):
	# check current operand with jth operand
	i = var_store['i']
	input_ = var_store['input']
	#print(input[i])
	j = var_store['lex_vars']['j']
	operators = var_store['lex_vars']['operators']
	return input_[i] == operators[j]



def evaluate(node, var_store):

	#print(var_store)
	#print(var_store['input'])
	i = var_store['i']
	input_ = var_store['input']
	var_store['operation_vars']['b'] = input_[i]
	#print(var_store['input'])

	a = int(var_store['operation_vars']['a'])
	b = int(var_store['operation_vars']['b'])

	j = var_store['lex_vars']['j']
	operators = var_store['lex_vars']['operators']
	operations = var_store['lex_vars']['operations']

	var_store['operation_vars']['a'] = operations[operators[j]] (a, b)
	var_store['operation_vars']['b'] = 0
	var_store['i'] += 1
	str_a = str(var_store['operation_vars']['a'])


	chain_length = var_store['operation_vars']['chain_length']

	# maybe i - 1
	before_the_chain = var_store['input'][0: i - 2]

	before_the_chain_len = len(before_the_chain)
	the_chain = str_a

	after_the_chain = var_store['input'][i + 1: len(var_store['input'])]

	var_store['input'] = before_the_chain

	var_store['input'].append(the_chain)
	for k, next_char in enumerate(after_the_chain):

		var_store['input'].append(after_the_chain[k])


	var_store['i'] = before_the_chain_len

	return True


def ignoreOp(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	#print(input[i])
	j = var_store['lex_vars']['j']
	operators = var_store['lex_vars']['operators']

	if endOfInput(node, var_store):

		return False

	# need to prove input[i] is an operator, but not operators[j]
	if  (input_[i] in operators)  and (input_[i] != operators[j]):

		var_store['operation_vars']['a'] = 0
		return True

	return False




def endOfInput(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	return i >= len(input_)


def inputIsInvalid(node, var_store):
	print('your input is invalid')
	return True


def noMoreInput(node, var_store):

	#print('at noMoreInput')
	return endOfInput(node, var_store)




def saveDigit(node, var_store):
	char = getChar(store, var_store)

	return char >= '0' and char <= '9'








def isWhiteSpace(node, var_store):

	return getChar(node, var_store) == ' '

def isDigit(node, var_store):
	char = getChar(node, var_store)
	#print(var_store, char)
	return char >= '0' and char <= '9'


def isNotDigit(node, var_store):
	return not isDigit(store, var_store)



def getChar(node, var_store):
	i = var_store['i']
	input_ = var_store['input']
	char = input_[i]
	return char


def parseChar(node, var_store):

	#console.log('in parseChar', node)
	#print('node', node)
	state = node[0]
	case_ = node[1]
	i = var_store['i']
	input_ = var_store['input']
	#console.log(i, input.length)

	#console.log('here is var store', var_store)
	#console.log('parseChar', node, i)
	if (i < len(input_)):

		#console.log(var_store)
		#console.log(state, case_, var_store['parsing_checks'])
		if (var_store['parsing_checks'][state][case_](node, var_store)):

			var_store['i'] += 1
			#var_store['validate_vars']['k'] += 1
			#var_store['validate_vars']['input_i'] += 1
			#var_store['operation_vars']['chain_length'] += 1
			return True





	return False



def mult(a, b):

	return a * b

def divide(a, b):

	return a / b

def plus(a, b):

	return a + b

def minus(a, b):

	return a - b




parsing_checks = {

	'op' : {'0':isOp},
	'value_ignore' : {'0': isDigit},
	'op_ignore' : {'0': ignoreOp},
	' ' : {'0':isWhiteSpace},

}

parents = {

	# only the parent
	' ' : {'0':{}},
	'a' : {'0':{'evaluate_expression': '0'}},
	'op' : {'0':{}},
	'b' : {'0':{}, 'evaluate':{}},
	'op_ignore' : {'0':{}},
	'value_ignore' : {'0':{'ignore':'0'}, 'valid_op': {}},
	'error' : {'0':{}},
	'invalid' : {'0': {}},
	'validate' : {'0':{}},
	'evaluate_expression' : {'0':{}},

	'reset_for_next_round_of_input' : {'0':{}},
	'end_of_evaluating' : {'0':{}},
	'input_has_1_value':{'0':{}},

	'split' : {'0':{'root':'0'}},

	'char': {'0':{'split':'0'}},
	'last_to_save' : {'0':{}},

	'save' : {'0':{}},
	'init' : {'0':{}}
}


def returnTrue(node, var_store):
	return True

def returnFalse(node, var_store):
	return False

def resetForNextRound(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	#print('here')
	#print(i >= len(input_))
	if i >= len(input_):

		#print(node)
		var_store['lex_vars']['j'] += 1
		var_store['i'] = 0
		return True


	return False


def showAndExit(node, var_store):

	input_ = var_store['input']
	#print(input_)
	if len(input_) == 1:

		print(input_[0])
		return True


	return False






def collectChar(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	#print(input[i])
	if input_[i] != ' ':

		var_store['collected_string'] += input_[i]
		var_store['i'] += 1
		return True


	return False

def save(node, var_store):

	#print('here')

	i = var_store['i']
	input_ = var_store['input']
	#print(input_, i)
	if input_[i] == ' ':

		collected_string = var_store['collected_string']
		var_store['expression'].append(collected_string)
		return True


	return False

def init(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	if (input_[i] != ' '):

		var_store['collected_string'] = ''
		return True

	return False


def lastToSave(node, var_store):

	#print(var_store)
	#exit()
	if endOfInput(node, var_store):

		collected_string = var_store['collected_string']
		var_store['expression'].append(collected_string)
		var_store['input'] = var_store['expression']
		var_store['i'] = 0
		var_store['expression'] = []
		var_store['collected_string'] = ''
		return True

	return False

def validOp(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	if isOp(node, var_store):

		var_store['operation_vars']['a'] = input_[i - 1]
		return True

	return True

def isNumber(number_string):
	#print(number_string)
	try:
		i = int(number_string)
		return True
	except ValueError as verror:
		return False
def validate(node, var_store):

	# expressions list
	# len > 3
	# alternate # and op
	# make sure the alternate starts and ends with #
	i = 1
	#print(var_store)

	input_ = var_store['input']

	if len(input_) >= 3:

		if not isNumber(input_[0]):


			return False

		while i < len(input_):

			# 2, 4, 6
			if i % 2 == 1:

				# not (input_[i] in var_store['lex_vars']['operators'])
				if not (input_[i] in var_store['lex_vars']['operators']):

					return False


			# 1, 3, 5
			else:

				if not isNumber(input_[i]):

					return False



			i += 1

		if not isNumber(input_[ -1 ]):

			return False


		return True




	return False

'''
passes (checked by wolfram alpha)
'1 + 2 + 3 + 4'
'1 + 2 + 3 + 4 - 5 + 6 + 7 - 8 - 9 + 10 + 11 + 12'
'1 + 2 + 3 + 4 - 5 + 6 * 7 - 8 - 9 + 10 * 11 + 12'
'''
vars = {
	'input' : '1 + 2 + 3 + 4 - 5 + 6 * 7 - 8 - 9 + 10 * 11 + 12', # '1 '
	# 10 - 18 - 8 - 42
	# 10 - 5 +
	'expression' : [],
	'collected_string' : '',
	'i' : 0,
	'parents' : parents,

	'operation_vars' : {

		'a' : 0,

		'b' : 0},

	'lex_vars' : {
		'operators' : ['*', '/', '-', '+'],
		'j' : 0,
		'operations' : {'*': mult, '/': divide, '+': plus, '-': minus}},
	# this control graph uses string for states and cases
	'node_graph2' : [


		# current state -> [current_context [list of (next_state, next_context)]]
		['split' , [
			['next', [['0', [['validate','0'], ['invalid','0']]]]],
			['children',  [['0', [['char','0']]]]],
			['functions', [['0', returnTrue ]]]]],

		['validate' ,  [
			['next', [['0', [['evaluate_expression', '0']]]]],
			['children', [['0', []]]],
			['functions', [['0', validate ]]]]],

		['evaluate_expression' ,  [
			['next', [['0', [['input_has_1_value','0'],['evaluate_expression','0']]]]],
			['children',   [['0', [['a','0']]]]],
			['functions', [['0', returnTrue ]]]]],



		['input_has_1_value' ,  [
			['next', [['0', []]]],
			['children',  [['0', []]]],
			['functions', [['0',showAndExit]]]]],

			# split

			['char',  [
				['next', [['0', [['last_to_save', '0'], ['char', '0'], ['save', '0']]]]],
				['children',   [['0', []]]],
				['functions', [['0',collectChar]]]]],

			['save',  [
				['next', [['0', [[' ', '0']]]]],
				['children',   [['0', []]]],
				['functions', [['0',save]]]]],

			[' ' , 	 [
				['next', [['0',[[' ','0'],['init','0']]]]],
				['children',   [['0', []]]],
				['functions', [['0',parseChar]]]]],

			['init', [
				['next', [['0', [['char', '0']]]]],
				['children',   [['0', []]]],
				['functions', [['0', init]]]]],

			['last_to_save' ,  [
				['next', [['0', []]]],
				['children',   [['0', []]]],
				['functions', [['0', lastToSave]]]]],

			# evaluate_expression
			['a' ,  [
				['next', [['0' , [['reset_for_next_round_of_input','0'], ['op','0'], ['op_ignore','0']]]]],
				['children',   [['0', []]]],
				['functions' , [['0',getA]]]]],

			['op' ,  [
				['next', [['0',[['error', '0'], ['b','evaluate']]]]],
				['children',   [['0', []]]],
				['functions' , [['0', parseChar]]]]],

			['b' ,  [
				['next', [['evaluate',[['reset_for_next_round_of_input','0'], ['a','0'], ['op_ignore','0']]]]],
				['children',    [['evaluate',[]]]],
				['functions' , [['evaluate', evaluate]]]]],

			['op_ignore' ,  [
				['next', [['0',[['error', '0'], ['value_ignore','0']]]]],
				['children',   [['0', []]]],
				['functions' , [['0',parseChar]]]]],

			['value_ignore' , 	 [
				['next', [['0',[['reset_for_next_round_of_input','0'], ['op_ignore','0'], ['value_ignore', 'valid_op']]], ['valid_op', [['op','0']]]]],
				['children',  [['0',[]], ['valid_op', []]]],
				['functions' , [['0',parseChar], ['valid_op', validOp]]]]],
			['reset_for_next_round_of_input',  [
				['next', [['0', [['end_of_evaluating', '0']]]]],
				['children',    [['0', []]]],
				['functions', [['0',resetForNextRound]]]]],

			['end_of_evaluating' ,  [
				['next', [['0', []]]],
				['children',	[['0', []]]],
				['functions', [['0',returnTrue]]]]],

		['error' ,  [
			['next', [['0', []]]],
			['children',   [['0', []]]],
			['functions', [['0', noMoreInput]]]]],

		['invalid' ,  [
			['next', [['0', []]]],
			['children',   [['0', []]]],
			['functions', [['0', inputIsInvalid]]]]]]


			# any next states having {} means it is a finishing state(but having no edges as True signals an error )
			# {'next': [], 'children':[], 'functions':[]}
			# {'next': {'0': {}}, 'children':{'0': {}}, 'functions':{'0'}}


				 # setKindOfNumberToA

		,

	'parsing_checks' : parsing_checks

}

#calculator_reducer = createStore(nodeReducer4)
# -1 so highest level of graph isn't printed with an indent
hcssm.visit(['split', '0'], vars, 0)

print('done w machine')
