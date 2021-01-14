from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from book.models import Book
from .forms import BookForm

def update_deal(request,pk):
    book1 = Book.objects.get(pk =pk)
    if book1.deal_flag == 0:
        book1.deal_flag = 1
        book1.save()
    else:
        book1.deal_flag = 0
        book1.save()

    context = {'object': book1}
    return render(request,'book/book_detail.html', context)


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'text', 'image','lecture', 'state', 'price', 'kakaoUrl','major_category','writer']
    template_name_suffix = '_create'
    success_url = '/book'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/book')
        else:
            return self.render_to_response({'form': form})

class BookList(ListView):
    model = Book
    paginate_by = 5
    template_name_suffix = '_list'
    context_object_name = 'book_list'

    def get_queryset(self):
        book_list = Book.objects.order_by('-id')
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

def update_list(request):
    first_books = Book.objects.all().order_by('-id')
    old_list = request.GET.getlist('object_list', None)
    search_type = request.GET.getlist('search-type', None)

    if 'deal' not in search_type:
        if 'free' not in search_type:
            return render(request, 'book/book_list.html', {'object_list': first_books, 'search_type': search_type})
        elif 'free' in search_type:
            return render(request, 'book/book_list.html', {'object_list': first_books.filter(price = 0), 'search_type': search_type})

    elif 'deal' in search_type:
        if 'free' not in search_type:
            return render(request, 'book/book_list.html', {'object_list': first_books.filter(deal_flag = 1), 'search_type': search_type})
        elif 'free' in search_type:
            return render(request, 'book/book_list.html', {'object_list': first_books.filter(deal_flag = 1 , price = 0), 'search_type': search_type})

def get_first_major_list(request):
    book_list = Book.objects.all().filter(major_category=request.user.first_major)
    search_type = request.GET.getlist('search-type', None)

    if 'deal' not in search_type:
        if 'free' not in search_type:
            return render(request, 'book/book_major1_list.html', {'object_list': book_list, 'search_type': search_type})
        elif 'free' in search_type:
            return render(request, 'book/book_major1_list.html',
                          {'object_list': Book.objects.all().filter(major_category=request.user.first_major, price = 0), 'search_type': search_type})

    elif 'deal' in search_type:
        if 'free' not in search_type:
            return render(request, 'book/book_major1_list.html',
                          {'object_list': Book.objects.all().filter(major_category=request.user.first_major,deal_flag=1), 'search_type': search_type})
        elif 'free' in search_type:
            return render(request, 'book/book_major1_list.html',
                          {'object_list': Book.objects.all().filter(major_category=request.user.first_major,deal_flag=1, price = 0), 'search_type': search_type})


def get_second_major_list(request):
    if request.user.second_major != "":
        book_list = Book.objects.all().filter(major_category=request.user.second_major)
        search_type = request.GET.getlist('search-type', None)
        if 'deal' not in search_type:
            if 'free' not in search_type:
                return render(request, 'book/book_major2_list.html',
                              {'object_list': book_list, 'search_type': search_type})
            elif 'free' in search_type:
                return render(request, 'book/book_major2_list.html',
                              {'object_list': Book.objects.all().filter(major_category=request.user.second_major,
                                                                        price=0), 'search_type': search_type})

        elif 'deal' in search_type:
            if 'free' not in search_type:
                return render(request, 'book/book_major2_list.html',
                              {'object_list': Book.objects.all().filter(major_category=request.user.second_major,
                                                                        deal_flag=1), 'search_type': search_type})
            elif 'free' in search_type:
                return render(request, 'book/book_major2_list.html',
                              {'object_list': Book.objects.all().filter(major_category=request.user.second_major,
                                                                        deal_flag=1, price=0),
                               'search_type': search_type})


def get_third_major_list(request):
    if request.user.third_major != "":
        book_list = Book.objects.all().filter(major_category=request.user.third_major)
        search_type = request.GET.getlist('search-type', None)

        if 'deal' not in search_type:
            if 'free' not in search_type:
                return render(request, 'book/book_major3_list.html',
                              {'object_list': book_list, 'search_type': search_type})
            elif 'free' in search_type:
                return render(request, 'book/book_major3_list.html',
                              {'object_list': Book.objects.all().filter(major_category=request.user.third_major,
                                                                        price=0), 'search_type': search_type})

        elif 'deal' in search_type:
            if 'free' not in search_type:
                return render(request, 'book/book_major3_list.html',
                              {'object_list': Book.objects.all().filter(major_category=request.user.third_major,
                                                                        deal_flag=1), 'search_type': search_type})
            elif 'free' in search_type:
                return render(request, 'book/book_major3_list.html',
                              {'object_list': Book.objects.all().filter(major_category=request.user.third_major,
                                                                        deal_flag=1, price=0),
                               'search_type': search_type})


class BookDetail(DetailView):
    model = Book
    template_name_suffix = '_detail'

class BookUpdate(UpdateView):
    model = Book
    context_object_name = 'update_book'
    fields = ['title', 'writer', 'major_category','lecture','state','price','image','text','kakaoUrl']
    template_name_suffix = '_update'
    success_url = '/book'

    def get_object(self):
        update_book = get_object_or_404(Book, pk=self.kwargs['pk'])
        return update_book

class BookDelete(DeleteView):
    model = Book
    template_name_suffix = '_delete'
    success_url = '/book'


def search(request):
    books = Book.objects.all().order_by('-id')
    q = request.POST.get('q', "")

    if q:
        books = books.filter(
            Q(title__icontains=q) or Q(lecture__icontains=q) or Q(writer__icontains=q)).distinct()  # 검색조건

        return render(request, 'book/book_search.html', {'books': books, 'q': q})
    # 필터 넣기 제목, 제목+작성자, 글내용
    else:
        return render(request, 'book/book_search.html')


def filter(request):
    first_books = Book.objects.all().order_by('-id')
    old_list = request.GET.getlist('object_list',None)
    search_type= request.GET.getlist('search-type',None)
    search_q = None

    if 'free' in search_type:
        temp_q = Q(price = 0)
        search_q = search_q | temp_q if search_q else temp_q

    if 'include-deal-complete' in search_type:
        temp_q = Q(deal_flag = 1) | Q(deal_flag = 0)
        search_q = search_q | temp_q if search_q else temp_q

    elif 'include-deal-complete' not in search_type:
        temp_q = Q(deal_flag = 1)
        search_q = search_q | temp_q if search_q else temp_q

    book_list = first_books.filter(search_q).distinct()
    return render(request, 'book/book_list.html', {'object_list': book_list, 'search_type': search_type})

