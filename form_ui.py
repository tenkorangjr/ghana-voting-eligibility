from tkinter import *
import datetime as dt
from tkinter import messagebox


class MyUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Check for Voting Eligibility")
        self.window.config(padx=30, pady=50)

        # Inputs
        self.name_label = Label(text="Name: ")
        self.name_label.grid(column=0, row=0)
        self.name = Entry()
        self.name.focus()
        self.name.grid(column=1, row=0)

        self.year_label = Label(text="Year Of Birth: ")
        self.year_label.grid(column=0, row=1)
        self.year = Entry()
        self.year.grid(column=1, row=1)

        self.month_label = Label(text="Month: ")
        self.month_label.grid(column=0, row=2)
        self.month = Entry()
        self.month.grid(column=1, row=2)

        self.day_label = Label(text="Day: ")
        self.day_label.grid(column=0, row=3)
        self.day = Entry()
        self.day.grid(column=1, row=3)

        self.nationality_label = Label(text="Nationality: ")
        self.nationality_label.grid(column=0, row=4)
        self.countries = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Cambodia', 'Cameroon', 'Canada', 'Cabo Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territories', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe')
        self.nationality = Listbox(self.window, height=3)
        for item in self.countries:
            self.nationality.insert(self.countries.index(item), item)
        self.nationality.grid(column=1, row=4)

        self.check_button = Button(text="Check Eligibility", command=self.check_eligibility)
        self.check_button.grid(column=1, row=6, pady=10)

        self.window.mainloop()

    def check_eligibility(self):
        nationality = None
        month = None
        name = self.name.get()
        year = int(self.year.get())
        day = int(self.day.get())
        try:
            month = int(self.month.get())
        except ValueError:
            month_num_dict = {
                'January': 1,
                'February': 2,
                'March': 3,
                'April': 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September': 9,
                'October': 10,
                'November': 11,
                'December': 12,
            }
            try:
                month = month_num_dict[self.month.get().title()]
            except IndexError:
                messagebox.showwarning(message="Enter a valid month! Either number or text")
        this_year = dt.date.today().year
        try:
            nationality = self.nationality.get(self.nationality.curselection())
        except TclError:
            messagebox.showwarning(message="Select country!")
        if nationality != "Ghana":
            messagebox.showwarning(message=f"Unfortunately, {name.title()} is not eligible to vote.")
        else:
            if (this_year - year) > 18:
                messagebox.showinfo(message=f"{name.title()} is eligible to vote.")
            elif (this_year - year) == 18:
                if month > dt.date.today().month:
                    messagebox.showwarning(message=f"Unfortunately, {name.title()} is not eligible to vote.")
                elif month == dt.datetime.today().month:
                    if day > dt.date.today().day:
                        messagebox.showwarning(message=f"Unfortunately, {name.title()} is not eligible to vote.")
                    else:
                        messagebox.showinfo(message=f"{name.title()} is eligible to vote.")
                else:
                    messagebox.showinfo(message=f"{name.title()} is eligible to vote.")



