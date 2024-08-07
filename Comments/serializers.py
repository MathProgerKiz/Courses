from rest_framework import serializers

from User.serializers import UserShortSerializer
from .models import CommentsModel


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    def get_fields(self):
        fields = super().get_fields()
        if self.context["request"].method == "GET":
            fields["author"] = UserShortSerializer(read_only=True)
        return fields

    class Meta:
        model = CommentsModel
        fields = '__all__'
