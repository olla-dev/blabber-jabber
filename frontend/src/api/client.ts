import axios, {
  AxiosInstance,
  AxiosResponse,
  AxiosRequestConfig
} from "axios";
import { HttpCode } from './http_codes'

const headers = {
  "Accept": "application/json",
  "Content-Type": "application/json; charset=utf-8",
}

const injectToken = (config: AxiosRequestConfig): AxiosRequestConfig => {
  const token = localStorage.getItem("authToken");

  if (token != null) {
    config.headers!.Authorization = `Token ${token}`;
  }
  return config;
};

/**
 * this api helper is inspired from: https://altrim.io/posts/axios-http-client-using-typescript
 */
class HttpClient {
  private instance: AxiosInstance | null = null;

  private get client(): AxiosInstance {
    return this.instance != null ? this.instance : this.initClient();
  }

  initClient() {
    const axiosClient = axios.create({
      baseURL: process.env.VUE_APP_API_BASE_URL,
      headers,
      withCredentials: false,
    });

    axiosClient.interceptors.request.use(injectToken, (error) => Promise.reject(error));

    axiosClient.interceptors.response.use(
      (response) => response,
      (error) => {
        const { response } = error;
        return this.handleError(response);
      }
    );

    this.instance = axiosClient;
    return axiosClient;
  }

  /**
   * Dispatch a notification with the proper 
   * message about the api error
   * @param error 
   * @returns void
   */
  private handleError(error: any) {
    const { status } = error;

    switch (status) {
      case HttpCode.BAD_REQUEST: {
        break;
      }
      case HttpCode.INTERNAL_SERVER_ERROR: {

        break;
      }
      case HttpCode.TOO_MANY_REQUESTS: {

        break;
      }
      default: {

        break;
      }
    }

    return Promise.reject(error);
  }

  async get(url: string) {
    return await this.client.get(url).then((response: AxiosResponse) => response);
  }

  async post<T>(url: string, body: T) {
    return await this.client.post(url, body).then((response: AxiosResponse) => response);
  }

  async put<T>(url: string, body: T) {
    return await this.client.put(url, body).then((response: AxiosResponse) => response);
  }

  async delete(url: string) {
    return await this.client.delete(url).then((response: AxiosResponse) => response.status);
  }
}

export const httpClient = new HttpClient();
