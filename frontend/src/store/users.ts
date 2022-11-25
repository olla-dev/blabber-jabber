import {
  Module,
  VuexModule,
  MutationAction,
  getModule,
  Mutation
} from 'vuex-module-decorators'
import { UserCredentials, UserRegister } from '@/utils/types/index'
import { userApi } from '@/api/user.service'
import store from './index'
  
@Module({ dynamic: true, store, name: 'users'})
class UserModule extends VuexModule {
    user: any = {};
    isAuthenticated = localStorage.getItem('isAuthenticated') ? localStorage.getItem('isAuthenticated') === 'true' : false;;
    authToken = localStorage.getItem('authToken') ? localStorage.getItem('authToken') : '';
    registrationSuccess = false;
    errorCode?: number = undefined;
    error = {}
  
    @MutationAction
    async login(credentials: UserCredentials) {
      debugger
      try {  
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
              user: {},
              authToken: response.auth_token,
              isAuthenticated: true,
              errorCode: undefined,
              error: {}
          }
        }
      } catch (error: any) {
        localStorage.removeItem('authToken');
        localStorage.removeItem('isAuthenticated');
        
        return {
            user: {},
            authToken: '',
            isAuthenticated: false,
            errorCode: error.status,
            error: error.data
        }
      }
    }

    @MutationAction
    async register(user: UserRegister) {
      try {
        const response: any = await userApi.register(user);
        if(response.error) {
          console.log('Registration failed');
          return {
              user: {},
              registrationSuccess: false,
              errorCode: response.code,
              error: response.error
          }
        } else {
          console.log('Registration success');
          
          return {
              user: {...response.data},
              registrationSuccess: true,
              errorCode: undefined,
              error: {}
          }
        }
      } catch (error: any) {
        return {
            user: {},
            registrationSuccess: false,
            errorCode: error.status,
            error: error.data
        }
      }
    }

    @MutationAction
    async logout() {
      if(!this.isAuthenticated) {
        throw 'Unauthenticated';
      }
      await userApi.logout();

      localStorage.removeItem('authToken');
      localStorage.removeItem('isAuthenticated');

      return { 
        authToken: '', 
        user: {}, 
        isAuthenticated: false
      }
    }

    @Mutation
    setRegistrationSuccess(value: boolean) {
      this.registrationSuccess = value;
    }
  }
  
  const userModule = getModule(UserModule)
  export default userModule