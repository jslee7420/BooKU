from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from allbook.models import AllBook

def complete_sale(request,pk):
    book1 = AllBook.objects.get(pk =pk)
    book1.DEAL_FLAG = 0
    context = {'complete_book_info': book1}
    return render(request,'allbook/allbook_detail.html', context)


class AllBookCreate(CreateView):
    model = AllBook
    fields = ['title', 'state', 'price', 'lecture', 'text', 'image','kakaoUrl']
    template_name_suffix = '_create'
    success_url = '/allbook' #나중에 전공책url, 교양책url 구분

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/allbook')
        else:
            return self.render_to_response({'form': form})

class AllBookList(ListView):
    model = AllBook
    paginate_by = 5
    template_name_suffix = '_list'
    context_object_name = 'allbook_list'

    def get_queryset(self):
        book_list = AllBook.objects.order_by('-id')
        return book_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)
        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

class AllBookDetail(DetailView):
    model = AllBook
    template_name_suffix = '_detail'

class AllBookUpdate(UpdateView):
    model = AllBook
    context_object_name = 'update_book'
    fields = ['title', 'state', 'price','lecture',
              'text', 'image']
    template_name_suffix = '_update'
    success_url = '/allbook'

    def get_object(self):
        update_book = get_object_or_404(AllBook, pk=self.kwargs['pk'])
        return update_book

class AllBookDelete(DeleteView):
    model = AllBook
    template_name_suffix = '_delete'
    success_url = '/allbook'

def search(request):
    books = AllBook.objects.all().order_by('-id')
    template_name_suffix = '_search'
    q = request.POST.get('q', "")

    if q:
        books = books.filter(Q(title__icontains=q) or Q(text__icontains=q) or Q(author__icontains=q)).distinct() #검색조건
        return render(request, 'allbook/allbook_search.html', {'books': books, 'q': q})
    #필터 넣기 제목, 제목+작성자, 글내용
    else:
        return render(request, 'allbook/allbook_search.html')
