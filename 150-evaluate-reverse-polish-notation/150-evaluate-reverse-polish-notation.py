class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		"""
		time complexity: O(N)
		space complexity: O(N)
		"""
		stack = []
		operators = set("+-*/")
		for ch in tokens:
			#pop two numbers from the stack and perform operation,
			#then put the result back to the stack
			if ch in operators:
				second_num = stack.pop()
				first_num = stack.pop()            
				if ch == "+":
					stack.append(first_num + second_num)
				elif ch == "-":
					stack.append(first_num - second_num)
				elif ch == "*":
					stack.append(first_num * second_num)
				else:
					stack.append(int(first_num / second_num))
			#it's a number
			else:
				stack.append(int(ch))

		return stack.pop()