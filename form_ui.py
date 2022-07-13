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
        self.years = [str(year) for year in range(1990, dt.date.today().year + 1)]
        self.year_val = StringVar(self.window)
        self.year_val.set(self.years[-1])
        self.year = OptionMenu(self.window, self.year_val, *self.years)
        self.year.grid(column=1, row=1)

        self.month_label = Label(text="Month: ")
        self.month_label.grid(column=0, row=2)
        self.months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        self.month_variable = StringVar(self.window)
        self.month_variable.set(self.months[0])  # default value
        self.month = OptionMenu(self.window, self.month_variable, *self.months)
        self.month.grid(column=1, row=2)

        self.day_label = Label(text="Day: ")
        self.day_label.grid(column=0, row=3)
        number_of_days = 31
        self.days = [str(day) for day in range(1, number_of_days)]
        self.day_val = StringVar(self.window)
        self.day_val.set(self.days[0])
        self.day = OptionMenu(self.window, self.day_val, *self.days)
        self.day.grid(column=1, row=3)

        self.nationality_label = Label(text="Nationality: ")
        self.nationality_label.grid(column=0, row=4)
        self.countries = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Cambodia', 'Cameroon', 'Canada', 'Cabo Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territories', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe')
        self.variable = StringVar(self.window)
        self.variable.set(self.countries[0])  # default value
        self.nationality = OptionMenu(self.window, self.variable, *self.countries)
        self.nationality.grid(column=1, row=4)

        self.check_button = Button(text="Check Eligibility", command=self.check_eligibility)
        self.check_button.grid(column=1, row=6, pady=10)

        self.window.mainloop()

    def check_eligibility(self):
        nationality = None
        name = self.name.get()
        year = int(self.year_val.get())
        day = int(self.day_val.get())
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
        month = month_num_dict[self.month_variable.get().title()]
        this_year = dt.date.today().year
        try:
            nationality = self.variable.get()
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

            else:
                messagebox.showwarning(message=f"Unfortunately, {name.title()} is not eligible to vote.")
