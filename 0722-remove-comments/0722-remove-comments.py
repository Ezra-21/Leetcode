class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
        flag = False
        answer = []
        temp = ''

        for word in source:
            if not flag:
                temp = ''
            i = 0
            while i < len(word):
                if flag:
                    if i<len(word)-1 and  word[i]=='*' and word[i+1]=='/':
                        flag = False
                        i+=1 
                else:
                    if i<len(word)-1 and  word[i]=='/' and word[i+1]=='*':
                        flag = True
                        i+=1
                    elif i<len(word)-1 and  word[i]=='/' and word[i+1]=='/':
                        break
                    else:
                        temp+=word[i]
                        
                i+=1
            
                    
            if not flag:
                if temp!='':
                    answer.append(temp)
        return answer


                

        