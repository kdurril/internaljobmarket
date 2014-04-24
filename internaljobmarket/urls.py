# URLs
import internaljobmarket.views 

app.add_url_rule('/students/', view_func=Student.as_view('students'))
app.add_url_rule('/supervisors/', view_func=Supervisors.as_view('supervisors'))
#Move to urls
app.add_url_rule('/positions/', view_func=Positions.as_view('positions'))
#this view must be restricted to the positon owner/supervisor
app.add_url_rule('/positions/<int:position_id>', view_func=position_view,
                 methods=['GET', 'PUT', 'DELETE'])
#For review of applications for individual
app.add_url_rule('/application/', view_func=Application.as_view('application'))
#OFFER
app.add_url_rule('/offer/', view_func=Offer.as_view('offer'))
app.add_url_rule('/offer/<int:offer_id>', view_func=offer_view,
                 methods=['GET', 'PUT', 'DELETE'])