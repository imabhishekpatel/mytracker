# views.py

from django.shortcuts import render,redirect
from checkInCheckOut.forms.checkInOutForm import *
from checkInCheckOut.models.Attendance import *
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def check_in_out(request):
    user = request.user
    attendance = Attendance.objects.filter(user=user,check_in_time__date=datetime.now().date()).last()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action:
            if action == 'check_in':
                Attendance.objects.create(user=user, check_in_time=datetime.now())
            elif action == 'check_out':
                if attendance and not attendance.check_out_time:
                    attendance.check_out_time = datetime.now()
                    attendance.save()

            # After handling the form submission, redirect to prevent form resubmission
            return redirect('check_in_out')

    return render(request, 'checkInCheckOut/checkin_checkout.html', {'attendance': attendance})

# @login_required
# def check_in_out(request):
#     user = request.user
#     attendance = Attendance.objects.filter(user=user).last()

#     if request.method == 'POST':
#         action = request.POST.get('action')
#         if action == 'check_in':
#             Attendance.objects.create(user=user, check_in_time=datetime.now())
#         elif action == 'check_out':
#             if attendance and not attendance.check_out_time:
#                 attendance.check_out_time = datetime.now()
#                 attendance.save()

#     return render(request, 'checkInCheckOut/checkin_checkout.html', {'attendance': attendance})

# @login_required
# def check_in_out(request):
#     form = CheckInOutForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             action = form.cleaned_data['action']
#             user = request.user
#             if action == 'check_in':
#                 Attendance.objects.create(user=user, check_in_time=datetime.now())
#             elif action == 'check_out':
#                 attendance = Attendance.objects.filter(user=user).last()
#                 if attendance and not attendance.check_out_time:
#                     attendance.check_out_time = datetime.now()
#                     attendance.save()
#     return render(request, 'checkInCheckOut/checkin_checkout.html', {'form': form})
