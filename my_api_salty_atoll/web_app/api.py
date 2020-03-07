from flask import Blueprint, jsonify, request, render_template, current_app
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


my_routes = Blueprint("my_routes", __name__)
# filename = 'static/sm_baseline_model.pkl'
# loaded_model = joblib.load(open(filename, 'rb'))


@my_routes.route('/')
def home():
    return 'Welcome Home, Homie!'

@my_routes.route('/reco')
def reco():
    return render_template('reco.html')

# Don't forget to re-add the GET method when deploying to Heroku
@my_routes.route('/get_recommendation', methods=["GET"])
def get_recommendation():
    # For now: this will return details on a random strain from a local db
    if(request.method == 'GET'):
        ailment = request.args['ailment']
        relief = request.args['relief']
        booboo = ailment + relief
        description = """Thought to be an accidental cross when the DNL hermied, Sour Diesel (or East Coast Sour Diesel, as it's commonly called) is a special plant in the OG Kush/ChemDawg line of strains.  Its often "crushing" sativa effect actually seems to hit most people as more of an indica, increasing couchlock and being strong to the point of being overwhelming at times.  The plant itself is a fairly lanky one that tends to show lots of foxtailing when finished, practically stinking up the room with its pungent fuel-skunk-citrus bouquet."""
        lineage = "Unconfirmed, thought to be Original Diesel (ChemDawg '91 x [Massachusetts Super Skunk x Sensi Seeds Northern Lights] x DNL (Northern Lights/Shiva x Hawaiian)"
        story = """When Original Diesel was accidentally crossed with a DNL plant that hermied, it created seed stock that produced the East Coast Sour Diesel (ECSD) clone.  Many seed companies have released crosses with the strain, and some (like Reservoir Seeds) have attempted to reproduce the strain in seed form, releasing a variety of backcrosses and IBLs with varying results."""
        aroma = """Sour Diesel displays an extremely pungent blend of fuel, skunk, citrus, and spice that will leak through many jars and bags when the strain is well-grown.  The sharpness gets stronger after breaking it up, adding a stronger kick of citrus as well as a cutting fuel aroma that tickles the nose."""
        flavor = """A frontal attack of skunky citrus funk gives way to a mentholated lime-kissed spice which lingers in the mouth.  The smoke is expansive and will definitely cause coughing on larger hits."""
        qualities = """Sour Diesel is fairly sativa-dominant but seems to exhibit a headslam of an indica effect at times, especially if let go late into flowering.  It hits the eyes and head immediately, filling them with pressure and energy, while the body seems almost immobile at times, trending heavily towards couchlock — a numbing quality is also often reported, aiding with nerve and muscle pain relief.  Sour Diesel isn't known for being a long-laster at medicinal levels — it's a high peak and then a valley normally, often finishing with the user feeling lethargic and a bit drained after the sativa start.  Sour Diesel often helps with nerve issues, appetite, and can also help as a sleep aid during the "crash" portion of the effects."""
        grow_medium = """Sour Diesel doesn't yield quite as well as Original Diesel, growing a bit more spindly and with lighter buds, but the yield is still above-average.  Training and netting works very well for this strain, and it will take moderate to high amounts of feeding during flower, bulking up until the very end.  It stretches at least twice its initial height when flowered, more than that without training."""
        origin = """East Coast of the United States"""
        grow = """Clone only, though Reservoir Seeds, Cali Connection, and a few others have since "selfed" the ECSD clone to produce feminized seed stock"""
        strain_type = """Sativa-dominant hybrid"""
        flowering_time = """About 75 days, can go as long as 85 days for a less uppy experience — the fuel and funk seems to come out later in flower while the citrus elements are present early on."""

        return jsonify({"strain": "Sour Diesel",
                        "ailment": ailment,
                        "relief": relief,
                        'description': description,
                        'lineage': lineage,
                        'story': story,
                        'aroma': aroma,
                        'flavor': flavor,
                        'qualities': qualities,
                        'grow_medium': grow_medium,
                        'origin': origin,
                        'grow': grow,
                        'strain_type': strain_type,
                        'flowing_time': flowering_time})
        temp_booboo = "I want to be able to stand up and not fall down at the same time, while also being able to speak and swallow liquids. I don't want to get too high."
        # pred = loaded_model.predict(temp_booboo)


        # return str(pred)

    if(request.method == 'POST'):
        return 'OOPS! Sorry! This route is only used for GET requests.'
