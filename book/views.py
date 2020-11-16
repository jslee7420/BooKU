from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from book.models import Book


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'category', 'state', 'price', 'lecture', 'text', 'image']
    template_name_suffix = '_create'
    success_url = '/book' #나중에 전공책url, 교양책url 구분

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

class BookDetail(DetailView):
    model = Book
    template_name_suffix = '_detail'

class BookUpdate(UpdateView):
    model = Book
    context_object_name = 'update_book'
    fields = ['title', 'category', 'state', 'price','lecture',
              'text', 'image']
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
    template_name_suffix = '_search'
    q = request.POST.get('q', "")

    if q:
        books = books.filter(Q(title__icontains=q) or Q(text__icontains=q) or Q(author__icontains=q)).distinct() #검색조건
        return render(request, 'book/book_search.html', {'books': books, 'q': q})
    #필터 넣기 제목, 제목+작성자, 글내용
    else:
        return render(request, 'book/book_search.html')
