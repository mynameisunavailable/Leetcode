#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//get current pos of location needed to be appended return new end
char* append_char_insitu(char* string, char c)
{
    *string = c;
    string++;
    *string = '\0';
    return string;
}

//takes string[] return malloced reverse string
char* reverse_string(char* string)
{
    int length = strlen(string);
    char* reversed_string = malloc((length + 1) * (sizeof(char)));
    char* string_p = reversed_string;
    for (int j = length - 1; j >= 0; j--)
    {
        string_p = append_char_insitu(string_p, string[j]);
    }
    return reversed_string;
}

void extract_rev_alpha(char* stack, int* stack_size, char* rev_string)
{
    char* rev_string_p = rev_string;

    //check alpha
    (*stack_size)--; //go before \0
    while (*stack_size > 0)
    {
        if (stack[*stack_size] == '[')
        {
            (*stack_size)--;
            break;
        }
        else
        {
            rev_string_p = append_char_insitu(rev_string_p, stack[*stack_size]);
            // printf("%c", stack[*stack_size]);
            (*stack_size)--;
        }
    }
    (*stack_size)++; //write back \0
    stack[*stack_size] = '\0';
}

int extract_times(char* stack, int* stack_size)
{
    //check times
    char* times_rev = malloc(sizeof(char) * (3 + 1)); //max 300
    times_rev[0] = '\0';
    char* times_rev_start = times_rev;
    int times = 0;
    (*stack_size)--;
    while (*stack_size >= 0 && isdigit(stack[*stack_size]) != 0)
    {
        times_rev = append_char_insitu(times_rev, stack[*stack_size]);
        (*stack_size)--;
    }
    char* times_rev_rev = reverse_string(times_rev_start);
    times = atoi(times_rev_rev);
    // printf("times: %d", times);
    free(times_rev_start);
    free(times_rev_rev);
    return times;
}

char* expand_last_bracket(char* stack, int* stack_size)
{
    size_t cap = *stack_size + 1;
    if (cap == 0) cap = 1;
    char* rev_string = malloc((cap)* sizeof(char));
    rev_string[0] = '\0';

    //get rev string
    extract_rev_alpha(stack, stack_size, rev_string);
    //get times to be repeated
    int times = extract_times(stack, stack_size);
    
    int rev_string_size = strlen(rev_string);
    char* result = malloc(sizeof(char) * times * rev_string_size + 1);
    char* result_p = result;
    for (size_t i = 0; i < times; i++)
    {
        for (int j = rev_string_size - 1; j >= 0; j--)
        {
            result_p = append_char_insitu(result_p, rev_string[j]);
        }
    }
    *result_p = '\0';
    
    //add null
    (*stack_size)++;
    stack[*stack_size] = '\0';
    
    free(rev_string);
    return result;
}

char* decodeString(char* s) 
{
    int s_len = strlen(s);
    char* stack = malloc(1024 * 10 * sizeof(char));
    int stack_mem_size = 1024;
    char* temp_stack;

    char* final_result = malloc(1024 * 10 * sizeof(char));
    int final_result_mem_size = 1024;
    final_result[0] = '\0';
    int final_result_size = 1;

    char* stack_p = stack;
    *stack = '\0';
    int stack_size = 0;
    int depth = 0;
    while (*s)
    {
        if (*s == ']')
        {
            temp_stack = expand_last_bracket(stack, &stack_size);
            depth--;
            if (depth == 0)
            {
                strcat(final_result, stack);
                stack[0] = '\0';
                strcat(final_result, temp_stack);
                final_result_size += strlen(temp_stack);
                free(temp_stack);
                stack_p = stack;
            }   
            else
            {
                strcat(stack, temp_stack);
                stack_size += strlen(temp_stack);
                free(temp_stack);
                //reset stack_p
                stack_p = stack;
                while (*stack_p)
                {
                    stack_p++;
                }
            }
            s++;
        }
        else
        {
            if (*s == '[')
            {
                depth++;
            }
            stack_p = append_char_insitu(stack_p, *s);
            stack_size++;
            s++;
        }
        
        // if (stack_size >= stack_mem_size)
        // {
        //     stack = realloc(stack, stack_size + (1024 * sizeof(char)));
        //     stack_mem_size += 1024;
        //     stack_p = stack + stack_size;
        // }
        // if (final_result_size > final_result_mem_size)
        // {
        //     final_result = realloc(final_result, final_result_size + (1024 * sizeof(char)));
        //     final_result_mem_size += 1024;
        // }
    }
    // printf("%s", stack);
    strcat(final_result, stack);

    free(stack);
    return final_result;
}
