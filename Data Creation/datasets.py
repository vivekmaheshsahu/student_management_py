import names
import pandas as pd
from random import choice


# Data created for analysis with help of code
def subject(s1, s2, s3, name_lst, counter):
    attended_s1 = choice([0, 1])
    attended_s2 = choice([0, 1])
    attended_s3 = choice([0, 1])
    Total_Lec = 3

    temp_dict = {'Enrolled_ID': int(counter)+1,
                 'Name': name_lst[int(counter)],
                 'Date': c_date.date(),
                 'Year': c_year,
                 'Branch': "DEMO",
                 'Total no.of Lec': Total_Lec,
                 'Lec_Attended_Percentage': round((((attended_s1 + attended_s2 + attended_s3) / Total_Lec) * 100), 2),
                 f'{s1}': attended_s1,
                 f'{s2}': attended_s2,
                 f'{s3}': attended_s3,}
    return temp_dict

# import names                                            # for unique names
# print([names.get_full_name() for x in range(60)])

lst = []
for c_date in pd.bdate_range(start='2/1/2021', end='6/2/2021'):
    for c_year in range(1, 5):
        if c_year == 1:
            first_year_name = ['Christopher Smith', 'Lou Nero', 'Vera Messina', 'Merna Dore', 'David Fairley', 'Pamela Franco', 'Randal Fenn', 'John Medeiros', 'Annie Locke', 'Matthew Sutton', 'Jeremy Davis', 'Scott Doucet', 'Horace Wessner', 'Deborah Santana', 'Kathy King', 'Rose Smiley', 'Daniel Kess', 'Troy Richard', 'Gabriel Mccullough', 'Shirley Mccarty', 'Peggy Garrard', 'Margaret Berens', 'Ronald Schafer', 'Willie Hutton', 'Bradley Todd', 'Alice Dean', 'Scott Glenn', 'Jennifer Kane', 'Carol Mckernan', 'Gregory Cornett', 'Clyde Sturgill', 'Amy White', 'Richard Purinton', 'Holly Nichols', 'Pamela Stone', 'Dave Riveron', 'Richard Chaney', 'Julie Hampton', 'Carol Tye', 'Dorothy Magana', 'Melissa Bercier', 'Jimmie Bowell', 'Sara Hutchison', 'Patrick Bynum', 'James Beltz', 'Dale Williams', 'Justin Choate', 'Rita Reed', 'Judith Aveado', 'Alejandro Cornell', 'Melissa Sparks', 'Elizabeth Phillips', 'Carl Bond', 'Arthur Cork', 'Sheila Hankins', 'Terri Johnson', 'Margret Barnhart', 'Earl Funderburg', 'Robert Phagan', 'Catherine Riggs']
            for counter in range(0, 60):
                temp_dict = subject('M1','CP','BEE',first_year_name,counter)
                lst.append(temp_dict)
        elif c_year == 2:
            second_year_name = ['Devon Munro', 'Matthew Vanderlip', 'Christopher Leclair', 'Joshua Ullman', 'Omar Lotti', 'William Whaley', 'Eleanor Marcum', 'Aaron Lafrance', 'Madelyn Love', 'Roberta Numbers', 'Cynthia Campos', 'Nancy Barajas', 'Dalton Jackson', 'Branden Brown', 'Dennis Deguire', 'Cynthia Gibbons', 'George Pisano', 'Hugo Campbell', 'Alvaro Smith', 'Joan Robinson', 'Pamela Simmons', 'Sean Savage', 'Ann Gray', 'Christopher Tafoya', 'Vicki Murphy', 'Chris Bostwick', 'Martha Delgado', 'William Dake', 'Brian Koral', 'Elizabeth Helbling', 'Estela Cannon', 'Mary Farmer', 'Perry Gallegos', 'Cora Ruggiero', 'Angela Macklin', 'Agnes Cancelliere', 'Gary Keeton', 'Myrtle Burleson', 'Norman Walden', 'Randall Bremer', 'Eric Hasas', 'Irene Anderson', 'Vernon Crumble', 'Rosemary Kitsmiller', 'Barbara Delfuente', 'Dominga Wright', 'Anthony Rivera', 'Donald Burke', 'Lorena White', 'Vincent Petrash', 'Ola Schreiber', 'Ruby Davila', 'Judith Shafer', 'Kareen Rutledge', 'Rex Taylor', 'Joel King', 'Trinidad Corcoran', 'Johnathon West', 'Robert Bradford', 'Jessica Stephens']
            for counter in range(0, 60):
                temp_dict = subject('VSLI','EV','Robotics',second_year_name,counter)
                lst.append(temp_dict)
        elif c_year == 3:
            third_year_name = ['Michael Malin', 'Susan Gladney', 'Louis Elmore', 'Ashley Beebe', 'Dana Krumm', 'Rhonda Martin', 'Mark Friend', 'Amanda Hill', 'Joey Sullivan', 'William Elias', 'Dorothy Fanno', 'Alfred Stone', 'Donald Moore', 'Robert Canon', 'Amy Daley', 'Barbara Phillips', 'Steven Kaiser', 'Claudette Kollar', 'Doris Alexander', 'Donna Buchanan', 'Larry Bush', 'Dawn Stigall', 'Susan Toland', 'Jared Cunningham', 'Ramon Runyan', 'Ramon Wood', 'Susan Matlock', 'Dustin Harrison', 'Irvin Roberts', 'Andre Allen', 'Edward Lundgren', 'Jon Walters', 'Linda Mccray', 'Ramona Hilbert', 'Elizabeth Leonard', 'Billy Yodis', 'Dora Wirtz', 'Mindy Policare', 'Meredith Brow', 'Timothy Lisa', 'Alberto Honeycutt', 'Eric Rico', 'Shannon Bahr', 'Gary Rodriguez', 'Jim Davis', 'George Culver', 'Matt Allen', 'Wade Heck', 'Sherry Harper', 'Richard Rogers', 'Joy Larson', 'Donald Wixon', 'Zachary Lasure', 'David Vaughan', 'Michael Beach', 'Leonel Herder', 'Darrell Hobson', 'Matt King', 'Rick Beery', 'Sam White']
            for counter in range(0, 60):
                temp_dict = subject('SAP','MBS','PLE',third_year_name,counter)
                lst.append(temp_dict)
        else:
            fourth_year_name = ['Byron Wheeler', 'William Middleton', 'Kelly Slate', 'David Ellis', 'Bill Koenig', 'Mary Thrill', 'Matthew Syphers', 'James Santiago', 'Sherry Walton', 'Ruben Nelson', 'Sarah Ewings', 'Jeannine Soldner', 'Nicholas Mcrae', 'Carter Locy', 'Mary Rodriguez', 'Pasquale Ferguson', 'Lacey James', 'Stephanie Riston', 'Amy Cheeks', 'Eddy Gibson', 'Violet Hoover', 'Teresa Cheung', 'Melanie Mahoney', 'Kenneth Williams', 'Dominique Mullen', 'Paula Earl', 'Quinton Lewin', 'Delores Moran', 'Jennifer Clevenger', 'Patricia Hart', 'Jessica Clark', 'Letha Hoffman', 'Grace Solian', 'David Redden', 'Jesus Wyatt', 'David Stewart', 'Susan Matthew', 'Brandon Kleist', 'Ricky Villarreal', 'John Gilliard', 'Van Welsh', 'Amy French', 'Rosemary Northrup', 'Adrienne Ashley', 'Julie Ervin', 'Duane Sims', 'Ann Damian', 'Jan Hansen', 'Anne Martin', 'Saundra Mccullough', 'Anna Swing', 'Eula Davis', 'Susan Medlar', 'Heather Finnell', 'Bethany Sindorf', 'Vivian Charles', 'Moses Smith', 'Elna Cowan', 'Teresa Huntington', 'Sandra Payne']
            for counter in range(0, 60):
                temp_dict = subject('ELE','FYP','MME',fourth_year_name,counter)
                lst.append(temp_dict)

df = pd.DataFrame(lst)                   # storing data in dataframe
# print(df)
df1 = df.to_csv('demo.csv', index=False)      # DF to CSV
print(df1)
