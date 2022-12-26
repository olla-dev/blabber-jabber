from random import sample
from django.core.management.base import BaseCommand
from faker import Faker
from django.db.models.signals import m2m_changed
from chat.models import Message, ChatRoom
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds the db with random data using faker'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        Faker.seed(0)
        User.objects.all().delete()
        ChatRoom.objects.all().delete()
        Message.objects.all().delete()

        nb_users = options['users']

        for nu in range(nb_users): 
            print(f"User {nu}:")
            user = User.objects.create_user(f"user{nu}", password='password')
            user.first_name = faker.first_name()
            user.last_name = faker.last_name()
            user.email = faker.email()
            user.is_superuser = False
            user.is_staff = False
            user.save()

        users = User.objects.values_list('pk', flat=True)
        
        m2m_changed.receivers = []
        room = ChatRoom()
        room.name = f"General"
        room.description = faker.paragraph(nb_sentences=5)
        room.save()

        random_room_users_id_list = sample(sorted(users), min(len(users), 10))
        random_room_users = User.objects.filter(id__in=random_room_users_id_list) 
        
        for u in random_room_users:
            room.users.add(u)

        room = ChatRoom()
        room.name = f"Random"
        room.description = faker.paragraph(nb_sentences=5)
        room.save()

        random_room_users_id_list = sample(sorted(users), min(len(users), 10))
        random_room_users = User.objects.filter(id__in=random_room_users_id_list) 

        for u in random_room_users:
            room.users.add(u)

        self.stdout.write(f"DB Seed done. Messages in DB: {Message.objects.count()}")