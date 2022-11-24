import { httpClient } from './client'
import { HttpCode } from './http_codes'
import { ApiError, User, UserRegister } from '../utils/types'

class UserApi {
    async register(user: UserRegister): Promise<User | ApiError > {
        const response = await (await httpClient.post('token/login/', user));
        if(response.status == HttpCode.SUCCESS){
            return response.data;
        } else {
            return {
                code: response.status,
                error: response.data
            };
        }
    }

    async login(username: string, password: string): Promise<User | ApiError> {
        const formData = {
            username: username,
            password: password
        }
        const response = await (await httpClient.post('token/login/', formData));
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
     * Logout user using djoser token logout endpoint
     *  
     * @returns HTTP_204_NO_CONTENT
     */
    async logout() : Promise<boolean> {
        const response = await httpClient.post('token/logout/', {});
        return response.status == HttpCode.NO_CONTENT
    }
}

export const userApi = new UserApi();