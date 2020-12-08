/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum=0;
        ListNode *l3=NULL;
        
        ListNode **node= &l3;   // node is a pointer to pointer, save the head of poineter to pointer

        ListNode * CurrentNodePointer = NULL; // pointer to current node            
        // ListNode * NextNodePointer = NULL;

        
        while(l1!=NULL||l2!=NULL||sum>0)
        {
            if(l1!=NULL)
            {
                sum+=l1->val;
                l1=l1->next;
            }
            if(l2!=NULL)
            {
                sum+=l2->val;
                l2=l2->next;
            }
            
            // (*node)=new ListNode(sum%10); // pointer to new ListNode object.
            ListNode * l4 = new ListNode(sum%10);
            (*node) = l4;
            
            sum/=10;

            //node=&((*node)->next); // can be separate into two steps.

            CurrentNodePointer = (*node); // pointer to current node            
            // ListNode * NextNodePointer = new ListNode(CurrentNodePointer -> next);
            // node = &NextNodePointer;
            node = &(CurrentNodePointer->next);
            
            
            
        }        
        return l3; 
    }
};
