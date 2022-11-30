import {
  Module,
  VuexModule,
  MutationAction,
  Mutation,
  getModule,
  Action
} from 'vuex-module-decorators'
import { ChatRoom, User, UserStatus } from '@/utils/types/index'
import { chatRoomApi } from '@/api/chat.service'
import store from './index'

@Module({ dynamic: true, store, name: 'chat-rooms' })
class ChatRoomModule extends VuexModule {
  rooms: ChatRoom[] = [];
  other_rooms: ChatRoom[] = [];
  selectedChatRoom: ChatRoom | undefined = undefined;
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
  }

  @Mutation
  setUserTyping(user_id: number) {
    this.userTyping = this.selectedChatRoom?.users.find((u: User) => u.id === user_id) as User;
    setTimeout(() => {
        this.userTyping = {} as User;
    }, 3000);
  }
  
  @Mutation
  setSelectedRoomById(room_id: number) {
    this.selectedChatRoom = this.rooms.find(r => r.id === room_id);
  }

  @Mutation
  resetRooms() {
    this.rooms = [];
    this.other_rooms = [];
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