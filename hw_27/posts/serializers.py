from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(source='get_name')

    # def get_name(self, obj):
    #     return obj.author.username

    class Meta:
        model = Post
        fields = ('id','title', 'post_body', 'post_cat', 'author', 'pub_date', 'edit_date')

class PostPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'post_body', 'post_cat',)