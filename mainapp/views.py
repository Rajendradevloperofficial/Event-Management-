from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Event, Alert
from .serializers import EventSerializer, AlertSerializer
from .permissions import IsAdmin


class EventCreateAPIView(generics.CreateAPIView):
    """
    Ingest security events
    Admin only
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdmin]

    def perform_create(self, serializer):
        event = serializer.save()

        if event.severity in ['High', 'Critical']:
            Alert.objects.create(event=event)


class AlertListAPIView(generics.ListAPIView):
    """
    List alerts
    Admin & Analyst (read-only)
    Supports filtering by severity & status
    """
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Alert.objects.select_related('event')

        severity = self.request.query_params.get('severity')
        status = self.request.query_params.get('status')

        if severity:
            qs = qs.filter(event__severity=severity)

        if status:
            qs = qs.filter(status=status)

        return qs


class AlertUpdateAPIView(generics.UpdateAPIView):
    """
    Update alert status
    Admin only
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAdmin]
    http_method_names = ['patch', 'put']
