    def isSameTree(self, p, q):
        
        def isSameTreeRec(proot, qroot):
            
            if proot == None and qroot == None:
                return True
            
            elif proot != None and qroot != None:
                    
                if proot.val == qroot.val:
                    return isSameTreeRec(proot.left, qroot.left) and isSameTreeRec(proot.right, qroot.right)
                    
                else:
                    return False
            
            else:
                return False
        
        return isSameTreeRec(p,q)
