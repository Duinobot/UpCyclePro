// when phonemodel is seletcted, display the color and storage base on model, using javascript to make it reponsive
django.jQuery(document).ready(function() {
    django.jQuery("#id_phonemodel").change(function() {
        var model = django.jQuery("#id_phonemodel").val();
        django.jQuery.ajax({
            url: "/admin/phones/getcolor/" + model,
            success: function(data) {
                django.jQuery("#id_color").html(data);
            }
        });
        django.jQuery.ajax({
            url: "/admin/phones/getstorage/" + model,
            success: function(data) {
                django.jQuery("#id_storage").html(data);
            }
        });
    });
});