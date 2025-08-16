
#include <stdlib.h>
struct ListNode* createnode(int value)
{
    struct ListNode* node = malloc(sizeof(struct ListNode));
    node->val = value;
    node->next = NULL;
    return (node);
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
    struct ListNode* res0 = createnode(0);
    struct ListNode* cur = res0;
    int n;

    n = 0;
    while (l1 != NULL || l2 != NULL || n > 0)
    {
        if (l1 != NULL)
        {
            n = n + l1->val;
            // printf("%d" ,l1->val);
            l1 = l1->next;
        }
        if (l2 != NULL)
        {
            n = n + l2->val;
            // printf("%d" ,l2->val);
            l2 = l2->next;
        }

        cur->next = createnode(n % 10);
        n = n / 10;
        cur = cur->next;
    }
    return (res0->next);
}
