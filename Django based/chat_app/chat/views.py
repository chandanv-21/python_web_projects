from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')
def room(request,roomName):
    username=request.GET.get('username')
    room_details=Room.objects.get(roomName=roomName)
    return render(request, 'room.html', {'roomName':room_details,'username':username})

def checkview(request):
    roomName=request.POST['roomName']
    username=request.POST['username']
    if Room.objects.filter(roomName=roomName).exists():
        return redirect('/'+roomName+'/?username='+username)
    else:
        new_room=Room.objects.create(roomName=roomName)
        new_room.save()
        return redirect('/'+roomName+'/?username='+username)
    
def send(request):
    username=request.POST['username']
    room_id=request.POST['room_id']
    message=request.POST['message']
    new_message=Message.objects.create(msg=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse("Message sent successfully")


def getMessages(request, roomName):
    room_details=Room.objects.get(roomName=roomName)
    messages=Message.objects.filter(room=room_details.id)
    # print(messages)
    return JsonResponse({'messages':list(messages.values())})