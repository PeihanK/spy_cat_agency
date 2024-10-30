from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cat, Mission, Target
from .serializers import CatSerializer, MissionSerializer, TargetSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request):
	return Response({
		'cats': request.build_absolute_uri('/api/cats/'),
		'missions': request.build_absolute_uri('/api/missions/'),
		'targets': request.build_absolute_uri('/api/targets/'),
	})


class CatViewSet(viewsets.ModelViewSet):
	queryset = Cat.objects.all()
	serializer_class = CatSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class MissionViewSet(viewsets.ModelViewSet):
	queryset = Mission.objects.all()
	serializer_class = MissionSerializer

	def create(self, request, *args, **kwargs):
		cat_id = request.data.get('cat')
		if Mission.objects.filter(cat_id=cat_id, is_completed=False).exists():
			return Response({"error": "This cat is already on a mission."}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class TargetViewSet(viewsets.ModelViewSet):
	queryset = Target.objects.all()
	serializer_class = TargetSerializer

	def complete(self, request, mission_id, target_id):
		target = self.get_object()
		target.is_completed = True
		target.save()

		if all(t.is_completed for t in target.mission.targets.all()):
			target.mission.is_completed = True
			target.mission.save()

		return Response(status=status.HTTP_204_NO_CONTENT)

	def update_notes(self, request, mission_id, target_id):
		target = self.get_object()
		if target.is_completed:
			return Response({"error": "Cannot update notes for a completed target."},
							status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(target, data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)
