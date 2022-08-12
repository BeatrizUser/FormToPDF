

django.jQuery(function(){
    django.jQuery('.mask-cpf').unmask();
    var tamanho = django.jQuery('.mask-cpf').val().length;

    if(tamanho == 11){
        django.jQuery('.mask-cpf').mask('999.999.99-99');
    } else if(tamanho == 14){
        django.jQuery('.mask-cpf').mask('99.999.999/9999-99');
    }                   
});