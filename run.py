import os                                 # explanation - lets us read FLASK_ENV from the environment
from studio_cost_raid import create_app  # explanation - import the factory from your package

# explanation - pick the config by FLASK_ENV ("development"/"testing"/"production"),
# instead of always using the "development" default - this is what makes FLASK_ENV
# actually do something once you set it on your host.
app = create_app(os.getenv("FLASK_ENV", "development"))

if __name__ == "__main__":  # explanation - only run this block when file is executed directly
    app.run(debug=True)     # explanation - start the LOCAL dev server only; gunicorn runs app directly in production