figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()