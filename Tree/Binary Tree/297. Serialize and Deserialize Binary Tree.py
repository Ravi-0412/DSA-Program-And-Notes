# was easy only but i was not getting how to do it
# for Serialise: just store the preorder with 'none' value also.
# for Deserialise: just make tree from above returned string. 
# Since we have returned using preorder, so we will make tree also keeping in mind how values will go the subtrees.
# in preorder we keep on going left so whenever we will get any 'Non-None' node means that will go the left side and when we will get 'None' then they will go to the left.
# (for this same thing will happen i.e NOT None to left ...)
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
        # print(",".join(ans))
        return ",".join(ans)   # will join all ele in 'ans'(list) into a string with comma between them
        

    def deserialize(self, data):   # whatever ans we have sent during Serialise will be in data
        vals= data.split(",")      # converting into list. since we have added all the node values with comma in the serialise fn
                                   # so splitting at when we will see ','.
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
        return Preorder()      
    

# shorter way of serialisation.
# just preorder only. Just above logic only.
def serialize(self, root):   
        if not root:
            return "N"
        s= ",".join([str(root.val) , self.serialize(root.left) , self.serialize(root.right)]) 
        return s


# Java
""""
public class Codec {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        preOrderTraverse(root, sb);
        sb.deleteCharAt(sb.length() - 1); // delete the last redundant comma ","
        return sb.toString();
    }

    void preOrderTraverse(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("null,");
            return;
        }
        sb.append(root.val);
        sb.append(",");
        preOrderTraverse(root.left, sb);
        preOrderTraverse(root.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        nodes = data.split(",");
        return dfs();
    }
    
    int i = 0;
    String[] nodes;

    TreeNode dfs() {
        String val = nodes[i];
        if(val.equals("null")) {
            i += 1 ;
            return null;
        }
        i += 1;
        TreeNode root = new TreeNode(Integer.parseInt(val));
        root.left = dfs();
        root.right = dfs();
        return root;
    }
}
"""