﻿# Επίλυση Δραστηριοτήτων του μαθήματος Προγραμματισμός Υπολογιστών
# Γ' ΕΠΑΛ
# ΤΟΜΕΑΣ ΠΛΗΡΟΦΟΡΙΚΗΣ
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

ΚΕΦΑΛΑΙΟ 11ο ΑΝΤΙΚΕΙΜΕΝΟΣΤΡΕΦΗΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ
Δραστηριότητα 2 /σελίδα 222
Να ορίσετε κλάση με όνομα Student η οποία θα έχει τρεις ιδιότητες για τον αριθμό
μητρώου, το ονοματεπώνυμο και τους βαθμούς σε 8 μαθήματα (πίνακας).
Επίσης να ορίσετε τις παρακάτω μεθόδους της κλάσης:
I. Μια μέθοδο για την ανάθεση τιμών στις ιδιότητες ενός αντικειμένου.
II. Μια μέθοδο για την εμφάνιση των τιμών των ιδιοτήτων ενός αντικειμένου.
III. Μια μέθοδο για τον υπολογισμό και την επιστροφή του μέσου όρου βαθμο-
λογίας στα 8 μαθήματα.
Στη συνέχεια να ορίσετε ένα στιγμιότυπο της κλάσης Student με όνομα Chris και
να χρησιμοποιήσετε τις παραπάνω μεθόδους για να δώσετε τιμή στις ιδιότητες του
αντικειμένου, να τις εμφανίσετε και να υπολογίσετε το μέσο όρο βαθμολογίας του.

'''

# Δημιουργία Κλάσης φοιτητή
class Student:
    def __init__(self, am, name, grades):
        self.am = am
        self.name = name
        self.grades = grades
    def updateStudent(self,am,name,grades):
        self.am = am
        self.name = name
        self.grades = grades
    def printStudent(self):
        print self.am, self.name, self.grades
    def calcAverage(self):
        xsum=0
        for grade in self.grades:
            xsum += grade
        return xsum / float(len(self.grades))
    

# Δοκιμαστικές κλήσεις της κλάσης
chris = Student('1234','christopher robert',[12,11,14,15,10,16,17,18])
chris.printStudent()
chris.updateStudent('4321','Christofer Robert\'s',[12,11,14,15,20,16,17,18])
chris.printStudent()
avg = chris.calcAverage()
print 'Μέσος όρος βαθμολογίας για %s είναι %.2f ' % (chris.name, avg)



