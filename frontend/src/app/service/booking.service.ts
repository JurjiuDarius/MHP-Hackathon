import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Booking } from '../models/booking';
@Injectable({
  providedIn: 'root',
})
export class BookingService {
  constructor(private http: HttpClient) {}

  getBookings(): Observable<any> {
    return this.http.get('http://localhost:5000/bookings');
  }

  createBooking(booking: Booking) {
    return this.http.post('http://localhost:5000/bookings', booking);
  }

  updateBooking(booking: Booking) {
    return this.http.put('http://localhost:5000/bookings', booking);
  }

  deleteBooking(bookingID: number) {
    return this.http.delete(`http://localhost:5000/bookings/{bookingID}`);
  }
}
