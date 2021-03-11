from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from book.models import Book
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


def bookList(request):
    """
    도서 목록출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    mc = request.GET.get('major_category', '전체')  # 전공 카테고리
    on_deal_only = request.GET.get('on_deal_only', '0')  # 거래중인 도서만 선택
    is_free = request.GET.get('is_free', '0')  # 무료나눔 도서만 선택

    # 조회
    book_list = Book.objects.order_by('-created')
    if mc != '전체':
        book_list = book_list.filter(major_category=mc)
    if on_deal_only == '1':
        book_list = book_list.filter(deal_flag=1)
    if is_free == '1':
        book_list = book_list.filter(price=0)
    if kw:
        book_list = book_list.filter(Q(title__icontains=kw) or Q(
            lecture__icontains=kw) or Q(writer__icontains=kw)).distinct()

    # 페이징처리
    paginator = Paginator(book_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'object_list': page_obj, 'page': page,
               'kw': kw, 'mc': mc, 'on_deal_only': on_deal_only, 'is_free': is_free}
    return render(request, 'book/book_list.html', context)


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'text', 'image', 'lecture', 'state',
              'price', 'kakaoUrl', 'major_category', 'writer']
    template_name_suffix = '_form'
    success_url = '/book'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/book')
        else:
            return self.render_to_response({'form': form})


class BookDetail(DetailView, LoginRequiredMixin):
    login_url = 'user:login'
    redirect_field_name = 'redirect_to'
    model = Book
    template_name_suffix = '_detail'


class BookUpdate(UpdateView):
    model = Book
    context_object_name = 'form'
    fields = ['title', 'writer', 'major_category', 'lecture',
              'state', 'price', 'image', 'text', 'kakaoUrl']
    template_name_suffix = '_form'
    success_url = '/book'

    def get_object(self):
        form = get_object_or_404(Book, pk=self.kwargs['pk'])
        return form


class BookDelete(DeleteView):
    model = Book
    success_url = '/book'


@login_required(login_url='user:login')
def update_deal(request, pk):
    book1 = Book.objects.get(pk=pk)
    if book1.deal_flag == 0:
        book1.deal_flag = 1
        book1.save()
    else:
        book1.deal_flag = 0
        book1.save()

    context = {'object': book1}
    return render(request, 'book/book_detail.html', context)
