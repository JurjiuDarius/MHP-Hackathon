import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Booking } from '../models/booking';
import { environment } from '../environments/development';
@Injectable({
  providedIn: 'root',
})
export class BookingService {
  private apiUrl = environment.apiURL;
  constructor(private http: HttpClient) {}

  getBookings(): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookings/`);
  }

  createBooking(booking: Booking) {
    return this.http.post(`${this.apiUrl}/bookings/`, booking);
  }

  updateBooking(booking: Booking) {
    return this.http.put(`${this.apiUrl}/bookings/`, booking);
  }

  deleteBooking(bookingID: number) {
    return this.http.delete(`${this.apiUrl}/bookings/${bookingID}`);
  }
}
