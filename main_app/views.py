from django.shortcuts import render

finches = [
    {'type': 'House finch', 'color': 'Rosey', 'info': 'The house finch is a bird in the finch family Fringillidae. It is native to western North America and has been introduced to the eastern half of the continent and Hawaii.'},
    {'type': 'Purple Finch', 'color': 'Purple','info': 'This species and the other "American rosefinches" were formerly included with the rosefinches of Eurasia in the genus Carpodacus; however, the three North American species are not closely related to the rosefinches of the Old World, and have thus been moved to the genus Haemorhous by most taxonomic authorities.'},
    {'type': 'Crossbill', 'color': 'Red','info': 'Crossbills are birds of the genus Loxia within the finch family, with six species. These birds are characterized by the mandibles with crossed tips, which gives the group its English name.'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})