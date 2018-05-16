from innp_app.app import create_app

app = create_app('developments')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

    # import pywsgi
    #
    # server = pywsgi.WSGIServer(('', 5000), app)
    # server.serve_forever()
