import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/development';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = environment.apiURL;

  constructor(private http: HttpClient) {}

  getUsers(): Observable<any> {
    return this.http.get(`${this.apiUrl}/user/users`);
  }
}
