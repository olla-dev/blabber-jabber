import { httpClient } from './client'
import { ApiError, ChatRoom } from '../utils/types'
import { HttpCode } from './http_codes';

class ChatRoomApi {
    async fetchRooms(): Promise<ChatRoom[] | ApiError> {
        const response = await httpClient.get('chat/rooms');
        if(response.status == HttpCode.SUCCESS){
            return response.data;
        } else {
            return {
                code: response.status,
                error: response.data
            };
        }
    }
    
    /**
     * Fetches messages for a chat room. 
     * @returns 
     */
    async fetchRoom(room_id: number): Promise<ChatRoom | ApiError> {
        const response = await httpClient.get('chat/room/'+room_id);
        if(response.status == HttpCode.SUCCESS){
            return response.data;
        } else {
            return {
                code: response.status,
                error: response.data
            };
        }
    }
}

export const chatRoomApi = new ChatRoomApi();