import {
  Module,
  VuexModule,
  MutationAction,
  Mutation,
  getModule,
} from 'vuex-module-decorators'
import { ChatRoom, Message, User, UserStatus } from '@/utils/types/index'
import { chatRoomApi } from '@/api/chat.service'
import store from './index'

@Module({ dynamic: true, store, name: 'chat-rooms' })
class ChatRoomModule extends VuexModule {
  rooms: ChatRoom[] = [];
  other_rooms: ChatRoom[] = [];
  selectedChatRoom: ChatRoom | undefined = undefined;
  joinChatRoom = '';
  leaveChatRoom = -1;
  userTyping: User = {} as User;

  /**
   * Returns a specific chat room by id
   */
  get chatRoom() {
    const rooms = this.rooms;
    return function (room_id: number) {
      return rooms.find(room => room.id === room_id);
    }
  }

  get getSelectedRoom(): ChatRoom | undefined {
    return this.selectedChatRoom;
  }

  @Mutation
  requestJoinRoom(room_name: string) {
    this.joinChatRoom = room_name;
  }

  @Mutation
  requestLeaveRoom(room_id: number) {
    this.leaveChatRoom = room_id;
  }

  @Mutation
  setSelectedRoom(room: ChatRoom | undefined) {
    if (room) {
      this.selectedChatRoom = this.rooms.find(r => r.id === room!.id);
      if (!this.selectedChatRoom) {
        this.rooms.push(room!);
        this.selectedChatRoom = room;
      }
    } else {
      this.selectedChatRoom = undefined
    }

    this.joinChatRoom = '';
    this.leaveChatRoom = -1;
  }

  @Mutation
  setUserTyping(user_id: number) {
    this.userTyping = this.selectedChatRoom?.users.find((u: User) => u.id === user_id) as User;
    setTimeout(() => {
        this.userTyping = {} as User;
    }, 3000);
  }


  @Mutation
  newMessage(message: Message) {
    const room = this.rooms.find(r => r.id == message.chat_room_id);
    if (room) {
      const messages = room!.messages;
      const old_message = messages.find(m => m.id == message.id)
      if(!old_message) {
        console.log('new message', room.id);
        room.messages =  [...messages, message];
        room.hasNewMessages = true;
      }
    }    
  }

  @Mutation
  roomNotification(updateEvent: any) {
    const room_id = updateEvent['room_id'];
    const message = updateEvent['message'];

    this.rooms.forEach(room => {
      if(room.id == room_id) {
        // this ugly, but i didn't find a way to use this aliases to call newMessage mutation
        const messages = room!.messages;
        const old_message = messages.find(m => m.id == message.id)
        if(!old_message) {
          console.log('new message', room.id);
          room.messages =  [...messages, message];
          room.hasNewMessages = true;
        }
        room.hasNewMessages = true;
      }
    })
    return this.rooms
  }
  
  @Mutation
  setSelectedRoomById(room_id: number) {    
    this.selectedChatRoom = this.rooms.find(r => r.id === room_id);    
    this.selectedChatRoom!.hasNewMessages = false;
    this.joinChatRoom = '';
    this.leaveChatRoom = -1;
  }

  @Mutation
  resetRooms() {
    this.rooms = [];
    this.other_rooms = [];
    this.joinChatRoom = '';
    this.leaveChatRoom = -1;
  }

  @MutationAction
  async fetchRooms() {
    const rooms = await chatRoomApi.fetchRooms();
    return { rooms }
  }

  @Mutation
  setUserStatus(userStatus: UserStatus) {    
    // update user status accross chat rooms
    // status = online: 1, offline: 0
    this.rooms.map(room => room.users.map(user => {
      if (user.id == userStatus.user_id) {
        user.profile.online = userStatus.status;
      }
    }))
  }
}

const chatRoomModule = getModule(ChatRoomModule)
export default chatRoomModule