class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        curstr=''
        for c in s:
            if c=='(':
                if curstr:
                    st.append(curstr)
                    curstr=''
                st.append(c)
            elif c.isalpha():
                curstr+=c
            else:
                while st and st[-1]!='(':
                    curstr=st.pop()+curstr
                if st and st[-1]=='(':
                    st.pop()
                    st.append(curstr[::-1])
                    curstr=''
        if curstr:
            st.append(curstr)
        return ''.join(st)