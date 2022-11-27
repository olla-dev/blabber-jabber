import {
  Module,
  VuexModule,
  MutationAction,
  Mutation,
  getModule
} from 'vuex-module-decorators'
import { ChatRoom } from '@/utils/types/index'
import { chatRoomApi } from '@/api/chat.service'
import store from './index'

@Module({ dynamic: true, store, name: 'chat-rooms' })
class ChatRoomModule extends VuexModule {
  rooms: ChatRoom[] = [];
  other_rooms: ChatRoom[] = [];
  selectedChatRoom: ChatRoom | undefined = undefined;

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
}

const chatRoomModule = getModule(ChatRoomModule)
export default chatRoomModule