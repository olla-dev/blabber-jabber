import { httpClient } from './client'
import { HttpCode } from './http_codes'
import { ApiError, User, UserCredentials, UserRegister } from '../utils/types'

class UserApi {
    async register(user: UserRegister): Promise<User | ApiError > {
        const response = await httpClient.post('users/', user);
        if(response.status == HttpCode.CREATED){
            return response.data;
        } else {
            return {
                code: response.status,
                error: response.data
            }
        }
    }

    async login(credentials: UserCredentials): Promise<User | ApiError> {
        const response = await httpClient.post('token/login/', credentials);
        if(response.status == HttpCode.SUCCESS){
            return response.data;
        } else {
            return {
                code: response.status,
                error: response.data
            }
        }
    }
    
    /**
     * Logout user using djoser token logout endpoint
     *  
     * @returns HTTP_204_NO_CONTENT
     */
    async logout() : Promise<boolean> {
        const response = await httpClient.post('token/logout/', {});
        return response.status == HttpCode.NO_CONTENT;
    }
}

export const userApi = new UserApi();