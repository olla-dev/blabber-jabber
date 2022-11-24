import { httpClient } from './client'
import { ChatRoom } from '../utils/types'

class ChatRoomApi {
    async fetchRooms(): Promise<ChatRoom[]> {
        return await httpClient.get('chat/rooms');
    }
    
    /**
     * Fetches messages for a chat room. 
     * @returns 
     */
    async fetchRoom(room_id: number): Promise<ChatRoom> {
        return await httpClient.get('chat/room/'+room_id);
    }
}

export const chatRoomApi = new ChatRoomApi();