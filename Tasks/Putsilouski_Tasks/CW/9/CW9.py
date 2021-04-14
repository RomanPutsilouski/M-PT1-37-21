def get_value_or_default(t):
    def get_value(l,i):
        if i>len(l)-1:
            return t
        else:
            return l[i]
    return get_value

num = get_value_or_default(0)
string = get_value_or_default("_")
n_1 = [1,2,3]
s_1 = ["a","b","c"]
print(num(n_1, 1))
print(num(n_1,101))
print(string(s_1,1))
print(string(s_1,101))