$(document).ready(
    function(){
        $('.btn-friends').click(
            function(){
                friend_id = $(this).parent().parent().find('#friend-id').value;

                $.get(
                    "{% url 'ajax:add_friends' %}",
                    
                    {'friend_id' : friend_id,
                            'user_id':user_id},
                            function(data){
                                $(this).html('test');
                            });
                console.log('added');

            });

        $('.btn-not-friends').click(
            function(){
                console.log('removed');
                friend_id = $(this).attr("friendid");
                user_id = $(this).attr("userid");

                $.get(
                    "{% url 'ajax:remove_friends' %}",
                    {'friend_id' : friend_id,
                    'user_id':user_id},
                    function(data){
                        $(this).html('test');
                    });


            });
        });
