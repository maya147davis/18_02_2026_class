#-----------------------------------------------------
# given information
#-----------------------------------------------------
# Languages good for Web Development
languages_web = {
    "JavaScript",
    "TypeScript",
    "Python",
    "PHP",
    "Ruby",
    "Go",
    "Java",
    "C#"
}
# Languages good for Data Science/Machine Learning
languages_data_science = {
    "Python",
    "R",
    "Julia",
    "Scala",
    "MATLAB",
    "Java",
    "SQL"
}
# Languages good for System Programming
languages_systems = {
    "C",
    "C++",
    "Rust",
    "Go",
    "Zig",
    "Assembly"
}
# Languages good for Mobile Development
languages_mobile = {
    "Swift",
    "Kotlin",
    "Java",
    "Dart",
    "JavaScript",
    "C#"
}
#------------------------------------------------
# QA
#------------------------------------------------
print("\n🌐 Languages for Web Development:")
print(sorted(languages_web))
print("\n📊 Languages for Data Science:")
print(sorted(languages_data_science))
print("\n⚙️  Languages for System Programming:")
print(sorted(languages_systems))
print("\n📱 Languages for Mobile Development:")
print(sorted(languages_mobile))


print("\n❓ Which languages are good for BOTH Web AND Data Science?")
both_web_data=languages_web&languages_data_science
print(both_web_data)
print("\n❓ Languages that can do Web, Mobile, OR Data Science?")
print(sorted(languages_web|languages_data_science|languages_systems))
print("\n❓ Languages ONLY for System Programming (not web/mobile/data)?")
print(languages_systems-languages_web-languages_data_science-languages_mobile)
print("\n❓ Which languages work for Web but NOT Mobile?")
print(languages_web-languages_mobile)
print("\n❓ Is 'Python' in the web development set?")
if 'Python' in languages_web:
    print("yes")
print("\n❓ The ultimate polyglot language (in ALL four categories)?")
if languages_web&languages_mobile&languages_systems&languages_data_science==set():
    print("there is no such language")
else:
    print(languages_web&languages_mobile&languages_systems&languages_data_science)
modern_web = {"JavaScript", "TypeScript", "Python"}
print("\n❓ Is modern_web a PROPER subset of web languages (PROPER = smaller, not equal)?")
if modern_web<languages_web:
    print("yes")
else:
    print("no")