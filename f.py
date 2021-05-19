OptionList = [
"COMPUTER",
"INFORMATION TECHNOLOGY",
"ELECTRONICS",
"EXTC"
] 


variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(roo1, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

app.mainloop()