def unify(w1,w2,subst={}):
    if w1==w2:
        return subst
    
    elif isinstance(w1,str):
        return unify_var(w1,w2,subst)
    
    elif isinstance(w2,str):
        return unify_var(w2,w1,subst)
    
    elif isinstance(w1,list) and isinstance(w2,list):
        if len(w1)!=len(w2):
            return "FAILURE"
        
        for i in range(len(w1)):
            subst=unify(w1[i],w2[i],subst)
        
            if subst=="FAILURE":
                return "FAILURE"
            
        return subst
    else:
        return "FAILURE"
    
def unify_var(var,x,subst):
    if var in subst:
        return unify(subst[var],x,subst)
    else:
        subst[var]=x
        return subst
# Example usage:
W1 = ["likes", ["John", "Mary"], ["pizza", "sushi"]]
W2 = ["likes", ["Bob", "Alice"], ["pizza", "sushi"]]

print(unify(W1, W2))