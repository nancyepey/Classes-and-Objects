class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name="Nancy", age=100, tracks=["fullstack", "mobile dev"], score=99.9):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = score
        print("Student name is ", self.name, "age of ", self.age, "my tracks are ", self.tracks, "with score of ", self.score)
    
    # methods
    def change_name(self, name):
        self.name = name
        print("Student changed name to ", self.name)
    
    def change_age(self, age):
        self.age = int(age)
        print("Student changed age to ", self.age)
    
    def add_track(self, track):
        tracks = self.tracks
        tracks.append(track)
        print("Student added track ", track, "and now final tracks are ", self.tracks)
        # return tracks
    
    def get_score(self):
        # self.score
        score = self.score
        print("Student score is ", score)
        return score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

# testing
# final_tracks = Bob.add_track("UI/UX")
# print(final_tracks)
get_score = Bob.get_score()
print(get_score)

Nancy = Student()
