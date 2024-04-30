import math
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RoomName, Tue

def loads(request):
    data = {}
    settings = {}
    currentPath = request.path

    settings['currentPath'] = currentPath

    dryRoomNames = RoomName.objects.filter(type=1).values_list('name', flat=True)
    wetRoomNames = RoomName.objects.filter(type=2).values_list('name', flat=True)

    roomNames = {
        'dryRoomNames': dryRoomNames, 
        'wetRoomNames': wetRoomNames
    }
    

    if request.method == 'GET':
        return render(request, 'loads.html', { 'data': data, 'roomNames': roomNames, 'settings': settings })
    
    if request.method == 'POST':
        data = getDataToUpdate(request)
        report = getReport(data)
        print(report)
        
        if 'addLineDryArea' in request.POST:
            data['dryAreas'].append({
                'room': '', 
                'length': '', 
                'width': '', 
                'area': '', 
                'perimeter': '', 
                'addLighting': '', 
                'lightingPower': '', 
                'addTug': '', 
                'quantity': '', 
                'power': ''
            })
        elif 'addLineWetArea' in request.POST:
            data['wetAreas'].append({
                'room': '', 
                'length': '', 
                'width': '', 
                'area': '', 
                'perimeter': '', 
                'addLighting': '', 
                'lightingPower': '', 
                'addTug': '', 
                'quantity': '', 
                'power': ''
            })
        elif 'addLineTue' in request.POST:
            data['tues']['tueLine'].append({'room': '', 'description': '', 'power': '' })
        else:
            print("Nenhum botão foi clicado!")

        if( len(data['tues']['roomNamesToTues']) >= 1 ):
            settings['hasArea'] = "true"

        return render(request, 'loads.html', { 'data': data, 'roomNames': roomNames, 'settings': settings, 'report': report })

def getDataToUpdate(request):
    roomNamesToTues = []

    dryAreas = []
    for i in range(len(request.POST.getlist('roomDryAreas'))):
        
        if ( request.POST.getlist('lengthDryAreas')[i] == "" or request.POST.getlist('widthDryAreas')[i] == ""):
            continue

        room = request.POST.getlist('roomDryAreas')[i]
        length = float(request.POST.getlist('lengthDryAreas')[i].replace(',', '.'))
        width = float(request.POST.getlist('widthDryAreas')[i].replace(',', '.'))
        area = round(length * width, 2)
        perimeter = 2 * (length + width)
        addLighting = int(request.POST.getlist('addLightingDryAreas')[i])
        lightingPower = getLightingPower(area, addLighting)
        addTug = int(request.POST.getlist('addTugDryAreas')[i])
        quantity = getQuantityDryAreas(perimeter, addTug)
        power = getPowerDryAreas(quantity)
        dryAreas.append({
            'room': room, 
            'length': length, 
            'width': width, 
            'area': area, 
            'perimeter': perimeter, 
            'addLighting': addLighting, 
            'lightingPower': lightingPower, 
            'addTug': addTug, 
            'quantity': quantity, 
            'power': power
        })
        roomNamesToTues.append(room)

    wetAreas = []
    for i in range(len(request.POST.getlist('roomWetAreas'))):
        
        if ( request.POST.getlist('lengthWetAreas')[i] == "" or request.POST.getlist('widthWetAreas')[i] == ""):
            continue

        room = request.POST.getlist('roomWetAreas')[i]
        length = float(request.POST.getlist('lengthWetAreas')[i].replace(',', '.'))
        width = float(request.POST.getlist('widthWetAreas')[i].replace(',', '.'))
        area = round(length * width, 2)
        perimeter = 2 * (length + width)
        addLighting = int(request.POST.getlist('addLightingWetAreas')[i])
        lightingPower = getLightingPower(area, addLighting)
        addTug = int(request.POST.getlist('addTugWetAreas')[i])
        quantity = getQuantityWetAreas(perimeter, addTug)
        power = getPowerWetAreas(quantity)
        wetAreas.append({
            'room': room, 
            'length': length, 
            'width': width, 
            'area': area, 
            'perimeter': perimeter, 
            'addLighting': addLighting, 
            'lightingPower': lightingPower, 
            'addTug': addTug, 
            'quantity': quantity, 
            'power': power
        })
        roomNamesToTues.append(room)

    tuesData= Tue.objects.all().values_list('name', 'power')

    tueLine = []
    
    for i in range(len(request.POST.getlist('roomNameTue'))):
        roomNameTue = request.POST.getlist('roomNameTue')[i]
        description = request.POST.getlist('descriptionTue')[i]
        power = Tue.objects.get(name = description).power
        tueLine.append({
            'roomNameTue': roomNameTue,
            'description': description,
            'power': power
        })

    tues = { 
        'tueLine': tueLine , 
        'tuesData': tuesData, 
        'roomNamesToTues': roomNamesToTues
    }

    data = { 
        'dryAreas': dryAreas, 
        'wetAreas': wetAreas, 
        'tues': tues 
    }

    return data

def getReport(data):

    lightingPowerDryArea = sum(room['lightingPower'] for room in data['dryAreas'])
    lightingPowerWetArea = sum(room['lightingPower'] for room in data['wetAreas'])
    tugPowerDryArea = sum(room['power'] for room in data['dryAreas'])
    tugPowerWetArea = sum(room['power'] for room in data['wetAreas'])
    lightingPower = lightingPowerDryArea + lightingPowerWetArea
    tugPower = tugPowerDryArea + tugPowerWetArea
    tuePower = sum(room['power'] for room in data['tues']['tueLine'])

    return {'lightingPower': lightingPower, 'tugPower': tugPower, 'tuePower': tuePower}

def getLightingPower(area, addLighting):
    if (area <= 6):
        return  addLighting + 100
    return addLighting + 100 + (int((area - 6)/4)*60)


def getQuantityDryAreas(perimeter, addTug):
    return addTug + math.ceil(perimeter/5)
    
def getQuantityWetAreas(perimeter, addTug):
    return addTug + math.ceil(perimeter/3.5)

def getPowerDryAreas(quantity):
    return quantity * 100
    
def getPowerWetAreas(quantity):
    if (quantity <= 3):
        return quantity * 600
    elif (quantity <= 6):
        return 1800 + (quantity - 3) * 100
    return 1200 + (quantity - 2) * 100
      
class CombinedArrays:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2