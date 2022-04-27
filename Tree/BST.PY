class Node:
    def __init__(self,data= None):
        self.data= data
        self.left= None
        self.right= None
    
class BST:

    def BuildBSTRecursive(self,root,ele):
        if root== None:
            return Node(ele)
        elif ele <root.data:
            root.left= self.BuildBSTRecursive(root.left, ele)
        else:
            root.right= self.BuildBSTRecursive(root.right, ele)
        return root  # return the root always as we have to start checking from root  
    
    def SearchMin(self,root):
        if root== None:
            return
        if root.left== None:
            return root.data
        return self.SearchMin(root.left)

    def SearchMax(self,root):
        if root== None:
            return
        if root.right== None:
            return root.data
        return self.SearchMax(root.right)
    
    def SearchKey(self,root, key):
        if root== None:
            print("{} is not present or tree is empty".format(key))
            return
        if root.data== key:
            print("{} is present at node address {}".format(key,root))
        elif key< root.data:
            self.SearchKey(root.left, key)
        else:
            self.SearchKey(root.right, key)
        
    # traversals
    def PreorderRecursive(self,root):
        if root== None:
            return
        print(root.data,end=" ")
        self.PreorderRecursive(root.left)
        self.PreorderRecursive(root.right)
    
    def PreorderIterative(self,root):
        if root== None:
            return 
        stack= []
        stack.append(root)
        while stack:
            curr= stack.pop()
            print(curr.data, end=" ")
            if curr.right: # first push the right subtree in the stack as we have to 
                           # print 'left' side first and stack is LIFO
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)


    def InorderRecursive(self,root):
        if root== None:
            return
        self.InorderRecursive(root.left)
        print(root.data,end=" ")
        self.InorderRecursive(root.right)  

    # def InorderIterative(self,root):
    #     if root== None:
    #         return 
    #     stack= []
    #     stack.append(root)
    #     curr= root
    #     while stack :
    #         if curr.left== None:
    #             temp= stack.pop()
    #             print(temp.data, end=" ")
    #             if temp.right:
    #                 curr= temp.right
    #                 stack.append(temp.right)
    #         if curr.left:
    #             stack.append(curr.left)
    #             curr= curr.left
    
    # another concise way of iterative approach of inorder traversal
    def InorderIterative(self,root):
        if root== None:
            return 
        stack= []
        curr= root
        while True:
            # reach the left bottom most node
            if curr:
                stack.append(curr)
                curr= curr.left
            # if no left child then we have to print the stack top and append the 'poped.right'
            elif stack:
                temp= stack.pop()
                print(temp.data, end=" ")
                curr= temp.right
            else:
                break

    def PostorderRecursive(self,root):
        if root== None:
            return
        self.InorderRecursive(root.left) 
        self.InorderRecursive(root.right)
        print(root.data,end=" ")
    

    def postorderIterative1(self, root):
        stack, ans= [], []
        if root== None:
            return root
        stack.append(root)
        while stack:
            curr= stack.pop()
            ans.append(curr.data)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        # now print the 'ans' in the reverse order
        while ans:
            print(ans.pop(),end= " ")
    
    # using only single stack(try later)
    def PostorderIterative(self,root):
        if root== None:
            return 
        stack= []
        stack.append(root)
        curr, pre= root, None
        while stack :
            if curr.left== None:         
                if curr.right:
                    stack.append(curr.right)
                    pre= curr
                    curr= curr.right
                else: # means curr.left== None and curr.right== None
                    # print("pre data " ,pre.data)
                    temp= stack.pop()
                    print(temp.data, end=" ")
                    curr= pre.right
                    stack.append(curr)
                    pre= None
                    # print("curr data", curr.data)
            if curr.left:
                stack.append(curr.left)
                pre= curr
                curr= curr.left

    def deleteNode(self, root, key):
        if root== None:
            return root
        if key< root.data:
            root.left= self.deleteNode(root.left, key)
        elif key >root.data:
            root.right= self.deleteNode(root.right, key)
        else:
            if root.left== None and root.right== None:
                root= None
            elif root.left!= None and root.right== None:
                root= root.left
            elif root.right!= None and root.left== None:
                root= root.right
            else:
                temp= self.SearchMin1(root.right)
                root.data= temp.data
                root.right= self.deleteNode(root.right, root.data)
        return root
                
    def SearchMin1(self,root):
        if root== None:
            return
        if root.left== None:
            return root
        return self.SearchMin(root.left)
    
    def TotalNodes(self, root):
         # just do any traversal and count
        # count= 0
        # if root== None:
        #     return 0
        # count+= 1
        # smallAns= self.TotalNodes(root.left)
        # count+= smallAns
        # smallAns1= self.TotalNodes(root.right)
        # count+= smallAns1
        # return count

        # concise way of writing
        if root== None:
            return 0
        return 1+ self.TotalNodes(root.left) + self.TotalNodes(root.right)
    # Later try by iterative way


    def LeafNode(self, root):
        # count= 0
        # if root== None:
        #     return 0
        # if root.left== None and root.right== None:
        #     return 1
        # smallAns= self.LeafNode(root.left)
        # smallAns1= self.LeafNode(root.right)
        # count+= smallAns + smallAns1
        # return count

        # concise way
        count= 0
        if root== None:
            return 0
        if root.left== None and root.right== None:
            return 1
        return self.LeafNode(root.left) + self.LeafNode(root.right)
        # Later try by iterative way

    def Depth(self,root):
        if root== None:
            return 0
        return 1 + max(self.Depth(root.left), self.Depth(root.right))
    # try later by iterative way

root= None
b= BST()
arr= [50,15,62,5,20,58,91,3,8,37,60,24]
for ele in arr:
    root= b.BuildBSTRecursive(root,ele)

# now insert into already made BST
# root= b.BuildBSTRecursive(root,23)

# print("minimum ele in BST is: ", b.SearchMin(root))
# print("maximum ele in BST is: ", b.SearchMax(root))

# b.SearchKey(root,20)
# b.SearchKey(root,13)

# print("Preorder traversal Recursive is: ")
# b.PreorderRecursive(root)
# print()
# print("Preorder traversal Iterative is: ")
# b.PreorderIterative(root)
# print()

# print("inorder traversal recursive is: ")
# b.InorderRecursive(root)
# print()
# print("inorder traversal Iterative is: ")
# b.InorderIterative(root)
# print()


# print("Postorder traversal Recursive is: ")
# b.PostorderRecursive(root)
# print()
# print("Postorder traversal Iterative is: ")
# b.postorderIterative1(root)
# print()

# b.deleteNode(root,24)
print("inorder traversal Iterative is: ")
b.InorderIterative(root)
print()
# print("total no of nodes: ", b.TotalNodes(root))
# print("no of leaf nodes: ", b.LeafNode(root))
print("depth of the tree is: ",b.Depth(root))