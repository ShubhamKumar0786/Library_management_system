a="Welcome to Skill Circle learning Management System"
print(a.center(170))



books={1:'''Book Title : Indian polity
Book Author: M.LAxmikant
Book Price : 728
Book Launch : 2023(latest edition)
Book Description : The Indian polity is the basic structure of the country as defined by the Constitution of India. It is a parliamentary system of government with a federal structure and unitary features.'''
,2:'''Book Title : Ethics,Integrity and Aptitude
Book Author: Ex-IRPS Virendra Pratap Singh
Book Price : 470
Book Launch : 2013
Book Description : 
Ethics:- A set of principles that guide behavior and determine the direction of life. The word ethics comes from the ancient Greek word ethos, which means custom,human character or disposition.
Integrity:- The idea that ethical principles should be carried out in daily life and activities.
Aptitude:- A natural ability or potential to learn or acquire a skill. It can be enhanced with knowledge and training.'''
,3:'''Book Title : Indian Society
Book Author: SC Dube
Book Price : 2
Book Launch : 1990
Book Description : This 1990 book examines the evolution of Indian society, including its diversity, unity, and the functioning of the varna and jati systems.'''
,4:'''Book Title : The Elements of Social Justice
Book Author: L. T. Hobhouse
Book Price : 4092
Book Launch : 1922
Book Description : social justice was based on natural theology and religion, and was an application of justice to social affairs.'''
,5:'''Book Title : The Constitution of India(Handwritten_version)
Book Author:Prem Behari Narain Raizada
Book Price : ________
Book Launch : 1949
Book Description : The Constitution of India is the supreme law of the country, establishing the structure, powers, and duties of the government and its citizens. It was adopted by the Constituent Assembly on November 26, 1949, and came into effect on January 26,1950.'''
      }


def user(x):
    print(books[x])
    
    y=int(input("press 1 to continue or 2 to exit"))

    if y==1:
        print("continue")
        y=user(x)
    elif y==2:
        print("Exit")
        print("Thanks for visiting")

user(3)


