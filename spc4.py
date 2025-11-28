m_passed={1,2,6,7,8,9,5}
s_passed={0,3,4,6,7,9}

print(len(m_passed))
print(len(s_passed))
print(m_passed.difference(s_passed))
print(s_passed.difference(m_passed))

print(len(m_passed.intersection(s_passed)))

if m_passed in s_passed:
    print("maths are subset of science")
else:
    print("no")

if s_passed in m_passed:
    print("science are subset of maths")
else:
    print("no")


sun = m_passed.issubset(s_passed)
print(sun)


sum = m_passed.issuperset(s_passed)
print(sum)


#que2
