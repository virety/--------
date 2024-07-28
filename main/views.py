from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Аленкафе-Главное'
        context['content'] = 'Интрига в каждой чашке'
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Аленкафе-О нас'
        context['content'] = 'О нас'
        context['heading'] = 'Аленкафе - ваш уютный уголок в мире кофе '
        context['text_on_page'] = 'Аленкафе - это место, где аромат свежесваренного кофе встречается с теплом домашней атмосферы.  Мы  бережно подбираем зерна, чтобы каждый глоток был наполнен яркими нотами и бодрящим вкусом. Наши бариста - настоящие мастера своего дела,  и с удовольствием помогут вам выбрать идеальный напиток, будь то классический эспрессо, ароматный латте или  нежный капучино.  Приходите к нам, чтобы насладиться вкусом кофе, поработать, встретиться с друзьями или просто отдохнуть от суеты. Аленкафе -  это больше, чем просто кофейня, это место, где вас всегда ждут с улыбкой и  уютным теплом. '
        return context