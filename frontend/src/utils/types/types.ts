export type ApiError = {
    code: number;
    error: {}
}
export type UserCredentials = {
    username: string, 
    password: string
}
export type UserStatus = {
    user_id: number, 
    status: number
}

export type UserProfile = {
    avatar: string;
    bio: string;
    age: number;
    is_verified: boolean;
    is_banned: boolean;
    is_premium: boolean;
    social_facebook: string;
    social_instagram: string;
    social_youtube: string;
    social_blog: string;
    online?: number;
};

export type UserRegister = {
    first_name: string,
    last_name: string;
    username: string;
    email: string;
    password: string;
    re_password: string;
};

export type User = {
    id: number,
    first_name: string,
    last_name: string;
    email: string;
    profile: UserProfile;
};

export type Message = {
    id: number,
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
    description: string;
    created_at: Date;
    updated_at: Date;
    users: User[];
};
