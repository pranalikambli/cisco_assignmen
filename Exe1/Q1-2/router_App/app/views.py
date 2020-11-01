from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages

from .models import RouterInfo
from .forms import RouterForm


# Create your views here.


def index(request):
    return render(request, 'app/index.html')


class RouterInfoList(ListView):
    template_name = 'app/list_view.html'

    def get(self, request, *args, **kwargs):
        """
        Return the list of all the active roles data.
        """

        sapid = self.request.GET.get('sapid', '')
        hostname = self.request.GET.get('hostname', '')
        loopback = self.request.GET.get('loopback', '')
        mac_address = self.request.GET.get('mac_address', '')
        

        if sapid:
            queryset = RouterInfo.objects.filter(is_active=True, sapid__icontains=sapid).all()
        elif hostname:
            queryset = RouterInfo.objects.filter(is_active=True, hostname__icontains=hostname).all()
        elif mac_address:
            queryset = RouterInfo.objects.filter(is_active=True, mac_address__icontains=mac_address).all()
        elif loopback:
            queryset = RouterInfo.objects.filter(is_active=True, loopback__icontains=loopback).all()
       
        else:
            queryset = RouterInfo.objects.filter(is_active=True).all()


        paginator = Paginator(queryset, 5)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            role_list = paginator.page(page)
        except PageNotAnInteger:
            role_list = paginator.page(1)
        except EmptyPage:
            role_list = paginator.page(paginator.num_pages)

        # Get the index of the current page
        index = role_list.number - 1

        # This value is maximum index of pages, so the last page - 1
        max_index = len(paginator.page_range)

        # range of 7, calculate where to slice the list
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 4 if index <= max_index - 4 else max_index

        # new page range
        page_range = paginator.page_range[start_index:end_index]

        # showing first and last links in pagination
        if index >= 4:
            start_index = 1
        if end_index - index >= 4 and end_index != max_index:
            end_index = max_index
        else:
            end_index = None

        return render(request, self.template_name,
                      {'record_list': role_list, 'page_range': page_range, 'start_index': start_index,
                       'end_index': end_index, 'max_index': max_index})



class RouterAdd(View):
    """
        This class will covers the create view of router information.
    """
    form_class = RouterForm
    template_name = 'app/add_view.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        context['form'] = form
        router_info = RouterInfo.objects.all()
        context['router_info'] = router_info
        if request.POST:
            if form.is_valid():
                router_info = RouterInfo(sapid=request.POST['sapid'], hostname=request.POST['hostname'],
                                         loopback=request.POST['loopback'], mac_address=request.POST['mac_address'])
                router_info.save()
                messages.add_message(request, messages.SUCCESS, 'Data Added Successfully!')
                return redirect('/')
            return render(request, "app/index.html", context)


class EmployeeDelete(View):
    """
        This class will covers the delete view of Router.
    """

    def get(self, request, pk):
        """
        This method will deactivate the passed router_id.
        :param request:
        :param pk: Instance pk
        :return: Return status as 200 if is_activate gets update successfully as False else it will
                return status as 400 if there is any
        """
        inactive_router = RouterInfo.objects.filter(id=pk).update(is_active=False)
        data = {}
        if inactive_router:
            data['message'] = 1
        else:
            data['message'] = 0

        return JsonResponse(data)


class RouterInfoUpdate(View):
    """
        This class will covers the update view of router info.
    """
    form_class = RouterForm
    template_name = 'app/edit.html'

    def get(self, request, pk):
        """
        Get router data by primary key.
        :param request:
        :param pk:
        :return: Return status as 200 if form is valid else it will return status as 400 if data is invalid.
        """
        router_data = RouterInfo.objects.get(pk=pk, is_active=True)
        if router_data:
            return render(request, self.template_name, {'router_info': router_data}, status=200)
        return render(request, self.template_name, status=400)

    def post(self, request, pk):
        """
        Update new router info instance.
        :param request:
        :param pk:
        :return: Return status as 200 if form is valid else it will return status as 400 if data is invalid.
        """
        form = self.form_class(request.POST)

        if form.is_valid():
            RouterInfo.objects.filter(id=pk).update(sapid=request.POST['sapid'], hostname=request.POST['hostname'],
                                     loopback=request.POST['loopback'], mac_address=request.POST['mac_address'])
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!')
            return redirect('/')
        return render(request, self.template_name, {'form':form, 'router_info': form.data, 'ValidationError': form}, status=400)