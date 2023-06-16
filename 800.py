import time
def counter(s):
    for let in s:
        count=0
        for sub_let in s:
            if let == sub_let:
                count+= 1
        #print(let, count)
start = time.time()
for i in range(1_000_000):
    counter("bbsimonn")
end = time.time()

#print(time.time())
counter("bbsimonn")

def counter(s):
    for let in set(s):
        count=0
        for sub_let in s:
            if let == sub_let:
                count+= 1
        print(let, count)
print(end - start)

counter("queue")
