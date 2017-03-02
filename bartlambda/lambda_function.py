"""
In this file we specify default event handlers which are then populated into the handler map using metaprogramming
"""

from ask import alexa
import mybart

def lambda_handler(request_obj, context={}):
    ''' All requests start here '''    
    return alexa.route_request(request_obj)

@alexa.default
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return alexa.create_response(message="Ask me Now")


@alexa.request("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to my Bart App. We can tell you 
                                         more information obout bart schedules")


@alexa.request(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!")

@alexa.intent('GetSchedule')
def get_posts_intent_handler(request):    
   
    def check_stattion(text):
        if text in mybart.stations:
           return text
        return 'null'
    srcst = request.slots("sourcest")
    check_station(srcst)
    destst = request.slots("destination")
    check_station(destst)
    myoutput = mybart.getSchedule(srcst,destst)

    return alexa.create_response(message='' .join(myoutput)
                                 end_session=True)
                                 

@alexa.intent('AMAZON.HelpIntent')
def help_intent_handler(request):
    st_list = [cat for cat in mybart.stations]
    message = ["You can ask for schedule in following stations - ",
               st_list]          
    return alexa.create_response(message=' '.join(message))

                                 
@alexa.intent('AMAZON.StopIntent')
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!")
