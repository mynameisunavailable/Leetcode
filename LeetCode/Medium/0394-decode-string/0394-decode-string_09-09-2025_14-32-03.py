# remove everything uptil and including [ counting from back
def expand_last_bracket(stack: list) -> list:
    bracketed_list_rev = []
    for i in reversed(stack):
        if i == "[":
            stack.pop(-1) #remove bracket
            break
        else:
            bracketed_list_rev.append(i)
            stack.pop(-1) #remove alpha
    bracketed_list_rev = list(reversed(bracketed_list_rev))
    # print(bracketed_list_rev)

    repeated_rev = [] 
    for i in reversed(stack):
        if i.isdigit():
            repeated_rev.append(i)
            stack.pop(-1)
        else:
            break
    #get correct orientated times
    repeated_rev = "".join(reversed(repeated_rev))
    repeated_rev = int(repeated_rev)
    # print(repeated_rev)

    result_list = []
    for i in range(repeated_rev):
        result_list.extend(bracketed_list_rev)
    
    return result_list
        
class Solution:
    def decodeString(self, s: str) -> str:
        s_list = list(s)
        stack = []
        final_list = []
        temp_stack = []
        for i in s_list:
            if i == "]":
                # print("close: ", i)
                temp_stack = expand_last_bracket(stack)
                #if is last bracket in stack then append to final list
                if stack == []:
                    final_list.extend(temp_stack)
                else:
                    stack.extend(temp_stack)
            else:
                stack.append(i)
        
        #process remainder stack
        for i in stack:
            final_list.append(i)
            
        result = "".join(final_list)
        return result