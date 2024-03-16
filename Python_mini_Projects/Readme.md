# Summation algo oop

## Specifications:
State-Space: (m:Z,n:Z,s:H)
Pre-Conditions:(m=m' and n=n')
Post-Conditions:(Pre and s = Summation(m..n) f(i)) where i belongs to Integrs

### Algorithm

s:= 0
loop: i = m...n
s := s + f(i) where i belongs to natural numbers
print(s)

# Counting

## Specifications:
State-Space: (m:N,n:N,c:N)
Pre-Conditions:(m=m' and n=n')
Post-Conditions:(Pre and c = Sum(m..n) & cond[i] == True 1) where i belongs to Integrs

### Algorithm

c:= 0
loop: i = m...n
if cond[i] == True
c := c + 1 where i belongs to natural numbers
else:
False
print(c)


# Maximal Search 

## Specifications
State-Space: (m:N,n:N,max:N,ind:N)
Pre-Conditions:(m=m' and n=n' and m<=n)
Post-Conditions:(Pre and (max,ind) = MAX i=m..n f(i)) where i belongs to Integrs

### Algorithm

max = f(m) , ind = m
loop (i = m+1 .. n)
if f(i) > max
f(i) = max
ind = i
else :
False

print(max,ind)











