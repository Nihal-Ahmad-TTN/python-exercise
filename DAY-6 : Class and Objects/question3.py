class Database:
    instance = 0
    def __new__(cls, *args, **kwargs):

        # limiting the class to create only one instance
        if cls.instance==0:
            cls.instance = super().__new__(cls)
        return cls.instance

#making 3 objects of the class
db1 = Database()
db2 = Database()
db3 = Database()

#checking if the instances are same or not
print(db3 is db1)
print(db2 is db1)