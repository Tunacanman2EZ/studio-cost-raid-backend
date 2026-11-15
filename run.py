from studio_cost_raid import create_app  # explanation - import the factory from your package

app = create_app()  # explanation - build the Flask app using the default "development" config

if __name__ == "__main__":  # explanation - only run this block when file is executed directly
    app.run(debug=True)     # explanation - start the dev server