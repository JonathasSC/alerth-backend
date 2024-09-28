import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from ..api.models import Event


class EventsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('events', self.channel_name)
        await self.accept()
        await self.send_events()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('events', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        lat = text_data_json.get('lat')
        lng = text_data_json.get('lng')
        category = text_data_json.get('category')  # Receber categoria
        urgency = text_data_json.get('urgency')    # Receber urgência

        if lat is not None and lng is not None and category is not None and urgency is not None:
            # Salvar o evento no banco de dados
            await self.save_event(lat, lng, category, urgency)

            # Enviar as coordenadas para o grupo
            await self.channel_layer.group_send(
                'events',
                {
                    'type': 'send_coordinates',
                    'lat': lat,
                    'lng': lng,
                    'category': category,   # Enviar categoria
                    'urgency': urgency       # Enviar urgência
                }
            )

    async def send_coordinates(self, event):
        lat = float(event.get('lat'))
        lng = float(event.get('lng'))
        category = event.get('category')
        urgency = event.get('urgency')

        await self.send(text_data=json.dumps({
            'lat': lat,
            'lng': lng,
            'category': category,     # Incluir categoria na mensagem
            'urgency': urgency        # Incluir urgência na mensagem
        }))

    async def send_events(self):
        events = await self.fetch_all_events()
        await self.send(text_data=json.dumps({
            'events': events
        }))

    @sync_to_async
    def fetch_all_events(self):
        events = Event.objects.values('lat', 'lng', 'category', 'urgency')
        return [
            {
                'lat': float(event['lat']),
                'lng': float(event['lng']),
                'category': event['category'],
                'urgency': event['urgency']
            }
            for event in events
        ]

    @sync_to_async
    def save_event(self, lat, lng, category, urgency, exp_acquired=0, reports_number=0):
        event = Event(lat=lat, lng=lng, category=category, urgency=urgency,
                      exp_acquired=exp_acquired, reports_number=reports_number)
        event.save()
