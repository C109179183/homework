alls = set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])

english = set(["John","Mary","Fiona","Claire","Ben","Bill"])

math = set(["Mary","Fiona","Claire","Eva","Ben"])

print("英文與數學都及格",english&math)

print("數學不及格",alls-math )

print("英文及格且數學不及格",english-math)