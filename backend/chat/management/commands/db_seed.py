from random import choice, sample
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from datetime import datetime
from faker import Faker
from chat.models import Message, ChatRoom
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds the db with random data using faker'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10)
        parser.add_argument('--rooms', type=int, default=1000)
        parser.add_argument('--messages-per-room', type=int, default=150000)

    def handle(self, *args, **options):
        faker = Faker()
        Faker.seed(0)
        User.objects.all().delete()
        ChatRoom.objects.all().delete()
        Message.objects.all().delete()

        nb_users = options['users']
        nb_rooms = options['rooms']
        messages_per_room = options['messages_per_room']

        for nu in range(nb_users): 
            print(f"User {nu}:")
            profile = faker.profile()
            user = User.objects.create_user(profile['username'], password='password')
            user.first_name = faker.first_name()
            user.last_name = faker.last_name()
            user.email = faker.email()
            user.is_superuser = False
            user.is_staff = False
            user.save()

        users = User.objects.values_list('pk', flat=True)

        for nr in range(nb_rooms):
            print(f"ChatRoom {nr}:")
            room = ChatRoom()
            room.name = f"room - {nr}"
            room.description = faker.paragraph(nb_sentences=5)
            room.save()

            random_room_users_id_list = sample(sorted(users), min(len(users), 10))
            random_room_users = User.objects.filter(id__in=random_room_users_id_list) 
            
            for u in random_room_users:
                room.users.add(u)
            
            for nm in range(messages_per_room):
                message = Message()
                message.content = faker.text()
                message.author_id = choice(random_room_users).id
                message.room_id = room.id
                message.status = Message.MessageStatus.SENT
                message.sent_time_utc = datetime.utcnow()
                message.save()

        self.stdout.write(f"DB Seed done. Messages in DB: {Message.objects.count()}")