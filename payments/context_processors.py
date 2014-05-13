def test_user_paid(request):
	from payments.models import UserPlanData
	try:
		request.user
		upd = UserPlanData.objects.get(user_id=request.user.id)
	except:
		return {}
	else:
       	    	return {'paid' : upd.user_status}
