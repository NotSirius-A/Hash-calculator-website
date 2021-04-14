from django.shortcuts import render

#from .models import HashFunction

from .forms import HashInputForm

from .utils import calculate_hashes

def calculator_page_view(request, *args, **kwargs):
    context = {}
    text_var_name = 'text'

    text_to_hash = request.GET.get(key=text_var_name)

    #returns an empty string when input is empty
    hashes_dict = calculate_hashes(string=text_to_hash)

    form = HashInputForm(request.GET or None)


    context = {
        'input_form': form,
        'hashes_dict': hashes_dict,
    }

    return render(request, 'hash_calculators/hash_body.html', context)
