from website import create_app

app = create_app()
#Keeps the program running
if __name__ == '__main__':
    app.run(debug=True)