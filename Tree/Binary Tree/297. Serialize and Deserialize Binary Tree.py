# was easy only but i was not getting how to do it
# time: O(n)
class Codec: 
    def serialize(self, root):
        ans= []  # later will join this by any delimiter and return
        def Preorder(root):
            if root== None:   # for None node, using a speacial char 'N'
                ans.append("N")  
                return
            ans.append(str(root.val))    # since we have to return in string
            Preorder(root.left)
            Preorder(root.right)
        
        Preorder(root)
        print(",".join(ans))
        return ",".join(ans)   # will join all ele in 'ans'(list) into a string with comma between them
        

    def deserialize(self, data):   # whatever ans we have sent during Serialise will be in data
        vals= data.split(",")      # since we have added all the node values with comma in the serialise fn
                                   # so for removing that we splitting at comma
        self.ind= 0   # for using as global
        def Preorder():
            if vals[self.ind]== "N":  # means None node then simply incr 'ind' and return None
                self.ind+= 1
                return None
            node= TreeNode(int(vals[self.ind]))  # first convert into 'int' since data was in string
            self.ind+= 1
            node.left=  Preorder()
            node.right= Preorder()
            return node
        return Preorder()      # was missing return so was getting None