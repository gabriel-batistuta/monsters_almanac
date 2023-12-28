from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Monster


#Class Based View
class MonsterListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Monster.objects.all()
    template_name = "monsters/list.html"
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(MonsterListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


#Function Based View
def monster_list_view(request):
    queryset = Monster.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "monsters/list.html", context)

#Class Based View
class MonsterDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Monster.objects.all()
    template_name = "monsters/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(MonsterDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

#Function Based View
def monster_detail_view(request, pk = None, *args, **kwargs):
    print(args)
    print(kwargs)
    # instance = Monster.objects.get(pk = pk) #get the object id
    instance = get_object_or_404(Monster, pk = pk)
    context = {
        'object': instance
    }
    return render(request, "monsters/detail.html", context)