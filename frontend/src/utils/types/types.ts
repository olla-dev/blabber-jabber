export type Message = {
    chat_room_id: number,
    author_id: number,
    content: string;
    status: string;
    sent_time_utc: Date;
    created_at: Date;
    updated_at: Date;
};

export type ChatRoom = {
    id: number,
    name: string,
    content: string;
    description: string;
    created_at: Date;
    updated_at: Date;
};
