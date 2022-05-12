import tkinter as tk

window = tk.Tk()

# input_source_path = '/Desktop/Result_7.csv'
# input_schema_name = 'pokemon'
# input_table_name = 'Result_7'


# Database Credentials Section
frame_database_credentials = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)

label_database_section = tk.Label(master=frame_database_credentials, text='Database Credentials')
label_database_section.pack()

frame_hostname = tk.Frame(master=frame_database_credentials)
frame_database = tk.Frame(master=frame_database_credentials)
frame_username = tk.Frame(master=frame_database_credentials)
frame_password = tk.Frame(master=frame_database_credentials)

label_hostname = tk.Label(master=frame_hostname, text='Host Name:')
label_database = tk.Label(master=frame_database, text='Database Name:')
label_username = tk.Label(master=frame_username, text='Username:')
label_password = tk.Label(master=frame_password, text='Password:')

label_hostname.pack(side=tk.LEFT)
label_database.pack(side=tk.LEFT)
label_username.pack(side=tk.LEFT)
label_password.pack(side=tk.LEFT)

entry_hostname = tk.Entry(master=frame_hostname)
entry_database = tk.Entry(master=frame_database)
entry_username = tk.Entry(master=frame_username)
entry_password = tk.Entry(show="*", master=frame_password)

entry_hostname.pack(side=tk.LEFT)
entry_database.pack(side=tk.LEFT)
entry_username.pack(side=tk.LEFT)
entry_password.pack(side=tk.LEFT)

frame_hostname.pack()
frame_database.pack()
frame_username.pack()
frame_password.pack()

frame_database_credentials.pack()

# frame destination
frame_destinations = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
label_destination = tk.Label(master=frame_destinations, text='Destinations')

label_destination.pack()

# input_source_path = '/Desktop/Result_7.csv'
# input_schema_name = 'pokemon'
# input_table_name = 'Result_7'

frame_source_path = tk.Frame(master=frame_destinations)
frame_schema_name = tk.Frame(master=frame_destinations)
frame_table_name = tk.Frame(master=frame_destinations)

frame_source_path.pack()
frame_schema_name.pack()
frame_table_name.pack()

label_source_path = tk.Label(master=frame_source_path ,text='CSV File Location: ')
label_schema_name = tk.Label(master=frame_schema_name, text='Destination Schema Name: ')
label_table_name = tk.Label(master=frame_table_name, text='Destination Table Name: ')

label_source_path.pack(side=tk.LEFT)
label_schema_name.pack(side=tk.LEFT)
label_table_name.pack(side=tk.LEFT)

frame_destinations.pack()

window.mainloop()