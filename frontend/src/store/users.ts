import {
  Module,
  VuexModule,
  MutationAction,
  getModule
} from 'vuex-module-decorators'
import { UserCredentials } from '@/utils/types/index'
import { userApi } from '@/api/user.service'
import store from './index'
  
@Module({ dynamic: true, store, name: 'users'})
class UserModule extends VuexModule {
    user: any = {};
    isAuthenticated = localStorage.getItem('isAuthenticated') ? localStorage.getItem('isAuthenticated') === 'true' : false;;
    authToken = localStorage.getItem('authToken') ? localStorage.getItem('authToken') : '';
    isLoading = false;
    errorCode?: number = undefined;
    error = {}
  
    @MutationAction
    async login(credentials: UserCredentials) {
      const response: any = await userApi.login(credentials);
      if(response.error) {
        localStorage.removeItem('authToken');
        localStorage.removeItem('isAuthenticated');
        
        return {
            user: {},
            authToken: '',
            isAuthenticated: false,
            errorCode: response.code,
            error: response.error
        }
      } else {
        // save token to local storage
        localStorage.setItem('authToken', response.auth_token);
        localStorage.setItem('isAuthenticated', 'true');

        return {
            authToken: response.auth_token,
            isAuthenticated: true,
            errorCode: undefined,
            error: {}
        }
      }
    }

    @MutationAction
    async logout() {
      if(!this.isAuthenticated) {
        throw 'Unauthenticated';
      }
      await userApi.logout();
      return { 
        authToken: '', 
        user: {}, 
        isAuthenticated: false, 
        isLoading: false 
      }
    }
  }
  
  const userModule = getModule(UserModule)
  export default userModule