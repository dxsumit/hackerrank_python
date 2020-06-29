def merge_the_tools(string, k):
    for i in range(0 , len(s) , k):
    string=""
    for each in s[i : i+k]:
        if(each not in string):
            string = string + each
    print(string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
