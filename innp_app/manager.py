from innp_app.innp_app.app import create_apps

app = create_apps()

if __name__ == '__main__':
    app.run(debug=True)