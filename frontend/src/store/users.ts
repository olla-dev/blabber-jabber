import {
    Module,
    VuexModule,
    MutationAction,
    Mutation,
    getModule
  } from 'vuex-module-decorators'
  import { User } from '@/utils/types/index'
  import { userApi } from '@/api/user.service'
  import store from './index'
  
  @Module({ dynamic: true, store, name: 'users' })
  class UserModule extends VuexModule {
    user: any = {};
    isAuthenticated = false;
    authToken = '';
    isLoading = false;
    errorCode?: number = undefined;
    error: any = {}
  
    get getUser(): User | undefined {
      return this.user;
    }
  
    @MutationAction
    async login(username: string, password: string) {
      const response: any = await userApi.login(username, password);
      if(response.error) {
        return {
            user: undefined,
            authToken: '',
            isAuthenticated: false,
            errorCode: response.code,
            error: response.error
        }
      } else {
        return {
            authToken: response.token,
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