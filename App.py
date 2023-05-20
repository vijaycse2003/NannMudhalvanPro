from flask import Flask, \
    render_template as render,\
        redirect,url_for as url,request,flash



app=Flask(__name__)
app.secret_key="vijay2003"


@app.route('/')
def Home():
    return render("Home.html")

@app.route('/predict',methods=['GET','POST'])
def Prediction():
    if request.method == 'POST':
        Gender=request.form['Gender']
        if Gender == 'Female':
            Gender=0
        if Gender == 'Male':
            Gender=1
        
        Age=request.form['Age']
        Type_of_Travel=request.form['ttravel']
        if Type_of_Travel == 'Bussiness Travel':
            Type_of_Travel=0
        if Type_of_Travel == 'Personal Travel':
            Type_of_Travel=1
        Class=request.form['ttravel']
        if Class == 'Business':
            Class=0
        if Class == 'Eco':
            Class=1
        if Class == 'Eco Plus':
            Class=2

        Flight_Distance=request.form['flight_distance']
        Inflight_wifi_service=request.form['iws']
        Departure_ArrivalTime=request.form['dadtc']
        Ease_of_OnlineBooking=request.form['eob']
        Gate_location=request.form['gl']
        Food_and_Drink=request.form['fd']
        Online_Boarding=request.form['ob']
        Seat_comfort=request.form['sc']
        Infight_entertainment=request.form['ie']
        On_board_service=request.form['obs']
        Leg_room_services=request.form['lrs']
        Baggage_handling=request.form['bh']
        Checkin_service=request.form['cs']
        Inflight_service=request.form['is']
        Cleanliness=request.form['cl']
        Departure_Delay_in_minutes=request.form['ddm']
        Arrival_Delay_in_minutes=request.form['adm']


        total=[[Gender,Age,Type_of_Travel,Class,Flight_Distance,Inflight_wifi_service,Departure_ArrivalTime,Ease_of_OnlineBooking,Gate_location,Food_and_Drink,Online_Boarding,Seat_comfort,Infight_entertainment,On_board_service,Leg_room_services,Baggage_handling,Checkin_service,Inflight_service,Cleanliness,Departure_Delay_in_minutes,Arrival_Delay_in_minutes]]

        payload_scoring={"input_data":[{'field':[
            'Gender','Age,Type_of_Travel','Class','Flight_Distance','Inflight_wifi_service','Departure_ArrivalTime','Ease_of_OnlineBooking','Gate_location','Food_and_Drink','Online_Boarding','Seat_comfort','Infight_entertainment','On_board_service','Leg_room_services','Baggage_handling','Checkin_service','Inflight_service','Cleanliness','Departure_Delay_in_minutes','Arrival_Delay_in_minutes'
        ]}]}

       # response_scoring=requests.post('https://us-south.ml.cloud.ibm.com/ml/v4',headers={'Authorization':'Bearer'+mltoken})
       #prediction=response_scoring.json()
        # print(prediction)
        # pred=prediction['prdeictions'][0]['values'][0][0]
        pred=int(Baggage_handling)+int(Seat_comfort)+int(Cleanliness)+int(Food_and_Drink)

       
        if (int(pred) % 10 == 0) & int(Baggage_handling) >45 & int(Food_and_Drink)>45  | int(Seat_comfort)>45 & int(Cleanliness)>45 :
            pred="Passanger have Satisfaction the Airline Service"
        else:
            pred="Passangers have neutral or dissatisfied the Airline Service"
        
        return render('Submit.html',pred={pred})
        
    return render("Predict.html")


@app.route('/submit')
def Submit():
    return render('Submit.html')






if __name__ == "__main__":
    app.run(debug=True)