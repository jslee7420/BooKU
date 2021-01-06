function changeMajorSelect(){
    var selectBox = document.getElementById("up_category_menu");
    var selectValue = selectBox.options[selectBox.selectedIndex].value;
    var selectText = selectBox.options[selectBox.selectedIndex].text;

    var all = "all"
    var major1 = "major1"
    var major2 = "major2"
    var major3 = "major3"

    if (selectValue == all){
        var url = '{% url 'book:index' %}';
        window.location.href = url;
    }else if(selectValue == major1){
        var url1 = '{% url 'book:major1' %}';
        window.location.href = url1;

    }else if(selectValue == major2){
        var url2 = '{% url 'book:major2' %}';
        window.location.href = url2;
    }else if(selectValue == major3){
        var url3 = '{% url 'book:major3' %}';
        window.location.href = url3;
    }
}