import { Injectable } from '@angular/core';
import { environment } from '../environments/development';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class StatisticsService {
  private apiUrl = environment.apiURL;
  constructor(private http: HttpClient) {}

  public getOfficeOccupancy(date: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/statistics/office-occupation`, {
      date,
    });
  }
}
