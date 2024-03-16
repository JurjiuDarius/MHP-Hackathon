import { Injectable } from '@angular/core';
import { environment } from '../environments/development';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BookableService {
  private apiUrl: string = environment.apiURL;

  constructor(private http: HttpClient) {}

  getCapacityForBookable(bookableId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookables/${bookableId}/capacity`);
  }
  getAvailabilityForBookable(
    bookableId: string,
    date: string
  ): Observable<any> {
    return this.http.post(`${this.apiUrl}/bookables/availability`, {
      bookableId,
      date,
    });
  }
  getBookingColors(date: string) {
    return this.http.post(`${this.apiUrl}/bookables/colors`, { date });
  }
}
